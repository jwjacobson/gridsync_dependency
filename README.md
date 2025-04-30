# gridsync_dependency - using Gridsync for its Tahoe object
## Update 2025-04-29
It is in fact possible to use gridsync in this way, but we will no longer be pursuing this path!

There were two major issues:
1. The [gridsync package on PyPI](https://pypi.org/project/gridsync/) is rather out of date, at version 0.4.3 instead of the latest 0.6.1. We got around this by building Gridsync directly from its Github repo instead of installing it from PyPI.
2. After updating, the blocking issue appears to have been a Python version mismatch; we were using Python 3.13, but gridsync only supports up to 3.11 (3.9 for PyPI gridsync!).

Making these two changes allowed our toy test to run successfully.

The reason we will not be pursuing this further is that Gridsync is a full desktop app and not a library, and using it for its Tahoe object involves pulling in a lot of unused and irrelevant dependencies, like QT. Instead we will focus on adapting the Tahoe module to work without the rest of Gridsync.

## Goal:
We want to install [Gridsync](https://github.com/gridsync/gridsync) as a project dependency and make use of its Tahoe object in [Private Facts](https://github.com/blaisep/private_facts), in particular for integration tests.

This repo will document and help troubleshoot issues with the process.

## Current error: why does Tahoe have no create_node method?
Line 14 of test/conftest.py successfully creates a Tahoe object called server.

Line 19 attempts to call the object's create_node() method, leading to an error:

```ERROR test/test_gridsync.py::test_fixtures - AttributeError: 'Tahoe' object has no attribute 'create_node'```

But the Tahoe object [does have such a method](https://github.com/gridsync/gridsync/blob/29edd61fa7dbd856fe757f0f11e911ebf6a44cab/gridsync/tahoe.py#L420)!

It is not defined [anywhere else](https://imgur.com/carbon-110dlO2)

## Steps to reproduce
1. Clone the repo and navigate to the gridsync_dependency directoryx
2. Run pytest: `uv run pytest` ([requires uv](https://docs.astral.sh/uv/))
3. You should see the error described above!
