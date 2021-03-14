"""
invoke tasks collection
"""

from typing import List

from invoke import task
from pylint import lint


@task
def code_format(context, reformat=False):
    """
    Check the format of your code or reformat it.
    """
    if reformat:
        _run_for_folders(context, ["src"], "black {folder}/")
    else:
        _run_for_folders(context, ["src"], "black --check {folder}/")


def _run_for_folders(context, src_folders: List, command: str):
    src_folders = src_folders if src_folders else context.src_folders
    for folder in src_folders:
        context.run(command.format(folder=folder), echo=True)


@task(pre=[code_format])
def check_commit(c):
    """
    runs tasks all after another
    :param :
    :return: None
    """
    pylint_opts = ["src"]
    lint.Run(pylint_opts)
