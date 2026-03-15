# Testing

The template configures a full testing setup with pytest, coverage reporting, and optional multi-version testing.

## pytest

[pytest](https://github.com/pytest-dev/pytest) is the default test runner. Tests live in the `tests/` directory.

/// tab | make

```bash
make test
```

///

/// tab | mise

```bash
mise run test
```

///

## Coverage

[Coverage.py](https://github.com/nedbat/coveragepy) generates test coverage reports in text, HTML, and XML formats.

/// tab | make

```bash
make coverage
```

///

/// tab | mise

```bash
mise run coverage
```

///

The coverage threshold is configurable via the `coverage_threshold` template variable (default: 100%).

## Tox

[Tox](https://github.com/tox-dev/tox) with [tox-uv](https://github.com/tox-dev/tox-uv) runs your test suite across multiple Python versions.

/// tab | make

```bash
make tox
```

///

/// tab | mise

```bash
mise run tox
```

///

Tox is included by default but can be disabled by setting `tox: false` during project generation.

## pytest-xdist

For parallel test execution, enable the `pytest_xdist` option during generation. This adds [pytest-xdist](https://github.com/pytest-dev/pytest-xdist) to your test dependencies.

/// tab | make

```bash
# Tests automatically run in parallel when pytest-xdist is installed
make test
```

///

/// tab | mise

```bash
# Tests automatically run in parallel when pytest-xdist is installed
mise run test
```

///
