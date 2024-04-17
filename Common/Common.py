
from Common.CommonLogger import *

from typing_extensions import  Self


#defining an exception handler for asyncio... 

class CommonConfigLoader:
    def __init__(self, path:str, fire_forget_type:typing.Any) -> None:
        self.path = path 
        self.fire_forget_type = type(fire_forget_type)
        #extend self with this ...
        pass


class IHTTPClass(ABC):
    """
        ICommonHTTPClass/children take the builder approach,
        other classes may implement some Commonly used builder funcs
        
    """
    
    def __init__(self, config:CommonConfigLoader|str = None) -> None:
        if(config is CommonConfigLoader ):
            pass
        elif(config is str):
            pass
        self.token = ""
    @abstractmethod
    def Run(self, on_done_func):
        task = asyncio.ensure_future(self._run)

        finished = asyncio.get_event_loop().create_future()

        task.add_done_callback(on_done_func)
        finished.result()

        # Run the main function asynchronously
        

        pass
    @abstractmethod
    def _run(self) -> None:
        return
    @abstractmethod
    def LogDfDelta(self, df1:pandas.DataFrame, df2:pandas.DataFrame)->Self:
        pass
    @abstractmethod
    def LogStart(self)->Self:
        pass
