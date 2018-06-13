import logging
import copy
import datetime
import signal

from det.exceptions import DETException
from det.utils import State
from det.utils.timeout import timeout


logger = logging.getLogger(__name__)


class TaskInstance(object):

        def __init__(self,
                     task,
                     execution_date=datetime.datetime.now(),
                     state=None,
                     *args,
                     **kwargs):
                env_nbr = kwargs.get('env_nbr', None)
                params = kwargs.get('params', None)
                self.context = {'params': params}
                self.task = task

        def run(self):
                task = self.task
                self.operator = task.__class__.__name__

                task_copy = copy.copy(task)
                self.task = task_copy

                def signal_handler(signum, frame):
                        '''Setting kill signal handler'''
                        logging.error("Killing subprocess")
                        task_copy.on_kill()
                        raise DETException('Task received SIGTERM signal')
                signal.signal(signal.SIGTERM, signal_handler)

                if task_copy.execution_timeout:
                        with timeout(int(task_copy.execution_timeout.total_seconds())):
                                result = task_copy.execute(context=self.context)
                else:
                        result = task_copy.execute(context=self.context)
                self.state = State.SUCCESS
                return(result)


class BaseOperator(object):
        """
        Abstract base class for all operators.

        """
        def __init__(self,
                     start_date=None,
                     end_date=None,
                     execution_timeout=None,
                     *args,
                     **kwargs):
                self.start_date = start_date
                self.end_date = end_date
                self.execution_timeout = execution_timeout

        def execute(self, context):
                """
                This is the main method to derive when creating an operator.
                """
                raise NotImplementedError()

        def on_kill(self):
                """
                Override this method to cleanup subprocesses when a task instance
                gets killed. Any use of the threading, subprocess or multiprocessing
                module within an operator needs to be cleaned up or it will leave
                ghost processes behind.
                """
                pass
