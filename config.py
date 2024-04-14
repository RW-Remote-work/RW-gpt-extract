# -*- coding: utf-8 -*-
import os

try:
    from local_config import LOG_DIR
except ImportError:
    LOG_DIR = '/home/work/log'
    pass
BASE_DIRS = os.path.dirname(__file__)

DEBUG = True

setting = {
    # Absolute path to statics file
    "static_path": os.path.join(BASE_DIRS, "statics/static"),
    # Absolute path to template file
    "template_path": os.path.join(BASE_DIRS, "statics"),
    # 设置Tornado是否工作在生产环境 设为true会自动重启
    "static_hash_cache": False,
    "serve_tracehack": True,
    "compress_response": True,
}

FDS_ACCESS_KEY = 'AKB3FUE7Z2PL74GHBK'
FDS_ACCESS_SECRET = 'EXB6d5LScq2v4OogmaPpn/hn9TmVCCTeP8SzYEXW'
FDS_ENDPOINT = 'cnbj1-fds.api.xiaomi.net'

# 设置宕机判断阈值为30min
DOWNTIME = 30

# 首页推荐页猜你想看接口名称
FRONT_GUESS_WATCH = 'guessWatch'

DB_URL = 'mysql+pymysql://admin:d1c70c30bc5c2cba2d6022aea58d501d@10.38.160.191:3306/avatar_cms'
DB_URL_OTT = 'mysql+pymysql://tv_ashes_s:jJA43gFgUKpSPkyki4fYCcaZUbflEWDC@10.132.108.40:6657/tv_ashes'

INTERFACE_URL = "http://pre.avatar.n.duokanbox.com/api/v1/recService/interface?key="

REDIS_META_CONFIG_MAP = {
    'mi_video': {
        'master': {
            'host': '10.142.181.13',
            'port': 5395,
            'timeout': 0.1
        },
        'slaves': [],
        'db': 1,
        'password': "aaca0f5eb4d2d98a6ce6dffa99f8254b",
    },
    'mi_tv': {
        'master': {
            'host': '10.142.181.13',
            'port': 5395,
            'timeout': 0.1
        },
        'slaves': [],
        'db': 6,
        'password': "aaca0f5eb4d2d98a6ce6dffa99f8254b",
    }
}

REDIS_CLUSTER_CONFIG_MAP = {
    'preference_cluster': [
        {
            'host': '10.132.19.6',
            'port': 34385,
            'socket_timeout': 0.5
        },
        {
            'host': '10.132.20.1',
            'port': 34387,
            'socket_timeout': 0.5
        },
        {
            'host': '10.132.21.5',
            'port': 34386,
            'socket_timeout': 0.5
        },
        {
            'host': '10.132.20.1',
            'port': 34384,
            'socket_timeout': 0.5
        },
        {
            'host': '10.132.21.5',
            'port': 34383,
            'socket_timeout': 0.5
        },
        {
            'host': '10.132.19.6',
            'port': 34382,
            'socket_timeout': 0.5
        },
    ],
}

CHANNEL_SOLR_HOST = "10.98.16.215:9160/mitv/search/movie/select"

MIVIDEO_DB = 'mi_video'
MITV_DB = 'mi_tv'
PREFERENCE_DB = 'preference_cluster'
AVATAR_HOST = 'pre.avatar.n.duokanbox.com'

try:
    from local_config import DB_URL
    from local_config import INTERFACE_URL
    from local_config import DEBUG
    from local_config import AVATAR_HOST
    from local_config import CHANNEL_SOLR_HOST
except ImportError:
    pass
