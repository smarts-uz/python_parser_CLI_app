import logging
import os
from parsing.functions import logger_path

class Logger():
    def __init__(self,module_name,fm):
        self.logger = logging.getLogger(module_name)
        self.logger.setLevel(logging.INFO)
        formater = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
        self.logger.info(f"Running module {module_name}...")
        handler2 = logging.FileHandler(f"{logger_path()}/{module_name}.log", mode=fm)
        handler2.setFormatter(formater)
        self.logger.addHandler(handler2)

    def log(self,message):
        self.logger.info(message)

    def err(self,message):
        self.logger.error(message)


