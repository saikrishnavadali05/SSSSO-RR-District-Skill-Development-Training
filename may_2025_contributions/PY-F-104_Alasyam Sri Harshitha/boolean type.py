items = [0, '', 42]
for item in items:
    if item:
        print(item, "is truthy")
    else:
        print(item, "is falsy")
