import os

from celery import Celery

app = Celery(
    'worker',
    broker=os.getenv("BROKER_CONN_STR"),
    backend=os.getenv("BACKEND_CONN_STR"),
    include=['worker.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
