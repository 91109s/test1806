import logging

import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")# project_name 项目名称
django.setup()

def loddemo():
    logger = logging.getLogger('django')
    logger.info('hello logging')
    logger.info('hello logging and ----')
    print("jog ok")
if __name__ == '__main__':
    loddemo()