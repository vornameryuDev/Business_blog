#서버환경에서 사용할 config

from logging.config import dictConfig
from config.default import *



SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
secret_key = b'7\x95\x10\x86\x1d\x1et\xf3,=\xd7{?\x08\xa0\xdd'

dictConfig({
    'version': 1, #고정값:1
    #로그를 출력할 형식
    'formatters': {
        'default': {
            # 현재시간, 로그레벨, 로그를 호출한 모듈, 출력내용
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    #로그를 출력할 방법
    'handlers': {
        #파일로 저장하겠음
        'file': {
            'level': 'INFO', #출력 로그 레벨
            'class': 'logging.handlers.RotatingFileHandler', #로그핸들러 클래스
            'filename': os.path.join(BASE_DIR, 'logs/myproject.log'), #로그파일명
            'maxBytes': 1024 * 1024 * 5,  # 로그파일크기: 5 MB
            'backupCount': 5, #로그 파일의 개수
            'formatter': 'default', #포맷터: default
        },
    },
    #최상위 로거
    'root': {
        'level': 'INFO', #로그레벨
        'handlers': ['file'] #핸들러: 파일
    }
})