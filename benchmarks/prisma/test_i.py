import asyncio
import os
import time
from random import choice
from typing import List

from prisma.models import Journal


LEVEL_CHOICE = [10, 20, 30, 40, 50]
concurrents = int(os.environ.get("CONCURRENTS", "10"))


async def _runtest(objs: List[Journal]) -> int:
    # TODO: in transaction
    for obj in objs:
        await Journal.prisma().update(
            where={
                "id": obj.id,
            },
            data={
                "level": choice(LEVEL_CHOICE),
                "text": f"{obj.text} Update",
            },
        )

    return len(objs)


async def runtest(loopstr: str) -> None:
    objs = await Journal.prisma().find_many()
    inrange = len(objs) // concurrents
    if inrange < 1:
        inrange = 1

    start = now = time.time()

    count = sum(
        await asyncio.gather(
            *[
                _runtest(objs[i * inrange : ((i + 1) * inrange) - 1])
                for i in range(concurrents)
            ]
        )
    )

    now = time.time()

    print(f"Prisma ORM{loopstr}, I: Rows/sec: {count / (now - start): 10.2f}")
