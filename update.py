'''
8) Write a program to update the given set in another set.
Sample Input:
1 2 3
3 4 5
Sample Output:
1 2 3 4 5

'''


set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

set1.update(set2)

sorted_combined = sorted(set1)

print(" ".join(map(str, sorted_combined)))
