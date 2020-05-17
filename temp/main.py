import logging, random

class MyFilter:
    def filter(self, logRecord):
        return logRecord.levelno == logging.INFO

logger = logging.Logger('MainLogger', logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

file_handler = logging.FileHandler('info.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
file_handler.addFilter(MyFilter())
logger.addHandler(file_handler)

logger.debug("Проверка того, что сообщения уровня DEBUG обрабатываются и логером и обработчиком")  
logger.info("Тестовое сообщение уровня INFO")  
logger.error("Ещё одно сообщение, но уже уровня ERROR")

levels = ['debug', 'info', 'warning', 'error', 'critical']

def log():
    for _ in range(10):  
        level = random.choice(levels)  
        eval('logger.{level}("тестовое сообщение уровня {level}")'.format(level=level))