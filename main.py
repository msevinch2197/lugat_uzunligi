def get_length(d):
    if not d:
        return "Lug‘at bo‘sh"
    return len(d)

# test
data = {'a': 1, 'b': 2, 'c': 3}
print(get_length(data))
