

def add(i: int):
    i = i + 1
    print(f' here is i value {i}')
    prim = 7
    if True:
        x = -1
        prim = 4
        print(prim)
    print(prim)
    print(x)


def add_c(i):
    i['a'] = i['a'] + 1
    print(i)


if __name__ == '__main__':
    prim = 1
    add(prim)
    print(prim)

    comp = {'a': 1}
    print(comp)
    add_c(comp)
    print(comp)
