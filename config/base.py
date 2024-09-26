from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:1234@localhost/ww2_normalized"

engine = create_engine(DATABASE_URL)
_session_factory = sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()

