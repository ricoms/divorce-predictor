from pathlib import Path

import numpy as np
import pytest

from divorce_predictor.data import DataLoader


def test_load_data_successfully():
    dataset_path = (
        Path(__file__).parent.parent.parent / "ml" / "input" / "data" / "divorce.csv"
    )
    data_loader = DataLoader(dataset_path=dataset_path, target_column="Class")
    X, y = data_loader.load_dataset()

    assert isinstance(X, np.ndarray)
    assert isinstance(y, np.ndarray)
    assert len(y.shape) == 1


def test_load_filenotfound():
    dataset_path = Path("bulhufas")
    with pytest.raises(FileNotFoundError):
        _ = DataLoader(dataset_path=dataset_path, target_column="variety")
