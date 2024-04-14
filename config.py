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