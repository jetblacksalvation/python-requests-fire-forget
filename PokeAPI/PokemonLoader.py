from pandas import DataFrame
from Common.Common import *

class LoadPokeMon(IHTTPClass):
    async def Run(self):
        print("Done")

    @classmethod
    async def UsingDf(cls, name: str) -> 'LoadPokeMon':
        # Perform asynchronous tasks here
        await asyncio.sleep(1)  # Example asynchronous operation
        return cls()

    @classmethod
    async def LoadPokeMon(cls) -> 'LoadPokeMon':
        # Perform asynchronous tasks here
        await asyncio.sleep(1)  # Example asynchronous operation
        return cls()

    async def LogDfDelta(self, df1: DataFrame, df2: DataFrame) -> 'LoadPokeMon':
        # Perform asynchronous tasks here
        await asyncio.sleep(1)  # Example asynchronous operation
        return await super().LogDfDelta(df1, df2)

    async def LogStart(self) -> 'LoadPokeMon':
        # Perform asynchronous tasks here
        await asyncio.sleep(1)  # Example asynchronous operation
        return await super().LogStart()