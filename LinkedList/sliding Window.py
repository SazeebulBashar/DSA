lst= [i for i in range(1,11)]
def sw(lst,n):
    if(len(lst) <= n):
        return lst
    for i in range(len(lst) - n+1):
        print(lst[i:i+n])

# sw(lst,3)

A = [5, -2, 3 , 1, 2]
B=3
curr_sum = sum(A[:B])
max_sum = curr_sum

j=len(A)-1
for i in range(B-1,-1,-1):
    curr_sum = curr_sum - A[i] + A[j]
    max_sum = max(curr_sum,max_sum)
    j-=1
return max_sum
