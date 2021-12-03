import asyncio
import os
import time
from random import choice

from prisma.models import Journal


LEVEL_CHOICE = [10, 20, 30, 40, 50]
concurrents = int(os.environ.get("CONCURRENTS", "10"))
count = int(os.environ.get("ITERATIONS", "1000"))
count = int(count // concurrents) * concurrents


async def _runtest(count: int) -> None:
    for i in range(count):
        await Journal.prisma().create(
            data={
                "level": choice(LEVEL_CHOICE),
                "text": f"Insert from A, item {i}",
            }
        )


async def runtest(loopstr: str) -> None:
    start = now = time.time()

    await asyncio.gather(*[_runtest(count // concurrents) for _ in range(concurrents)])

    now = time.time()

    print(f"Prisma ORM{loopstr}, A: Rows/sec: {count / (now - start): 10.2f}")
