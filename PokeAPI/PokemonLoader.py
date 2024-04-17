import asyncio
from pandas import DataFrame
from Common.Common import *
from Common.Common import CommonConfigLoader

class LoadPokeMon(IHTTPClass):
    def __init__(self, config: CommonConfigLoader | str = None) -> None:
        super().__init__()

    async def Run(self, on_done_func):
        task = asyncio.ensure_future(self._run())
        await task
        return on_done_func(task)

    async def _run(self):
        print("Done")
        # Load Pokemon data
        pokemon_data = await self.LoadPokeMon()
        # Write Pokemon data to a file
        await self.WriteToFile(pokemon_data)
    @classmethod
    async def UsingDf(cls, name: str) -> 'LoadPokeMon':
        # Perform asynchronous tasks here
        await asyncio.sleep(1)  # Example asynchronous operation
        return cls

    @classmethod
    async def LoadPokeMon(cls) -> 'LoadPokeMon':
        # Perform asynchronous tasks here
        await asyncio.sleep(1)  # Example asynchronous operation
        # Dummy Pokemon data
        pokemon_data = {"name": "Pikachu", "type": "Electric"}
        return pokemon_data

    async def WriteToFile(self, data):
        # Perform asynchronous tasks here
        await asyncio.sleep(1)  # Example asynchronous operation
        with open('pokemon_data.txt', 'w') as f:
            f.write(str(data))

    async def LogDfDelta(self, df1: DataFrame, df2: DataFrame) -> 'LoadPokeMon':
        # Perform asynchronous tasks here
        await asyncio.sleep(1)  # Example asynchronous operation
        return await super().LogDfDelta(df1, df2)

    async def LogStart(self) -> 'LoadPokeMon':
        # Perform asynchronous tasks here
        await asyncio.sleep(1)  # Example asynchronous operation
        return await super().LogStart()

