def reverse_dict(d):
    return {v: k for k, v in d.items()}
sample = {"a": 1, "b": 2, "c": 3}
print(reverse_dict(sample))
