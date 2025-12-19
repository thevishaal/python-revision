"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
"""

n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

max1 = max(arr)

for i in arr:
    if i != max1:
        print(i)
        break
    
