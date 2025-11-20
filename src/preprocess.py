import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import os

def main():
    # Загрузка данных
    data = load_iris(as_frame=True)
    df = data.frame
    
    # Сплит
    train, test = train_test_split(df, test_size=0.2, random_state=42)
    
    # Сохранение
    os.makedirs("data", exist_ok=True)
    train.to_csv("data/train.csv", index=False)
    test.to_csv("data/test.csv", index=False)
    print("Data processed and saved to data/")

if __name__ == "__main__":
    main()
