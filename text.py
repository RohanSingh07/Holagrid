def smallestSubWithSum(arr, l, target):
    ans = l
    for i in range(0, l):
        curr_sum = arr[i]
        if (curr_sum >=target):
            return 1
        for j in range(i + 1, l):
            curr_sum += arr[j]
            if curr_sum >= target and (j - i + 1) < ans:
                ans = j - i + 1
    return ans

lis = list(map(int,input().split()))
target = int(input())
print(smallestSubWithSum(lis,len(lis),target))

