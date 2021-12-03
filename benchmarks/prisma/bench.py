#!/usr/bin/env python
import os
import sys

try:
    concurrents = int(os.environ.get("CONCURRENTS", "10"))

    if concurrents != 10:
        loopstr = f" C{concurrents}"
    else:
        loopstr = ""
    if os.environ.get("UVLOOP", ""):
        import asyncio

        import uvloop

        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
finally:
    pass

if concurrents > 1 and sys.version_info < (3, 7):
    sys.exit()


import test_a
import test_b
import test_d
import test_e
import test_f
import test_g
import test_i
import test_j
import test_k
from prisma import Client, register
from prisma.utils import async_run


async def init():
    client = Client()
    register(client)
    await client.connect()


async def run_benchmarks():
    await init()
    await test_a.runtest(loopstr)
    await test_b.runtest(loopstr)
    await test_d.runtest(loopstr)
    await test_e.runtest(loopstr)
    await test_f.runtest(loopstr)
    await test_g.runtest(loopstr)
    await test_i.runtest(loopstr)
    await test_j.runtest(loopstr)
    await test_k.runtest(loopstr)


async_run(run_benchmarks())
