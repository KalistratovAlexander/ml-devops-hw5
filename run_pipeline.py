import subprocess


def main():
    steps = [
        "python src/preprocess.py",
        "python src/validate_deepchecks.py",
        "python src/train.py",
        "python src/evaluate.py",
        "python src/drift_evidently.py",
    ]
    for cmd in steps:
        subprocess.run(cmd, shell=True, check=True)


if __name__ == "__main__":
    main()

