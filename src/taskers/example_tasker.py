# Standard modules
import time

# Internal modules
import logger


log = logger.get_logger(__name__)


def example_task():
    for i in range(60):
        try:
            param1 = i
            param2 = i * 2
            paramN = i ** i

            time.sleep(1)

            yield param1, param2, paramN
        except KeyboardInterrupt:
            raise
        except:
            log.exception(
                "Fatal error during example_task: ")
            continue
