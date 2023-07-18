def pack_backpack(items, max_weight):
    copyitems = items.copy()
    for i in list(items.keys()):
        possible_items = []
        curr_weight = max_weight
        up = copyitems.popitem()
        upda = {up[0]:up[1]}
        #print(upda)
        res = upda | copyitems
        copyitems = res.copy()
        #print(res)
        for item, weight in res.items():
            if weight <= curr_weight:
                possible_items.append(item)
                curr_weight -= weight
        print(possible_items)


items = {'tent': 5,
         'water': 3,
         'food': 4,
         'clothes': 2,
         'first aid kit': 1}
max_weight = 10
pack_backpack(items, max_weight)
