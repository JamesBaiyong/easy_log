# encoding=utf-8
mail = {'mail': {
      'class': 'logging.handlers.SMTPHandler',
      'level': 'CRITICAL',
      'formatter': 'mail',
      'mailhost': ('smtp.126.com', 25),
      'credentials': ('sender mail', 'password'),
      'fromaddr': 'sender mail',
      'toaddrs': ['your_mail'],
      'subject': 'easy_log_test',
    }}
from easy_log.easy_log import EasyLog

# log = EasyLog(mail)
log = EasyLog()
log.logger.info('info message')
log.logger.debug('debug message')
log.logger.error('error message')
log.logger.critical('critical message :(')
