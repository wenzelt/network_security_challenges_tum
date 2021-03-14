"""
Collection of helper functions over the project
"""

import ast
import operator as op
import sys

# supported operators
operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.BitXor: op.xor,
    ast.USub: op.neg,
}


def double_digits_from_randnum(number: int) -> str:
    """
    :param number:
    :return: returns str of number <10 with leading 0
    """
    if number < 10:
        return f"0{str(number)}"
    return str(number)


def eval_expr(expr):
    """
    >>> eval_expr('2^6')
    4
    >>> eval_expr('2**6')
    64
    >>> eval_expr('1 + 2*3**(4^5) / (6 + -7)')
    -5.0
    """
    return eval_(ast.parse(expr, mode="eval").body)


def eval_(node):
    """
    :param node:
    :return:
    """

    if isinstance(node, ast.Num):  # <number>
        return_value = node.n
    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
        nodes = eval_(node.left), eval_(node.right)
        return_value = operators[type(node.op)](nodes)
    elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
        return_value = operators[type(node.op)](eval_(node.operand))
    else:
        return_value = TypeError(node)
    return return_value


# update_progress() : Displays or updates a console progress bar
# Accepts a float between 0 and 1. Any int will be converted to a float.
# A value under 0 represents a 'halt'.
# A value at 1 or bigger represents 100%
def update_progress(progress):
    """
    :param progress:
    :return: prints to console
    """
    bar_length = 10  # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(bar_length * progress))
    text = "\rPercent: [{0}] {1}% {2}".format(
        "#" * block + "-" * (bar_length - block), progress * 100, status
    )
    sys.stdout.write(text)
    sys.stdout.flush()
