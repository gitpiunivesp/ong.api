from playhouse.postgres_ext import PostgresqlExtDatabase

import os

db = PostgresqlExtDatabase(
    database="ong",
    user=os.getenv("PGUSER"),
    password=os.getenv("PGPASSWORD"),
    host="db"
)
