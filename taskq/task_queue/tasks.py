"""Celery app initialization and tasks."""
import time
from functools import wraps

from celery import Celery

celery_app = Celery('tasks')

celery_app.conf.update(
    enable_utc=True,
    timezone='Europe/Moscow',
    broker_url='pyamqp://rabbitmq',
    result_backend='rpc://',
)


def timeit(func):
    """Measure execution time."""
    @wraps(func)
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        return {
            'Execution time': f'{func.__name__} executed for {t2 - t1}',
            'result': result,
        }
    return wrapper


@celery_app.task(name='heavy_task')
@timeit
def heavy_task(period) -> True:
    """Imitate a heave task."""
    time.sleep(int(period))
    return True


if __name__ == '__main__':
    args = ['worker', '-P', 'threads', '--loglevel=INFO']
    celery_app.worker_main(argv=args)
