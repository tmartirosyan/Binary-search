ls = list(range(1, 10001))
# 9
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
search_num = 4

left = 0
right = len(ls) - 1
midpoint = (right + left) // 2
count = 1
while left <= right:
    if search_num == ls[midpoint]:
        break
    else:
        if search_num < ls[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    midpoint = (left + right) // 2
    count += 1
print(count)
