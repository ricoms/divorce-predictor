from abc import ABC, abstractmethod
from pathlib import Path

import pandas as pd


class BaseDataLoader(ABC):
    @abstractmethod
    def load_dataset(self) -> pd.DataFrame:
        pass


class BaseExperiment(ABC):
    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def persist(self, output_path: Path):
        pass
