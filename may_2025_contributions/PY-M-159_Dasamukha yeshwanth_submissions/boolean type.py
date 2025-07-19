values = [0, '', 42]
for value in values:
    if value:
        print(f"{value!r} is truth")
    else:
        print(f"{value!r} is false")

values = [0, '', 67]

for value in values:
    if value:
        print(f"{value!r} is truth")
    else:
        print(f"{value!r} is false")
