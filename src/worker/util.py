from worker.celery import app

def task_info_by_id(task_id):
    task = app.AsyncResult(task_id)
    return task.info

def list_active_tasks():
    ids = []
    inspection = app.control.inspect()
    workers = inspection.active()
    for worker in workers:
        tasks = workers[worker]
        for task in tasks:
            ids.append(task["id"])
    return ids
