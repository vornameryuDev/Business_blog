secret_key = 'dev'

db = {
    'user': 'root',
    'pw': '123123',
    'host': 'localhost',
    'port': 3306,
    'db': "b5randj"
}

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{user}:{pw}@{host}:{port}/{db}?charset=utf8".format(user=db['user'], pw=db['pw'], host=db['host'], port=db['port'], db=db['db'])
SQLALCEMY_TRACK_MODIFICATIONS = False