import pytest
import os
import sys
from pathlib import Path

from gridsync.tahoe import Tahoe

# @pytest.mark.skip(reason="Doesn't work")
def test_fixtures(tahoe_server):
    test_server = tahoe_server
    assert True