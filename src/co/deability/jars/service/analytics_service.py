from subprocess import CompletedProcess
import subprocess
import shlex

from co.deability.jars.error.r_script_error import RScriptError


def run(script: str) -> str:
    """
    Runs the supplied R script.

    :param script: The script to be run.
    :return: The output of RScript's execution of the supplied script.
    """
    if not validate(script):
        raise RScriptError(bad_script=script)

    script = shlex.quote(script)
    r_command = rf"eval(str2expression({script}))"
    completed_process: CompletedProcess = subprocess.run(
        ["Rscript", "-e", r_command], capture_output=True, shell=False
    )
    if completed_process.returncode != 0:
        raise RScriptError(bad_script=script)
    return completed_process.stdout.decode("utf-8")


def validate(script: str) -> bool:
    """
    Returns `True` if the supplied script is valid R code that can be executed by Rscript,
    `False` otherwise.

    :param script: The script to be validated.
    :return: `True` if the supplied script can be executed by Rscript, `False` otherwise.
    """
    script = shlex.quote(script)
    r_command = f"str2expression({script});"
    completed_process: CompletedProcess = subprocess.run(
        ["Rscript", "-e", r_command],
        capture_output=True,
        shell=False,
    )
    return_code = completed_process.returncode
    return return_code == 0
