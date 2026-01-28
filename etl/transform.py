import pandas as pd
from datetime import datetime


# -------------------------
# QUALITY
# -------------------------
def apply_quality_rules(df):
    hoje = pd.to_datetime(datetime.today().date())

    df["flag_sem_resposta"] = df["data_resposta"].isna()
    df["flag_data_futura"] = df["data_interacao"] > hoje

    # Remove registros inválidos
    df = df[~df["flag_data_futura"]]

    return df


# -------------------------
# METRICS
# -------------------------
def calculate_metrics(df):
    hoje = pd.to_datetime(datetime.today().date())

    df["data_interacao"] = pd.to_datetime(df["data_interacao"])
    df["data_resposta"] = pd.to_datetime(df["data_resposta"], errors="coerce")

    # Interações abertas
    df_abertas = df[df["status"] != "Resolvido"].copy()

    # Dias sem resposta = hoje - data_interacao (SÓ abertas)
    df_abertas["dias_sem_resposta"] = (
        hoje - df_abertas["data_interacao"]
    ).dt.days

    # Métricas por cliente
    metrics = (
        df.groupby("cliente_id")
        .agg(
            qtd_interacoes_abertas=("status", lambda x: (x != "Resolvido").sum()),
            canal_preferido=("canal", lambda x: x.mode().iloc[0])
        )
        .reset_index()
    )

    # Máximo de dias sem resposta APENAS se houver abertos
    dias_abertos = (
        df_abertas.groupby("cliente_id")
        .agg(dias_sem_resposta=("dias_sem_resposta", "max"))
        .reset_index()
    )

    metrics = metrics.merge(dias_abertos, on="cliente_id", how="left")
    metrics["dias_sem_resposta"] = metrics["dias_sem_resposta"].fillna(0)

    return metrics



# -------------------------
# SCORE
# -------------------------
def calculate_score(metrics_df):
    metrics_df = metrics_df.copy()

    metrics_df["score"] = 100
    metrics_df["score"] -= metrics_df["qtd_interacoes_abertas"] * 20
    metrics_df["score"] -= metrics_df["dias_sem_resposta"].fillna(0) * 5

    metrics_df["score"] = metrics_df["score"].clip(0, 100)

    return metrics_df


# -------------------------
# SEGMENTATION
# -------------------------
def segment_customers(metrics_df):

    # 1️⃣ Criar score ANTES de classificar
    metrics_df["dias_sem_resposta"] = metrics_df["dias_sem_resposta"].fillna(0)

    metrics_df["score"] = (
        metrics_df["qtd_interacoes_abertas"] * 30 +
        metrics_df["dias_sem_resposta"] * 2
    )


    # 2️⃣ Classificação baseada no score
    def classify(row):
        if row["qtd_interacoes_abertas"] >= 2 or row["score"] >= 100:
            return "Crítico"
        elif row["qtd_interacoes_abertas"] == 1:
            return "Atenção"
        else:
            return "Saudável"


    metrics_df["segmento"] = metrics_df.apply(classify, axis=1)

    return metrics_df



# -------------------------
# AI SUMMARY
# -------------------------
def generate_summaries(metrics_df):
    metrics_df["resumo_ia"] = metrics_df.apply(
        lambda row: (
            f"Cliente classificado como {row['segmento']}, "
            f"score {row['score']}, "
            f"{row['qtd_interacoes_abertas']} interações abertas "
            f"e {row['dias_sem_resposta']} dias sem resposta."
        ),
        axis=1
    )

    return metrics_df
