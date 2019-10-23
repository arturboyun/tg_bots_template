from peewee import *

from bot.config import DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASS

database = PostgresqlDatabase(DB_NAME,
                              host=DB_HOST,
                              port=DB_PORT,
                              user=DB_USER,
                              password=DB_PASS)


class BaseModel(Model):
    class Meta:
        database = database
