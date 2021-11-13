#!/usr/bin/env python
from pathlib import Path
from divorce_predictor.data import DataLoader
from divorce_predictor.experiment import Experiment

if __name__ == "__main__":
    print("Begin train.py")
    project_root = Path(__file__).parent.parent
    dataset_path = project_root / "ml" / "input" / "data" / "divorce.csv"
    output_path = project_root / "ml" / "output"
    data_loader = DataLoader(dataset_path=dataset_path, target_column="Class")
    X, y = data_loader.load_dataset()

    experiment = Experiment(X, y)

    experiment.setup()
    experiment.run()
    experiment.persist(output_path)

    print("End train.py")
