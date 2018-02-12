import os
from app import db_engine as engine
from app.settings import project_config


def write_demo_records():
    with open(os.path.join(project_config.APP_DIR, 'sql', 'fill_test_db.sql'), 'r') as sql_file:
        query = list(
            filter(None, sql_file.read().split(';'))
        )

    for line in query:
        engine.execute(line)
