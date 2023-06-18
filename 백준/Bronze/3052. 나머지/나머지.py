num_list = []
for _ in range(10):
    data = int(input())
    num_list.append(data % 42)
print(len(set(num_list)))