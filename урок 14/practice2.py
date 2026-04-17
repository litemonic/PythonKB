'''
nums = (10,20,30,20,40)
try:
    if 20 in nums:
        print("True")
    else:
        print("False")
    print(nums.count(20))
    print(nums[1:4])
    nums[2] = 100
except TypeError as e:
    print(f"Ошибка {e}")
'''
'''
p1 = (3,5)
p2 = (1,2)
p3 = (4,0)
if p1[0] < p2[0] and p1[0] < p3[0]:
    print(f"Левее всех точка {p1}")
elif p2[0] < p1[0] and p2[0] < p3[0]:
    print(f"Левее всех точка {p2}")
elif p3[0] < p1[0] and p3[0] < p2[0]:
    print(f"Левее всех точка {p3}")
'''
p1 = (3,5)
p2 = (1,2)
p3 = (4,0)
pLeft = p1
    
if p2[0] > p1[0]:
    pLeft = p2
if p3[0] > p1[0]:
    pLeft = p3

print(f"Самая левая точка: {pLeft}")