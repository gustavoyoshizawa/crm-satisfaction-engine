import os
import time
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError


def get_engine_with_retry(db_url, retries=15, delay=2):
    for attempt in range(retries):
        try:
            engine = create_engine(db_url)
            with engine.connect():
                print("✅ MySQL conectado com sucesso")
            return engine
        except OperationalError:
            print(f"⏳ MySQL indisponível... tentando novamente ({attempt + 1}/{retries})")
            time.sleep(delay)

    raise RuntimeError("❌ MySQL não respondeu a tempo")


def load_mysql(df):
    db_url = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:3306/"
        f"{os.getenv('DB_NAME')}"
    )

    engine = get_engine_with_retry(db_url)

    df.to_sql(
        "customer_profile",
        engine,
        if_exists="replace",
        index=False
    )

    print("✅ Dados carregados com sucesso no MySQL")
