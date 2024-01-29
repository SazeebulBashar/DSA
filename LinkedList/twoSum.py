# def largestOddNumber(num):
#         if(len(num) == 0):
#             return ""
#         if(int(num)%2!=0):
#             return num
        
#         return largestOddNumber(num[:-1])

# print(largestOddNumber("88188"))

def largestOddNumber(num):
        if(len(num) == 0):
            return ""
        if(len(num)==1 and int(num[0])%2==0):
             return ""
        if(int(num)%2!=0):
            return num
        cur = len(num)-1
        for i in range(len(num)-1,-1,-1):
            if(len(num) == 0):
                return ""
            if(int(num[cur]) % 2 == 0):
                cur -= 1
                continue
            return num[:cur+1]
        return ""
        
print(largestOddNumber("4062"))