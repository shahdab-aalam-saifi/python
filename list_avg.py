def list_avg(lst=None):
    if lst is None:
        lst = []
    return sum(lst)/len(lst)


print("Avg of list", list_avg([x for x in range(10)]))

