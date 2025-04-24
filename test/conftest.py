# import ipdb
import pytest

from pytest_twisted import async_yield_fixture

from gridsync.tahoe import Tahoe



PORT = 3456

@async_yield_fixture(scope="module")
async def tahoe_server(tmp_path_factory):
    server = Tahoe(tmp_path_factory.mktemp("tahoe_server") / "nodedir")
    settings = {
        "port": f"tcp:{PORT}:interface=127.0.0.1",
        "location": f"tcp:127.0.0.1:{PORT}",
    }
    await server.create_node(settings)
    server.config_set("storage", "reserved_space", "10M")
    await server.start()
    yield server
    await server.stop()