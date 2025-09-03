values = [0, '', 42]
for val in values:
    print(f"{val!r} is", "truthy" if val else "falsy")