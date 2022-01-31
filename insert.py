from json import load
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
import glob, os

import pandas as pd

with open("config.json") as jsonfile:
    db = load(jsonfile)['database']

engine = create_engine(URL(db['drivername'], db['username'], db['password'], db['host'], db['port'], db['database']))


for file in glob.glob("*.csv"):
    print(file)
    df = pd.read_csv(file, delimiter=',', quotechar='"')
    df.to_sql('tiktok_raw', engine, if_exists='append')
    os.rename(file, file+'.old')
