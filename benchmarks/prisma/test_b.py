import asyncio
import os
import time
from random import choice

from prisma import Client, get_client


LEVEL_CHOICE = [10, 20, 30, 40, 50]
concurrents = int(os.environ.get("CONCURRENTS", "10"))
count = int(os.environ.get("ITERATIONS", "1000"))
count = int(count // concurrents) * concurrents


async def _runtest(count: int, client: Client) -> None:
    async with client.batch_() as batcher:
        for i in range(count):
            batcher.journal.create(
                data={
                    "level": choice(LEVEL_CHOICE),
                    "text": f"Insert from B, item {i}",
                },
            )


async def runtest(loopstr: str) -> None:
    start = now = time.time()
    client = get_client()

    await asyncio.gather(
        *[_runtest(count // concurrents, client) for _ in range(concurrents)]
    )

    now = time.time()

    print(f"Prisma ORM{loopstr}, B: Rows/sec: {count / (now - start): 10.2f}")
