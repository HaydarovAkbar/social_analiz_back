import asyncio
from shazamio import Shazam


async def main():
    shazam = Shazam()
    tracks = await shazam.search_track(query="Arash", limit=5)
    print(tracks)

loop = asyncio.get_event_loop_policy().get_event_loop()
loop.run_until_complete(main())