# JARS - Just Another R Server

The purpose of JARS is to provide a reliable and performant HTTP API for accessing the powerful data analytics and machine learning capabilities of R.


## Requirements

JARS requires Python 13+.

## Environment
JARS supports the following environment variables.

### Logging (required)
Note the supported values for both are CRITICAL, FATAL, ERROR, WARN, INFO, or DEBUG:

  - JARS_LOG_LEVEL _Specifies the logging level for JARS_
  - ROOT_LOG_LEVEL _Specifies the logging level for dependencies used by JARS_

## Setup
Create a virtual environment for JARS:

    python -m venv .venv
    source .venv/bin/activate

## Execution

    python src/co/deability/jars/api/app.py

## Testing

    curl -X POST -d "x=1; print(x)" 127.0.0.1/jars/analytics/run/rscript
