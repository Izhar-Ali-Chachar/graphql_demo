from sqlalchemy import Table, Column, Integer, String
from  sqlalchemy.sql.sqltypes import Integer, String

from conn.db import meta

users = Table(
    'user',
    meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(50)),
    Column('email', String(100)),
    Column('password', String(50))
)