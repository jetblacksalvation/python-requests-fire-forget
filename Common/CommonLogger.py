import asyncio
import traceback
import threading
import sys
import pandas
import typing
from typing_extensions import  Self

from abc import ABC, abstractmethod, ABCMeta

class ILogger(ABC):
    #logger 
    @abstractmethod
    def _AsyncExceptHook(exc_type,exc_value,traceback)->None:
        pass
    @abstractmethod
    def Info(exc_type,exc_value,traceback)->None:
        pass
    @abstractmethod
    def Success(exc_type,exc_value,traceback)->None:
        pass
    @abstractmethod
    def Error(exc_type,exc_value,traceback)->None:

        pass
    def CriticalError(exc_type,exc_value,traceback)->None:

        pass
    @staticmethod
    @abstractmethod
    def SetMainThreadExceptHook(self):
        def excepthook(exc_type, exc_value, traceback):
            exc_info = exc_type, exc_value, traceback
            if not issubclass(exc_type, (KeyboardInterrupt, SystemExit)):
                self.error('Unhandled exception', exc_info=exc_info)
            sys.__excepthook__(*exc_info)

        sys.excepthook = excepthook
        pass


_async_loop = asyncio.get_event_loop()

_async_loop.set_exception_handler = ILogger._AsyncExceptHook

dbricks_libs = [('Ipython', 'Ipython')] # (library_name, shorthand)
for (name, short) in dbricks_libs:
    try:
        lib = __import__(name)
        globals()[short] = lib
    except:
        print(sys.exc_info())


