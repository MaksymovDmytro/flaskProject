import logging
import os

from testAPI.storage.repository import ConnectionManager


def setup_logger() -> logging.Logger:
    logger = logging.getLogger("Flask-Project-Logger")
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


def gen_db_uri() -> str:
    """Generate URI string to connect to db from env variables of default values"""
    uri = f"{os.getenv('DB_MS', 'mysql+pymysql')}://" \
           f"{os.getenv('DB_USER', 'usr')}:" \
           f"{os.getenv('DB_PASSWORD', 'usr_pass')}@" \
           f"{os.getenv('DB_HOST', 'localhost')}:" \
           f"{os.getenv('DB_PORT', 3306)}/" \
           f"{os.getenv('DB_NAME', 'mysql_db')}"
    return uri


logger = setup_logger()

db_connection = ConnectionManager(uri=gen_db_uri())
