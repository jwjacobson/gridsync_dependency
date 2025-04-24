# gridsync_dependency
## Goal:
Can we install gridsync as a project dependency and make use of its Tahoe object?

## Current error: why does Tahoe have no create_node method?
Line 14 of conftest.py successfully creates a Tahoe object called server.

Line 19 attempts to call the object's create_node() method, leading to an error:

```ERROR test/test_gridsync.py::test_fixtures - AttributeError: 'Tahoe' object has no attribute 'create_node'```

But the Tahoe object [does have such a method](https://github.com/gridsync/gridsync/blob/29edd61fa7dbd856fe757f0f11e911ebf6a44cab/gridsync/tahoe.py#L420)!

It is not defined [anywhere else](https://imgur.com/carbon-110dlO2)

## Steps to reproduce
1. Clone the repo and navigate to the gridsync_dependency directory
2. run `uv run pytest` ([requires uv](https://docs.astral.sh/uv/))
3. You should see the error described above!