import os
import json
from pathlib import Path

def ensure_dir(directory):
    """Создает директорию, если её нет"""
    os.makedirs(directory, exist_ok=True)

def save_json(data, filepath):
    """Сохраняет данные в JSON"""
    ensure_dir(os.path.dirname(filepath))
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Saved: {filepath}")

def load_json(filepath):
    """Загружает данные из JSON"""
    with open(filepath, 'r') as f:
        return json.load(f)

def get_project_root():
    """Возвращает корневую директорию проекта"""
    return Path(__file__).parent.parent

def check_file_exists(filepath, error_msg="File not found"):
    """Проверяет существование файла"""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"{error_msg}: {filepath}")
    return True

