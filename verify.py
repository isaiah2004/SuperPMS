from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect

engine = create_engine('sqlite:///data.db', echo=True)
Base = declarative_base()
Base.metadata.reflect(engine)

inspector = inspect(engine)
for table_name in inspector.get_table_names():
    print(f"Table: {table_name}")
    for column in inspector.get_columns(table_name):
        print(f"Column: {column['name']} Type: {column['type']}")
    print("\n")
