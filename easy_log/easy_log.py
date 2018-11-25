# encoding=utf-8
import os
import logging.config

class EasyLog(object):
    """
    日志记录
    """
    def __init__(self, mail_conf=None):
        self._work_path = os.getcwd()
        self._data_path = '%s/data' % self._work_path
        self._log_path = '%s/log' % self._data_path
        self._logger_name = 'log_note'
        self.logger = logging.getLogger(self._logger_name)
        self.logfile = self.load_file(self._work_path + '/config/logconfig.txt')
        if not os.path.isdir(self._data_path):
            self.make_data_dir()
        logConfig = eval(self.logfile)
        if mail_conf:
            logConfig = self.email_conf(logConfig, mail_conf)
        logging.config.dictConfig(logConfig)

    def make_data_dir(self):
        os.makedirs(self._data_path)

    @staticmethod
    def load_file(filename):
        with open(filename, 'r') as f:
            return f.read()

    @staticmethod
    def email_conf(logConfig, email_conf):
        logConfig['handlers'].update(email_conf)
        logConfig['loggers']['log_note']['handlers'].append('mail')
        return logConfig


