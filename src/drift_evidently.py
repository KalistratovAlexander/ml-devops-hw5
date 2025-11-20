import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, DataQualityPreset
import os

def main():
    if not os.path.exists("data/train.csv") or not os.path.exists("data/test.csv"):
        raise FileNotFoundError("Run preprocess.py first")
    
    train_df = pd.read_csv("data/train.csv")
    test_df = pd.read_csv("data/test.csv")
    
    # Create report
    report = Report(metrics=[
        DataDriftPreset(),
        DataQualityPreset()
    ])
    
    report.run(reference_data=train_df, current_data=test_df)
    
    # Save report
    os.makedirs("reports", exist_ok=True)
    report.save_html("reports/evidently_report.html")
    
    print("Evidently drift analysis completed. Report saved to reports/evidently_report.html")

if __name__ == "__main__":
    main()

