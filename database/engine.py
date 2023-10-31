from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


db_uri = "mysql://root:admin@localhost/extendvision"
engine = create_engine(db_uri)
Base = declarative_base()