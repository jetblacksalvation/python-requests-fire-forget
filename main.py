import asyncio
from PokeAPI.PokemonLoader import *

async def main():
    # Create an instance of LoadPokeMon
    pokemon_loader = LoadPokeMon()
    # Dispatch the Run method asynchronously and don't wait for it to complete
    asyncio.create_task(pokemon_loader.Run())

# Run the main function asynchronously
asyncio.run(main())
