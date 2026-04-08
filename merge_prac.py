def merge_sort(nums):
    if len(nums) < 2:
        return nums
    first = nums[:len(nums)//2]
    second = nums[len(nums)//2:]
    return (first,second)

def merge(first, second):
    final = []
    i = 0 
    j = 0
    while len(first[i]) <= len(second[j]):
        final.append(first[i])
        i +=1
    else:
        final.append(second[j])
        j += 1
    while i < len(first):
        final.append(first[i])
        i +=1
    while i < len(second):
        final.append(second[j])
        j +=1    
    return final    