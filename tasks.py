import pathlib
from typing import List

import pylint
from invoke import task
from pylint.lint import Run


def get_folder_path(file_path):
    return pathlib.Path(file_path).parent.absolute()


@task
def code_format(context, reformat=False):
    """
    Check the format of your code or reformat it.
    """
    if reformat:
        _run_for_folders(context, ["src"], "black {folder}/")
    else:
        _run_for_folders(context, ["src"], "black --check {folder}/")


def _run_for_folders(context, src_folders, command: str):
    src_folders = src_folders if src_folders else context.src_folders
    for folder in src_folders:
        context.run(command.format(folder=folder), echo=True)


@task(pre=[code_format])
def check_commit(c):
    pylint_opts = ["src"]
    pylint.lint.Run(pylint_opts)
