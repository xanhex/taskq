"""Fast API app."""
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from task_queue.tasks import celery_app

app = FastAPI()


@app.get('/create/{period}')
def task_create(period: int) -> JSONResponse:
    """Endpoint for creacting a Celery task."""
    task = celery_app.send_task('heavy_task', args=(period,))
    return JSONResponse({'task_id': task.id})


@app.get('/{task_id}')
def task_status(task_id: str) -> JSONResponse:
    """Endpoint for checking the status of the Celery task."""
    task_result = celery_app.AsyncResult(task_id)
    result = {
        'task_id': task_id,
        'task_status': task_result.status,
        'task_result': task_result.result,
    }
    return JSONResponse(result)
