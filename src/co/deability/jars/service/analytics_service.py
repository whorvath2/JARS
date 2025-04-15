from subprocess import CompletedProcess
import subprocess
import shlex

from co.deability.jars.config import LOG
from co.deability.jars.error.r_script_error import RScriptError


def run(script: str) -> str:
    """
    Runs the supplied R script.

    :param script: The script to be run.
    :return: The output of RScript's execution of the supplied script.
    """
    if not validate(script):
        raise RScriptError(bad_script=script)
    completed_process: CompletedProcess = subprocess.run(
        ["Rscript", "-e", script], capture_output=True
    )
    LOG.debug(vars(completed_process))
    if completed_process.returncode != 0:
        raise RScriptError(bad_script=script)
    return completed_process.stdout.decode("utf-8")


def validate(script: str) -> bool:
    """
    Returns `True` if the supplied R script can be executed by Rscript, `False` otherwise.

    :param script: The script to be validated.
    :return: `True` if the supplied R script can be executed by Rscript, `False` otherwise.
    """
    r_command = shlex.quote(script)
    completed_process: CompletedProcess = subprocess.run(
        ["Rscript", "-e", r_command],
        capture_output=True,
        shell=False,
    )
    return_code = completed_process.returncode
    LOG.debug(
        f"Return code: {return_code}\n"
        f"StdOut: {completed_process.stdout}\n"
        f"StdErr: {completed_process.stderr}\n"
    )
    return return_code == 0
