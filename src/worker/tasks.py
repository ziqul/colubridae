from worker.celery import app
from taskers import example_tasker
import time


@app.task
def example_task():
    for (param1, param2, paramN) in \
        example_tasker.example_task() \
    :
        example_task.update_state(
            meta={
                'param1': param1,
                'param2': param2,
                'paramN': paramN,
            }
        )
