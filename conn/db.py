from sqlalchemy import create_engine, MetaData

engine = create_engine('sqlite:///data.sqlite')
meta = MetaData()

conn = engine.connect()