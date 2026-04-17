def even_nums(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num
            
start = int(input())
end = int(input())

print(start, end)
print(list(even_nums(start, end)))