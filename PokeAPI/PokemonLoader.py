from pandas import DataFrame
from Common.Common import *


class LoadPokeMon(IHTTPClass):
    def Run(self):
        print("I ran")
        pass
    async def LogDfDelta(self, df1: DataFrame, df2: DataFrame) -> Self:
        return super().LogDfDelta(df1, df2)
    async def LogStart(self) -> Self:
        return super().LogStart()
    pass