# LIRS - a Less Irritating R Server

The purpose of LIRS is to provide a reliable and performant HTTP API for accessing the powerful data analytics and machine learning capabilities of R.


## Requirements

LIRS requires Python 13+.

## Environment
LIRS supports the following environment variables.

### Logging (required)
Note the supported values for both are CRITICAL, FATAL, ERROR, WARN, INFO, or DEBUG:

  - LIRS_LOG_LEVEL _Specifies the logging level for LIRS_
  - ROOT_LOG_LEVEL _Specifies the logging level for dependencies used by LIRS_

## Setup
Create a virtual environment for LIRS:

    python -m venv .venv
    source .venv/bin/activate

## Execution

    python src/co/deability/lirs/api/app.py

## Testing

    curl -X POST -d "x=1; print(x)" 127.0.0.1/lirs/analytics/run/rscript
