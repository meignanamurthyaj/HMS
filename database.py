from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL (Update password if needed)
URL = "mysql+pymysql://root:Meignanam%401992@localhost/Hospital_db"

# CREATE ENGINE
engine = create_engine(URL)

# CREATE SESSION
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)

# BASE CLASS
Base = declarative_base()