users_id = [75, 83, 82, 14, 21, 22, 51, 12, 28]


def sort_func(variable: int):

    if variable % 2 == 0:
        return True

    return False


if __name__ == '__main__':
    filtered = filter(sort_func, users_id)
    for a in filtered:
        print(a)
