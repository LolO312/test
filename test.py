def square(a):
    res = []
    for i in a:
        res.append(i**2)
    return res

nums = [1, 31, 11, 5]
print(square(nums))
