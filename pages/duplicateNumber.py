nums = [1, 3, 5, 7, 8, 4, 3, 21, 1]
seen = set()


def duplicate():
    for x in nums:
        if x in seen:
            return True
        else:
            seen.add(x)
    return False


print(duplicate())
print(seen)
