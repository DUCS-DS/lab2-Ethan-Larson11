
def monotonic(lst):
    increasing = decreasing = True
    
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            decreasing = False
        elif lst[i] < lst[i - 1]:
            increasing = False
    
    return increasing or decreasing

lst = [43, 56, 56, 60]
#lst = [10, 7, 7, 2]
#lst = [100, 50, 100]
print(monotonic(lst))