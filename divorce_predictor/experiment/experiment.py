import json
from pathlib import Path

import numpy as np
import pandas as pd
from joblib import dump
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import cross_validate

from divorce_predictor.base import BaseExperiment


class Experiment(BaseExperiment):
    def __init__(self, X: np.ndarray, y: np.ndarray):
        self.X = X
        self.y = y

    def setup(self):
        self.scoring = ["roc_auc", "balanced_accuracy"]
        self.model = DummyClassifier()

    def run(self):
        self.cv_results = cross_validate(
            self.model,
            self.X,
            self.y,
            cv=5,
            return_train_score=True,
            return_estimator=True,
            n_jobs=-1,
            verbose=4,
            scoring=self.scoring,
        )
        best_model_idx = np.argmax(self.cv_results["test_roc_auc"])
        self.best_model = self.cv_results["estimator"][best_model_idx]
        self.predicted = self.best_model.predict(self.X)
        self.cv_results = pd.DataFrame(self.cv_results)

    def persist(self, output_path: Path):
        dump(self.best_model, output_path / "estimator.joblib")
        confusion_matrix_df = pd.DataFrame(
            {
                "actual": self.y,
                "predicted": self.predicted,
            }
        )
        confusion_matrix_df.to_csv(
            output_path / "confusion.csv",
            index=False,
            header=True,
        )
        cv_keys_to_save = [
            "fit_time",
            "test_roc_auc",
            "train_roc_auc",
            "test_balanced_accuracy",
            "train_balanced_accuracy",
        ]
        scores = self.cv_results.loc[:, cv_keys_to_save].to_dict(orient="records")
        scores = {"train": scores}
        avg_scores = self.cv_results.loc[:, cv_keys_to_save].mean().to_dict()

        with open(output_path / "avg_scores.json", "w") as fp:
            json.dump(avg_scores, fp, sort_keys=True, indent=4)
        with open(output_path / "scores.json", "w") as fp:
            json.dump(scores, fp, sort_keys=True, indent=4)
