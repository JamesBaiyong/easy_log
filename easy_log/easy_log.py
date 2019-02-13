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
        log_config['handlers'].update(email_conf)
        log_config['loggers']['log_note']['handlers'].append('mail')
        return log_config
