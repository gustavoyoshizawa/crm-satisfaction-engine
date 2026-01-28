import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def extract_excel(relative_path):
    path = BASE_DIR / relative_path

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    df = pd.read_excel(path)

    expected_columns = [
        "cliente_id", "data_interacao", "canal",
        "tipo_interacao", "status", "data_resposta", "observacao"
    ]

    if not all(col in df.columns for col in expected_columns):
        raise ValueError("Estrutura do Excel inválida")

    return df
