from sqlalchemy import Table, Column, ForeignKey, Integer, Float, String, DateTime, MetaData
from sqlalchemy import create_engine
import csv


engine = create_engine('sqlite:///database.db', echo=False)


meta = MetaData()


stations = Table(
    'stations', meta,
    Column('id', Integer, primary_key=True),
    Column('station', String),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('elevation', Float),
    Column('name', String),
    Column('country', String),
    Column('state', String)
)


datapoints = Table(
    'datapoints', meta,
    Column('id', Integer, primary_key=True),
    #Column('station', String), #how to add foregin key?
    Column('datle', DateTime),
    Column('precipitation', Float),
    Column('tobs', Integer)
)


def csv_to_dict(csv_file):
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data


if __name__ == '__main__':
    meta.create_all(engine)
    conn = engine.connect()

    stations_list = csv_to_dict('venv/stations.csv')
    ins = stations.insert()
    conn.execute(ins, stations_list)

    datapoints_list = csv_to_dict('venv/datapoints.csv')
    ins = datapoints.insert()
    conn.execute(ins, datapoints_list)

    data = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()

    for dat in data:
        print(dat)