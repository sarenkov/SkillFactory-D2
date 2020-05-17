import sentry_sdk
from bottle import Bottle, run, error, response
from sentry_sdk.integrations.bottle import BottleIntegration
import os

# Настройка Sentry
sentry_sdk.init(
    "https://1f383aa181004648a40af745978fabea@o393938.ingest.sentry.io/5243519",
    integrations=[BottleIntegration()]
)


app = Bottle()


def get_response_text(status):
    return f'<h1>Текущий статус: {status}. Можно проверить в консоли</h1>'


@app.route('/success')
def success():
    response.status = 200
    return get_response_text(response.status)


@app.route('/fail')
def fail():
    print('hello')
    raise Exception(
        "Статус ответа 500. Сервис ходит по лезвию просто. Ошибка отправлена в Sentry")


@app.route('/notFound')
def not_found():
    response.status = 404
    return get_response_text(response.status)


@app.route('/unautorized')
def unautorized():
    response.status = 403
    return get_response_text(response.status)


if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080, debug=True)
