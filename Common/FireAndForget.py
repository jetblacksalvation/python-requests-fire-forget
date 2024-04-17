from Common.Common import *
import requests

class IHTTPMeta(type(IHTTPClass)):
    """ When nesting abc classes, you must create a metaclass (apparently)"""
    pass

class IFireAndForgetHTTP(metaclass=IHTTPMeta):
    def __init__(self) -> None:
        #self.config_path must be defined 
        try: 
            super().__init__(self.config_path)
        except Exception as E :
            raise Exception(f"ERR in {traceback.extract_stack()}  Except was: {E}")
            pass
    
