import pandas as pd
from deepchecks.tabular import Dataset
from deepchecks.tabular.suites import data_integrity
import os

def main():
    if not os.path.exists("data/train.csv"):
        raise FileNotFoundError("Run preprocess.py first")
    
    df = pd.read_csv("data/train.csv")
    
    # Создание Deepchecks датасета
    ds = Dataset(df, label="target", cat_features=[])
    
    # Запуск Integrity Suite
    suite = data_integrity()
    result = suite.run(ds)
    
    # Сохранение отчета
    os.makedirs("reports", exist_ok=True)
    result.save_as_html("reports/deepchecks_report.html", connected=True)
    
if __name__ == "__main__":
    main()

