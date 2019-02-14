# encoding=utf-8
import os
import logging.config
from common.log_conf import log_str


class EasyLog(object):
    """
    易用日志
    """
    def __init__(self, mail_conf=None):
        self._work_path = os.getcwd()
        self._data_path = '%s/log_data' % self._work_path
        self._log_path = '%s/log' % self._data_path
        self._logger_name = 'log_note'
        self.logger = logging.getLogger(self._logger_name)
        self.logfile = log_str
        if not os.path.isdir(self._data_path):
            self._make_data_dir()
        log_config = eval(self.logfile)
        if isinstance(mail_conf, dict) and mail_conf:
            self.__check_email_conf(email_conf=mail_conf)
            log_config = self.__email_conf(log_config, mail_conf)
        logging.config.dictConfig(log_config)

    def _make_data_dir(self):
        """
        创建目录
        """
        os.makedirs(self._data_path)

    @staticmethod
    def  __email_conf(log_config, email_conf):
        """
        邮件通知配置加载
        """
        email_conf.update({'fromaddr':email_conf['credentials'][0]})
        log_config['handlers']['mail'].update(email_conf)
        log_config['loggers']['log_note']['handlers'].append('mail')
        return log_config

    @staticmethod
    def __check_email_conf(email_conf):
        """
        传入参数简单检查
        """
        if not isinstance(email_conf, dict):
            raise TypeError('email conf type error must dict.')
        if not isinstance(email_conf['mailhost'][0], str):
            raise TypeError('email host address error.')
        if not isinstance(email_conf['mailhost'][1], int):
            raise TypeError('email host port error.')
        if not isinstance(email_conf['credentials'][0],str):
            raise TypeError('sender email error')
        if not isinstance(email_conf['credentials'][1], str):
            raise TypeError('sender password error')
        if not isinstance(email_conf['toaddrs'],list) or len(email_conf['toaddrs']) ==0:
            raise TypeError('toaddrs email error.')
