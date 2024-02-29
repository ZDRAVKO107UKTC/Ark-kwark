def missing(*args):
    missing_students = len(args)
    return missing_students

print(missing(1, 4, 5))
print(missing(4, 5, 6, 1, 3))
print(missing(2, 20, 10, 15, 28, 3, 1))