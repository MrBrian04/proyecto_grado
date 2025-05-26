from sqlalchemy import create_engine, colum, integer, string
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmarker


engine = create_engine("Sqlite:///proyecto.db", echo=True)
base = declarative_base()


DATABASE_URL = "mysql+pymysql://root:@localhost:3306/pro" \

db = SQLALchemy()