from pathlib import Path

import pandas as pd

from divorce_predictor.base import BaseDataLoader


class DataLoader(BaseDataLoader):
    def __init__(self, dataset_path: Path, target_column: str):
        self.dataset_path = dataset_path
        if not self.dataset_path.is_file():
            raise FileNotFoundError
        self.target_column = target_column

    def load_dataset(self) -> pd.DataFrame:
        dataf = pd.read_csv(self.dataset_path, header=0, sep=";")
        feature_columns = [
            column for column in dataf.columns if column not in self.target_column
        ]
        X = dataf.loc[:, feature_columns].values
        y = dataf.loc[:, self.target_column].values
        return X, y
