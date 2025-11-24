import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import os
import yaml

def main():
    # Загрузка параметров
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)
    test_size = params["split"]["test_size"]
    random_state = params["split"]["random_state"]

    raw_path = "data/raw/iris.csv"
    # Если CSV отсутствует (например, в CI без dvc pull) — сгенерируем из sklearn
    if not os.path.exists(raw_path):
        os.makedirs("data/raw", exist_ok=True)
        load_iris(as_frame=True).frame.to_csv(raw_path, index=False)
    # Загрузка сырых данных из CSV (версионируется через DVC)
    df = pd.read_csv(raw_path)
    
    # Сплит
    train, test = train_test_split(df, test_size=test_size, random_state=random_state)
    
    # Сохранение
    os.makedirs("data", exist_ok=True)
    train.to_csv("data/train.csv", index=False)
    test.to_csv("data/test.csv", index=False)
    print("Data processed and saved to data/")

if __name__ == "__main__":
    main()
