import pandas as pd
import pickle
import json
import os
import mlflow
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

def main():
    if not os.path.exists("data/test.csv"):
        raise FileNotFoundError("Run preprocess.py first")
    
    df = pd.read_csv("data/test.csv")
    X = df.drop(columns=["target"])
    y = df["target"]
    
    with open("models/model.pkl", "rb") as f:
        model = pickle.load(f)
    
    # Predict
    predictions = model.predict(X)
    
    # Metrics
    acc = accuracy_score(y, predictions)
    f1 = f1_score(y, predictions, average='weighted')
    precision = precision_score(y, predictions, average='weighted')
    recall = recall_score(y, predictions, average='weighted')
    
    # MLflow logging
    mlflow.set_experiment("iris_classification")
    with mlflow.start_run():
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("f1_score", f1)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
    
    # Save report
    os.makedirs("reports", exist_ok=True)
    metrics = {
        "accuracy": acc,
        "f1_score": f1,
        "precision": precision,
        "recall": recall
    }
    
    with open("reports/metrics.json", "w") as f:
        json.dump(metrics, f, indent=4)
        
    print(f"Evaluation: Accuracy={acc:.3f}, F1={f1:.3f}")

if __name__ == "__main__":
    main()

