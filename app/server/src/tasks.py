from celery import Celery

app = Celery(
    "tasks", broker="amqp://guest@rabbitmq:5672//", backend="rpc://"
)


@app.task
def add(a, b):
    return a + b
