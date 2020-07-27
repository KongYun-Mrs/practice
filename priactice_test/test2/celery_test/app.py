from flask import Flask
from Celery_broker import init_celery
from mail import init_mail

app = Flask(__name__)
app.config.from_pyfile('settings.py')
celery = init_celery()



@celery.task()
def send_mail():
    mail, msg = init_mail()
    msg = 'HELLO1'
    mail.send(msg)


@app.route('/')
def hello_world():
    send_mail.apply_async()
    return 'send_mail SUCCESS!'


if __name__ == '__main__':
    app.run()
