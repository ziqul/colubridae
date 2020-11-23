# Standard modules
import os

# External modules
from dotenv import load_dotenv
from waitress import serve

# Internal modules
from server.handlers import healthz
from server.handlers import metrics
from server.handlers import not_allowed
from server.handlers import not_found
from server.handlers import tasks
import logger
import server.app
import worker.tasks
import worker.util


log = logger.get_logger(__name__)


def main():
    log.info("Loading .env...")
    load_dotenv()

    log.info("Creating application ...")
    app = server.app.create_app(
        {
            "/_healthz": healthz.handler,
            "/_metrics": metrics.handler,
            "/example_tasks":
                tasks.create_handler(
                    worker.tasks.example_task,
                    worker.util,
                ),
        },
        {
            404: not_found.handler,
            405: not_allowed.handler,
        }
    )

    log.info("Starting server ...")
    if os.getenv("ENV") == "dev":
        app.run(
            debug=True,
            host='0.0.0.0',
            port=int(os.getenv("PORT")),
        )
    else:
        serve(
            app, host="0.0.0.0",
            port=int(os.getenv("PORT")),
            _quiet=True,
        )


if __name__ == "__main__":
    main()
