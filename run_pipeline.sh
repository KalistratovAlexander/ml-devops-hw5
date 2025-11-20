#!/bin/bash
# Полный ML пайплайн

echo "=== ML Pipeline Start ==="

echo "[1/5] Preprocessing data..."
python src/preprocess.py

echo "[2/5] Validating with Deepchecks..."
python src/validate_deepchecks.py

echo "[3/5] Training model with MLflow..."
python src/train.py

echo "[4/5] Evaluating model..."
python src/evaluate.py

echo "[5/5] Analyzing drift with Evidently..."
python src/drift_evidently.py

echo "=== Pipeline Complete ==="
echo "View MLflow UI: mlflow ui"
echo "Reports saved in: reports/"

