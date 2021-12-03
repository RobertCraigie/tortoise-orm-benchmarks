import asyncio
import os
import time
from random import randint

from prisma.models import Journal

concurrents = int(os.environ.get("CONCURRENTS", "10"))
count = int(os.environ.get("ITERATIONS", "1000"))
maxval = count - 1
count *= 2


async def _runtest(count: int) -> None:
    for _ in range(count):
        await Journal.prisma().find_unique(
            where={
                "id": randint(1, maxval),
            },
        )


async def runtest(loopstr: str) -> None:
    start = now = time.time()

    await asyncio.gather(*[_runtest(count // concurrents) for _ in range(concurrents)])

    now = time.time()

    print(f"Prisma ORM{loopstr}, F: Rows/sec: {count / (now - start): 10.2f}")
