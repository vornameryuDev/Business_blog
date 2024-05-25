#서버환경에서 사용할 config

from config.default import *



SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
secret_key = b'7\x95\x10\x86\x1d\x1et\xf3,=\xd7{?\x08\xa0\xdd'