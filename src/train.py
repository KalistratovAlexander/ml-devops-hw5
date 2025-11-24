import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import pickle
import os
import mlflow
import mlflow.sklearn
import yaml

def main():
    if not os.path.exists("data/train.csv"):
        raise FileNotFoundError("Run preprocess.py first")
    if not os.path.exists("data/test.csv"):
        raise FileNotFoundError("Run preprocess.py first")
        
    train_df = pd.read_csv("data/train.csv")
    X_train = train_df.drop(columns=["target"])
    y_train = train_df["target"]
    test_df = pd.read_csv("data/test.csv")
    X_test = test_df.drop(columns=["target"])
    y_test = test_df["target"]
    
    # Параметры модели
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)
    n_estimators = params["model"]["n_estimators"]
    max_depth = params["model"]["max_depth"]
    random_state = params["model"]["random_state"]
    
    # MLflow логирование
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("iris_classification")
    
    with mlflow.start_run():
        # Логирование параметров
        mlflow.log_param("model", "RandomForestClassifier")
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("random_state", random_state)
        
        # Обучение модели
        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=random_state
        )
        model.fit(X_train, y_train)
        
        # Метрики на тесте
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        f1 = f1_score(y_test, preds, average="weighted")
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("f1_score", f1)
        
        # Логирование модели
        mlflow.sklearn.log_model(model, "model")
        
        # Сохранение модели локально
        os.makedirs("models", exist_ok=True)
        with open("models/model.pkl", "wb") as f:
            pickle.dump(model, f)
        # Логирование артефакта модели
        mlflow.log_artifact("models/model.pkl")
        
if __name__ == "__main__":
    main()
