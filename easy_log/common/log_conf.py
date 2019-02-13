# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @createTime: 2019/2/13 22:17
# @author: scdev030
log_str = '''{
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(levelname)s - %(module)s.%(name)s : %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'mail': {
            'format': '%(asctime)s : %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'default': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'default',
                'filename': 'log_data/app.log',
                'maxBytes': 5 * 1024 * 1024,
                'backupCount': 30,
            },
        'log_note': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': 'log_data/data.log',
            'maxBytes': 5 * 1024 * 1024,
            'backupCount': 30
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        'log_note': {
            'handlers': ['log_note', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
    },
    'mail':{
        'handlers': ['mail'],
        'level': 'CRITICAL',
        'propagate': False
    },
    'root': {
        'handlers': ['default', 'console'],
        'level': 'WARNING'
    },
}'''