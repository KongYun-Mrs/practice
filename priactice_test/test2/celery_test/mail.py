from flask_mail import Message, Mail


def init_mail():
    from app import app
    mail = Mail(app)
    msg = Message("Hello1", sender=("Me", "1053764099@qq.com"), recipients=["ky19940204@126.com"])
    return mail, msg
