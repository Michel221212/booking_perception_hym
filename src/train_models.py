import os
import time
import pandas as pd
import numpy as np
import joblib
import gzip
import spacy
import swifter
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, accuracy_score, f1_score, recall_score, precision_score
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import ComplementNB  # Cambio aquí para evitar valores negativos
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder

# Configurar el entorno
os.environ["LOKY_MAX_CPU_COUNT"] = "6"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Cargar modelo de procesamiento de lenguaje natural
nlp = spacy.load("es_core_news_md")

def preprocess_text(text):
    if pd.isna(text):
        return ""
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

# Entrenar modelo no supervisado (K-Means)
def train_unsupervised_model(df):
    print("\n🔹 Entrenando modelo no supervisado (K-Means)...")
    df["Opiniones Procesadas"] = df["Opiniones"].astype(str).swifter.apply(preprocess_text)
    vectorizer = TfidfVectorizer(max_features=300)
    X = vectorizer.fit_transform(df["Opiniones Procesadas"])
    
    os.makedirs("models", exist_ok=True)
    joblib.dump(vectorizer, "models/vectorizer.pkl")
    
    num_clusters = 5
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)  # Agregado n_init=10
    df["Cluster"] = kmeans.fit_predict(X)
    
    joblib.dump(kmeans, "models/kmeans_model.pkl")
    
    silhouette_avg = silhouette_score(X, df["Cluster"])
    print("Puntuación Silhouette Score:", silhouette_avg)
    return df, X, kmeans, vectorizer  # Asegurar que vectorizer se retorne correctamente

# Entrenar modelos supervisados
def train_supervised_models(df, vectorizer):
    print("\n🔹 Entrenando modelos supervisados...")

    # Verificar si la columna 'Grupo viaje' existe
    if "Grupo viaje" not in df.columns:
        raise ValueError("❌ Error: La columna 'Grupo viaje' no se encuentra en el DataFrame.")

    label_encoder = LabelEncoder()
    df["Etiqueta"] = label_encoder.fit_transform(df["Grupo viaje"])
    joblib.dump(label_encoder, "models/label_encoder.pkl")
    
    if vectorizer is None:
        raise ValueError("❌ Error: El vectorizador no se ha pasado correctamente.")
    
    X_train, X_test, y_train, y_test = train_test_split(df["Opiniones Procesadas"], df["Etiqueta"], test_size=0.2, random_state=42)
    X_train_vec = vectorizer.transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    models = {
        "Naïve Bayes": ComplementNB(),  # Usamos ComplementNB para evitar errores con valores negativos
        "Random Forest": RandomizedSearchCV(RandomForestClassifier(random_state=42), param_distributions={"n_estimators": [50, 100, 200], "max_depth": [10, 20, 30]}, cv=3, scoring='accuracy', n_jobs=-1, n_iter=10),
        "XGBoost": RandomizedSearchCV(XGBClassifier(eval_metric='logloss', use_label_encoder=False), param_distributions={"n_estimators": [50, 100, 200], "max_depth": [3, 6, 9]}, cv=3, scoring='accuracy', n_jobs=-1, n_iter=10)
    }
    
    best_model = None
    best_score = 0
    results = []
    
    for name, model in models.items():
        print(f"\n▶ Entrenando {name}...")
        start_time = time.time()
        model.fit(X_train_vec, y_train)
        train_time = time.time() - start_time
        
        start_time = time.time()
        y_pred = model.predict(X_test_vec)
        predict_time = time.time() - start_time
        
        metrics = {
            "Modelo": name,
            "Accuracy": accuracy_score(y_test, y_pred),
            "F1-score": f1_score(y_test, y_pred, average='weighted'),
            "Recall": recall_score(y_test, y_pred, average='weighted'),
            "Precision": precision_score(y_test, y_pred, average='weighted'),
            "Tiempo Entrenamiento (s)": train_time,
            "Tiempo Predicción (s)": predict_time
        }
        results.append(metrics)
        
        print(f"\nMétricas para {name}:")
        for metric, value in metrics.items():
            print(f"{metric}: {value:.4f}" if isinstance(value, float) else f"{metric}: {value}")
        
        if metrics["Accuracy"] > best_score:
            best_score = metrics["Accuracy"]
            best_model = model.best_estimator_ if isinstance(model, RandomizedSearchCV) else model
    
    return best_model, results, label_encoder

# Función principal de entrenamiento
def train_and_save_models(df):
    df, X, kmeans, vectorizer = train_unsupervised_model(df)  # Capturamos vectorizer aquí
    best_model, results, label_encoder = train_supervised_models(df, vectorizer)  # Pasamos vectorizer
    
    model_bundle = {
        "supervised_model": best_model,
        "unsupervised_model": kmeans,
        "vectorizer": vectorizer,
        "label_encoder": label_encoder
    }
    
    best_model_name = "models/mejor_modelo.gz"
    with gzip.open(best_model_name, "wb") as f:
        joblib.dump(model_bundle, f)
    
    print(f"✅ Modelos combinados guardados en {best_model_name}")
    
    results_df = pd.DataFrame(results)
    results_df.to_csv("data/results/model_results.csv", index=False)
    print("✅ Métricas guardadas en data/results/model_results.csv")
    plot_metrics(results_df)
    
    return best_model_name

def plot_metrics(results_df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Accuracy", y="Modelo", data=results_df, palette="viridis")
    plt.xlabel("Precisión")
    plt.ylabel("Modelo")
    plt.title("Comparación de Modelos Supervisados")
    plt.show()