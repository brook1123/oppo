data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f: 
        count += 1

        if count % 1000 == 0:
            data.append(line.strip())
            print(count)


print(data[0])

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
    print('平均', sum_len / len(data))