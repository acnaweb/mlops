import pandas as pd
import pytest

def test_entrada_valida():
    df = pd.read_csv("data/sample_ref.csv")
    required_columns = {"feature1", "feature2", "feature3", "target"}
    assert required_columns.issubset(df.columns), "Colunas obrigatórias ausentes"
    assert df.isnull().sum().sum() == 0, "Dados de entrada possuem valores nulos"