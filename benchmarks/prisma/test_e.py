import asyncio
import os
import time
from random import randrange

from prisma.models import Journal


LEVEL_CHOICE = [10, 20, 30, 40, 50]
iters = int(os.environ.get("ITERATIONS", "1000"))
concurrents = int(os.environ.get("CONCURRENTS", "10"))


async def _runtest(_iters: int) -> int:
    count = 0

    for _ in range(_iters):
        for level in LEVEL_CHOICE:
            res = await Journal.prisma().find_many(
                where={
                    "level": level,
                },
                take=20,
                skip=randrange(iters - 20),
            )
            count += len(res)

    return count


async def runtest(loopstr: str) -> None:
    start = now = time.time()
    count = 0

    count = sum(
        await asyncio.gather(
            *[_runtest(iters // 10 // concurrents) for _ in range(concurrents)]
        )
    )

    now = time.time()

    print(f"Prisma ORM{loopstr}, E: Rows/sec: {count / (now - start): 10.2f}")
