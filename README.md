# ML DevOps Homework 5

Воспроизводимый ML-проект с интеграцией MLflow, Deepchecks, EvidentlyAI и CI/CD.

## Быстрый старт

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск пайплайна
python run_pipeline.py
# или
./run_pipeline.sh

# Просмотр MLflow UI
mlflow ui
```

## Структура проекта

```
ml-devops-hw5/
├── src/                        # Исходный код
│   ├── preprocess.py           # Подготовка данных
│   ├── train.py                # Обучение + MLflow
│   ├── evaluate.py             # Оценка + MLflow
│   ├── validate_deepchecks.py  # Deepchecks валидация
│   └── drift_evidently.py      # Evidently анализ дрейфа
├── data/                       # Данные (генерируются)
├── models/                     # Модели (генерируются)
├── reports/                    # Отчеты (генерируются)
├── notebooks/                  # Jupyter notebooks
├── .github/workflows/          # GitHub Actions
├── .gitlab-ci.yml              # GitLab CI
├── Dockerfile                  # Docker образ
└── requirements.txt            # Зависимости
```

## Компоненты

- **MLflow** - отслеживание экспериментов
- **Deepchecks** - проверка качества данных
- **EvidentlyAI** - анализ дрейфа данных
- **GitHub Actions / GitLab CI** - автоматизация

## CI/CD

### GitHub Actions
При push в `main` автоматически запускается пайплайн.

### GitLab CI
5 стадий: preprocess → validate → train → evaluate → drift

## Docker

```bash
docker build -t ml-devops-hw5 .
docker run ml-devops-hw5
```

