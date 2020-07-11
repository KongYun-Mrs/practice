from celery import Celery


def init_celery():
    try:
        from app import app
        celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
        celery.conf.update(app.config)
        return celery
    except Exception as e:
        print e
        raise e
