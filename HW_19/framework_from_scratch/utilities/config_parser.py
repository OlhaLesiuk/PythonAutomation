import configparser
from HW_18.framework_from_scratch.CONSTANTS import ROOT_DIR

config = configparser.RawConfigParser()
config.read(f'{ROOT_DIR}/configuration/configuration.ini')


class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_driver_id():
        return config.get('browser', 'browser_id')
