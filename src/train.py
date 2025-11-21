import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
import mlflow
import mlflow.sklearn

def main():
    if not os.path.exists("data/train.csv"):
        raise FileNotFoundError("Run preprocess.py first")
        
    df = pd.read_csv("data/train.csv")
    X = df.drop(columns=["target"])
    y = df["target"]
    
    # MLflow логирование
    mlflow.set_experiment("iris_classification")
    
    with mlflow.start_run():
        n_estimators = 100
        max_depth = 5
        
        # Логирование параметров
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("random_state", 42)
        
        # Обучение модели
        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=42
        )
        model.fit(X, y)
        
        # Логирование модели
        mlflow.sklearn.log_model(model, "model")
        
        # Сохранение модели локально
        os.makedirs("models", exist_ok=True)
        with open("models/model.pkl", "wb") as f:
            pickle.dump(model, f)
        
if __name__ == "__main__":
    main()
