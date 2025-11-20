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
    
    # MLflow tracking
    mlflow.set_experiment("iris_classification")
    
    with mlflow.start_run():
        n_estimators = 100
        max_depth = 5
        
        # Log params
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("random_state", 42)
        
        # Train
        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=42
        )
        model.fit(X, y)
        
        # Log model
        mlflow.sklearn.log_model(model, "model")
        
        # Save locally
        os.makedirs("models", exist_ok=True)
        with open("models/model.pkl", "wb") as f:
            pickle.dump(model, f)
        
        print("Model trained and logged to MLflow")

if __name__ == "__main__":
    main()
