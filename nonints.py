def remove_nonints(nums):
    new_list = []
    for num in nums:
         if type(num) == int:
             new_list.append(num)
    return new_list  