def double_digits_from_randnum(number: int) -> str:
    if number < 10:
        return f"0{str(number)}"
    else:
        return str(number)
