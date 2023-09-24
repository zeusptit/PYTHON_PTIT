def is_valid_number(s):
    return s.isdigit() and int(s) <= 2**32

with open("DATA.in", "r") as file_obj:
    data = file_obj.read().split()

res = [i for i in data if not is_valid_number(i)]
res.sort()

print(*res)
