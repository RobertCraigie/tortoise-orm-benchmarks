import asyncio
import os
import time

from prisma.models import Journal


LEVEL_CHOICE = [10, 20, 30, 40, 50]
concurrents = int(os.environ.get("CONCURRENTS", "10"))


async def _runtest(inrange: int) -> int:
    count = 0

    for _ in range(inrange):
        for level in LEVEL_CHOICE:
            res = await Journal.prisma().find_many(
                where={
                    "level": level,
                },
            )
            count += len(res)

    return count


async def runtest(loopstr: str) -> None:
    inrange = 10 // concurrents
    if inrange < 1:
        inrange = 1

    start = now = time.time()

    count = sum(await asyncio.gather(*[_runtest(inrange) for _ in range(concurrents)]))

    now = time.time()

    print(f"Prisma ORM{loopstr}, D: Rows/sec: {count / (now - start): 10.2f}")
