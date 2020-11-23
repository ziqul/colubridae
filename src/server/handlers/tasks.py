from flask import request


def create_handler(task, worker_util):
    def handler():
        if request.method == "POST":
            promise = task.delay()
            return f"{promise.id}", 200
        elif request.method == "GET":
            task_id = request.args.get('id')
            if task_id is not None:
                task_info = \
                    worker_util.task_info_by_id(task_id)
                if task_info is not None:
                    return f"{task_info}", 200
                else:
                    return "Not Found", 404
            else:
                ids = worker_util.list_active_tasks()
                ids_as_string = \
                    "\n".join([id for id in ids])
                return f"{ids_as_string}", 200

    handler.methods = ["POST", "GET"]

    return handler
