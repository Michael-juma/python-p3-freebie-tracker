from models import *
from sqlalchemy import create_engine
from models import Base

engine = create_engine('sqlite:///lib/freebies.db')
Base.metadata.create_all(engine)
if __name__ == '__main__':
    print("Database migration complete. All tables created.")