""" Сортировка выбором """
nums = list(map(int, input().split()))

index = 0 # индекс элемента

for i in range(len(nums)):
    for j in range(index, len(nums)):
        if nums[index] > nums[j]:
            nums[index], nums[j] = nums[j], nums[index]
    index += 1


print(*nums)
    

