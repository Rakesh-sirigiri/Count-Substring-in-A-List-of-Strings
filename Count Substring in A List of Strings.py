x = ["hello", "world", "hi", "hello world"]
count = sum(1 for y in x if "hello" in y)
print(count)
