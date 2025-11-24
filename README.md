# Создание воспроизводимого ML-pipeline с использованием DVC и MLflow

## Цель проекта
Минимальный, но полноценный ML-проект с воспроизводимым пайплайном на DVC и логированием экспериментов в MLflow (метрики, параметры, артефакты).

## Структура
- `src/` — скрипты пайплайна (`preprocess.py`, `train.py`)
- `data/` — сырые и обработанные данные
- `dvc.yaml` — описание пайплайна
- `params.yaml` — гиперпараметры
- `models/` — сохранённая модель
- `mlruns/` — локальные логи MLflow

## Запуск
```bash
pip install -r requirements.txt
dvc pull || true
dvc repro
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Где смотреть MLflow UI: откройте http://127.0.0.1:5000 в браузере.

## Описание пайплайна
- `prepare`: читает сырые данные `data/raw/iris.csv`, делит на train и test по `params.yaml`, сохраняет `data/train.csv`, `data/test.csv`.
- `train`: обучает `RandomForestClassifier` с параметрами из `params.yaml`, логирует параметры, метрики (accuracy, f1) и артефакты в MLflow, сохраняет `models/model.pkl`.

Запуск воспроизводимости:
```bash
dvc repro
```

## Версионирование данных
Проект использует DVC:
- артефакты `data/train.csv`, `data/test.csv`, `models/model.pkl` — как `outs` стадий DVC;
- локальное удалённое хранилище можно добавить командой:
```bash
dvc remote add -d local ./dvcstore
dvc push
```



