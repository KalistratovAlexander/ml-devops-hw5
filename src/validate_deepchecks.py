import pandas as pd
from deepchecks.tabular import Dataset
from deepchecks.tabular.suites import data_integrity
import os

def main():
    if not os.path.exists("data/train.csv"):
        raise FileNotFoundError("Run preprocess.py first")
    
    df = pd.read_csv("data/train.csv")
    
    # Create Deepchecks dataset
    ds = Dataset(df, label="target", cat_features=[])
    
    # Run data integrity suite
    suite = data_integrity()
    result = suite.run(ds)
    
    # Save report
    os.makedirs("reports", exist_ok=True)
    # Save as HTML with embedded resources to avoid CDN dependencies
    result.save_as_html("reports/deepchecks_report.html", connected=True)
    
    print("Deepchecks validation completed. Report saved to reports/deepchecks_report.html")

if __name__ == "__main__":
    main()

