# encoding=utf-8
mail = {
 'mailhost' : ('smtp.mxhichina.com', 25),
 'credentials': ('it@test.cn', 'password'),
 'toaddrs': ['some_one@test.cn'],
}

from easy_log.easy_log import EasyLog

# log = EasyLog(mail)
log = EasyLog()
log.logger.info('info message')
log.logger.debug('debug message')
log.logger.error('error message')
log.logger.critical('critical message :(')
