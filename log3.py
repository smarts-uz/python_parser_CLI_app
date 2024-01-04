import logging
import os
from parsing.functions import logger_path

class Logger():
    def __init__(self,module_name,fm):
        self.logger = logging.getLogger(module_name)
        formater = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
        self.logger.info(f"Running module {module_name}...")
        handler2 = logging.FileHandler(f"{logger_path()}/{module_name}.log", mode=fm, encoding='utf-8')
        handler2.setFormatter(formater)
        self.logger.addHandler(handler2)

    def log(self,message):
        self.logger.setLevel(logging.DEBUG)
        self.logger.info(message)

    def err(self, err):
        self.logger.setLevel(logging.ERROR)
        self.logger.exception(err)


