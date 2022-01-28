from json import load
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL



with open("config.json") as jsonfile:
    db_config = load(jsonfile)['database_dml']

engine = create_engine(URL(db_config['drivername'], db_config['username'],
                           db_config['password'], db_config['host'],
                           db_config['port'], db_config['database']))
