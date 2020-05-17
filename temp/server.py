import sentry_sdk
from bottle import Bottle, run
from sentry_sdk.integrations.bottle import BottleIntegration
import main
import logging

#Настройка Sentry
sentry_sdk.init(
    "https://1f383aa181004648a40af745978fabea@o393938.ingest.sentry.io/5243519",
    integrations=[BottleIntegration()]
    )

#СОздам нового обработчика
server_logger = logging.getLogger(__name__)
server_logger.setLevel(logging.INFO)

server_log_handler = logging.FileHandler('access.log', encoding='UTF-8')
server_log_handler.setLevel(logging.INFO)
server_log_handler.setFormatter(main.formatter)
server_log_handler.addFilter(main.MyFilter())

server_logger.addHandler(server_log_handler)


app = Bottle()

@app.route('/index')
def greeting():
    server_logger.info("Роут на /")
    return("<h2>Hello World!</h2?")

@app.route('/log')
def logger():
    raise RuntimeError("There is an error!")  
    server_logger.info("Роут на /log")
    return 

if __name__ == '__main__':
    app.run()