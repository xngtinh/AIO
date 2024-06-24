num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
output = []

for i in range(k, len(num_list)+1):
    max_value = max(num_list[i-3:i])
    output.append(max_value)

print(output)
