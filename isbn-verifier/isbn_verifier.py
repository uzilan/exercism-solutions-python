def verify(isbn):
    no_hyphens = isbn.replace('-', '')
    if len(no_hyphens) != 10 \
            or not no_hyphens[0:9].isdigit() \
            or not (no_hyphens[-1].isdigit() or no_hyphens.endswith('X')):
        return False

    nums = [int(x) for x in no_hyphens[0:-1]]
    nums.append(10 if no_hyphens.endswith('X') else int(no_hyphens[-1]))

    zipped = zip(nums, range(10, 0, -1))
    multiplied = [x * y for (x, y) in zipped]

    return sum(multiplied) % 11 == 0
