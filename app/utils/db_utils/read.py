import pandas as pd

from app import db_engine as engine
from app.models import demo_table
from sqlalchemy.sql import select


def sql_demo_to_html():

    conn = engine.connect()
    s = select([demo_table])
    result = conn.execute(s)

    lst = [{'id': res[0], 'name': res[1]} for res in result]

    df = pd.DataFrame(lst)
    return df.to_html()
