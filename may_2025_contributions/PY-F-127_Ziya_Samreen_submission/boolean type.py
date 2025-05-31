items = [0, '', 42]

for item in items:
    print(f"{repr(item)} is", "truthy" if bool(item) else "falsy")