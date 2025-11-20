"""
Быстрый старт проекта
Запускает полный ML пайплайн
"""

import subprocess
import sys

def run_command(cmd, description):
    print(f"\n{'='*60}")
    print(f"[{description}]")
    print(f"{'='*60}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"Ошибка в: {description}")
        sys.exit(1)

def main():
    print("\n" + "="*60)
    print("ML PIPELINE START")
    print("="*60)
    
    steps = [
        ("python src/preprocess.py", "1/5 Preprocessing data"),
        ("python src/validate_deepchecks.py", "2/5 Validating with Deepchecks"),
        ("python src/train.py", "3/5 Training model with MLflow"),
        ("python src/evaluate.py", "4/5 Evaluating model"),
        ("python src/drift_evidently.py", "5/5 Analyzing drift with Evidently"),
    ]
    
    for cmd, desc in steps:
        run_command(cmd, desc)
    
    print("\n" + "="*60)
    print("PIPELINE COMPLETE!")
    print("="*60)
    print("\nNext steps:")
    print("  - View MLflow UI: mlflow ui")
    print("  - Check reports: ls -lh reports/")
    print("  - Open deepchecks_report.html in browser")
    print("  - Open evidently_report.html in browser")

if __name__ == "__main__":
    main()

