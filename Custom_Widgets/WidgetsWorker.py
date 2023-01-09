########################################################################
## IMPORTS
########################################################################
import os
import sys
import traceback

########################################################################
## IMPORT PYSIDE2 OR PYSIDE6
########################################################################
# if 'PySide2' in sys.modules:
#     from PySide2.QtCore import QObject, Signal, QRunnable, Slot 

# elif 'PySide6' in sys.modules:
#     from PySide6.QtCore import QObject, Signal, QRunnable, Slot

########################################################################
## MODULE UPDATED TO USE QTPY
########################################################################
from qtpy.QtCore import QObject, Signal, QRunnable, Slot

########################################################################
## WORKER SIGNAL CLASS
########################################################################
class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)

########################################################################
## 
########################################################################


########################################################################
## WORKER  CLASS
########################################################################
class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except Exception as e:
            print(e)
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done
    

########################################################################
## WORKER  CLASS
########################################################################
class WorkerResponse():
    ########################################################################
    ## WORKER PRINT OUT
    ########################################################################
    def print_output(s):
        if s is not None:
            print(s)
        
    ########################################################################
    ## 
    ########################################################################

    ########################################################################
    ## WORKER THREAD COMPLETE FUNCTION
    ########################################################################
    def thread_complete():
        print("THREAD COMPLETE!")
    ########################################################################
    ## 
    ########################################################################



    ########################################################################
    ## WORKER THREAD PROGRESS FUNCTION
    ########################################################################
    def progress_fn(n):
        # n = progress value
        print("%d%% done" % n)
    ########################################################################
    ## 
    ########################################################################


########################################################################
## 
########################################################################