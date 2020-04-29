in_file = open("input.txt", "r", encoding="utf8")
a = []
print(len(set(in_file.read().split())))
