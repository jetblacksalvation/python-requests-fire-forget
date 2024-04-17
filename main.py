import asyncio
from PokeAPI.PokemonLoader import *
isDone = False
def onDone(p):
    global isDone
    isDone = True
    print("DOne")


asyncio.run(LoadPokeMon().Run(onDone))
