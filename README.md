# JARS - Just Another R Server

The purpose of JARS is to provide a reliable and performant HTTP API for accessing the powerful data analytics and machine learning capabilities of R.

## Requirements

JARS requires [Python 13+](https://www.python.org). Use of the `build.sh` and `exec.sh` scripts to build and execute JARS in a container requires [podman](https://podman.io).

## Environment
JARS supports the following environment variables.

### Logging (required)
Note the supported values for both are CRITICAL, FATAL, ERROR, WARN, INFO, or DEBUG:

  - JARS_LOG_LEVEL _Specifies the logging level for JARS_
  - ROOT_LOG_LEVEL _Specifies the logging level for dependencies used by JARS_

## Containerized Build
The `build.sh` and `exec.sh` scripts are for building the (`jars-image`) container image and executing it in a podman virtual machine.

### Setup
Builds the `jars_image` from the `Dockerfile`.

    sh build.sh

### Execution
Runs `jars_image` in a container, but requires that the podman machine is running first; _i.e._, the first two steps are optional if the machine is already running.

    podman machine init    # Create a podman VM
    podman machine start   # Start the podman VM
    sh exec.sh

### Testing

    curl -X POST -d "x=1; print(x)" 127.0.0.1/jars/analytics/run/rscript

## Non-Containerized Build
The JARS server can also be built and executed outside a containerized environment.

### Setup
Create a virtual environment for JARS:

    python -m venv .venv
    source .venv/bin/activate
    pip install .

### Execution

    python src/co/deability/jars/api/app.py

### Testing

    curl -X POST -d "x=1; print(x)" 127.0.0.1:5277/jars/analytics/run/rscript

## Development
JARS uses pytest for unit testing and pre-commit for ensuring unit tests are run prior to a commit.

    pip install .[dev]
    pytest test
