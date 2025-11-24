import pandas as pd
from sklearn.model_selection import train_test_split
import os
import yaml

def main():
    # Загрузка параметров
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)
    test_size = params["split"]["test_size"]
    random_state = params["split"]["random_state"]

    # Загрузка сырых данных из CSV (версионируется через DVC)
    df = pd.read_csv("data/raw/iris.csv")
    
    # Сплит
    train, test = train_test_split(df, test_size=test_size, random_state=random_state)
    
    # Сохранение
    os.makedirs("data", exist_ok=True)
    train.to_csv("data/train.csv", index=False)
    test.to_csv("data/test.csv", index=False)
    print("Data processed and saved to data/")

if __name__ == "__main__":
    main()
