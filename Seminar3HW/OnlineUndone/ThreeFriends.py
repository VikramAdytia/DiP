

friends = input().split()
data = {}


for friend in friends:
    data.setdefault(friend, tuple(input().split()))


def uniq_things(doc: dict) -> str:
    lst = []
    for tup in doc.values():
        for k in tup:
            lst.append(k)
    return set(lst)


def except_things(d: dict, name: str):
    for key, value in d.items():
        friends_things = []
        if key != name:
            print(f'{key} взял с собой {value}')
        for rev_key, rev_value in reversed(d.items()):
            if rev_key != key:
                friends_things.extend(rev_value)
        if key != name:
            for element in value:
                if element not in friends_things:
                    print(f' вещь {element}, есть только у одного {key}')
            for memement in set(friends_things):
                if memement not in value:
                    print(f'  у {key} данная {memement} отсутствует ')


print(f'Какие вещи взяли все три друга: {uniq_things(data)}')
except_things(data, 'name')
