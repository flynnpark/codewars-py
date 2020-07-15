def create_phone_number(n):
    if len(n) != 10:
        raise Exception("Invalid input")
    n = list(map(str, n))
    first = "".join(n[0:3])
    second = "".join(n[3:6])
    third = "".join(n[6:])
    return f"({first}) {second}-{third}"
