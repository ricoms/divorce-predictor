curl https://archive.ics.uci.edu/ml/machine-learning-databases/00497/divorce.rar --output ml/input/data/divorce.rar

unar --quiet -D ml/input/data/divorce.rar -o ml/input/data/
rm ml/input/data/divorce.rar
rm ml/input/data/divorce.xlsx
