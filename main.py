import asyncio
from Common.FireAndForget import *
from PokeAPI.PokemonLoader import *

async def main():
    # Dispatch the Run method asynchronously
    await asyncio.create_task(LoadPokeMon().Run())

# Run the main function asynchronously
asyncio.run(main())
