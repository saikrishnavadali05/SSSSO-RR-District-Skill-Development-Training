# 6. Boolean Type
values = [0, '', 42] 
for val in values:
    print(f"{val} is", "Truthy" if val else "Falsy")
# output:
# 0 is Falsy
# '' is Falsy
# 42 is Truthy
