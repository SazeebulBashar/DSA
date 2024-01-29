# def twoSum(nums, target):
#     numMap = {}
#     n = len(nums)

#     for i in range(n):
#         complement = target - nums[i]
#         if complement in numMap:
#             return [numMap[complement], i]
#         numMap[nums[i]] = i
#         print(numMap)

#     return [] 

# print(twoSum([100,90,80,4,5,6,7,8,9,1],87))


strs = ["flower","flow","flight"]
com =strs[0][0]

n = len(min(strs))
for i in range(n):
    for j in range(i:len(strs)):
        if com[i] != strs[i][j]:
            print(com)
        com += strs[i][j]
        print(strs[i][j])
         
