from subprocess import CompletedProcess

import subprocess

from co.deability.lirs.config import LOG


def run(script: str) -> str:
    """
    Runs the supplied R script.

    :param script: The script to be run.
    :return: The output of RScript's execution of the supplied script.
    """
    if not validate(script):
        raise ValueError("You bad scripter you!")
    completed_process: CompletedProcess = subprocess.run(["Rscript", "-e", script], capture_output=True)
    LOG.debug(vars(completed_process))
    if completed_process.returncode != 0:
        raise RuntimeError("You bad Rscript runner you!")
    return completed_process.stdout.decode("utf-8")

def validate(script: str) -> bool:
    completed_process: CompletedProcess = subprocess.run(
        ["Rscript", "-e", f"'parse(text = {script})'"], capture_output=True)
    LOG.debug(vars(completed_process))
    return completed_process.returncode == 0
