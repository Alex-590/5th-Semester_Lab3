from pprint import pprint


# def nicely_sorted[T](s: list[list[T]]) -> list[list[T]]:

#     def size_and_content(value: list[T]) -> tuple[int, list[T]]:
#         return (len(value), value)

#     return sorted(s, key=size_and_content)

# 
# Complexity: O(2 ^ N)
def power_set[T](s: list[T]) -> list[list[T]]:
    if not s:
        return [[]]
    temp: list[list[T]] = power_set(s[:-1]) # butlast of s
    return temp + [e + [s[-1]] for e in temp]


def combinations[T](s: list[T], k: int) -> list[list[T]]:
    return [t for t in power_set(s) if len(t) == k]


def insert[T](x: T, s: list[T], i: int) -> list[T]:
    return s[:i] + [x] + s[i:]
#mete el valro en cada indice 


def insert_everywhere[T](x: T, s: list[T]) -> list[list[T]]:
    return [insert(x, s, i) for i in range(len(s) + 1)]


def permute[T](s: list[T]) -> list[list[T]]:
    if not s:
        return [[]]
    empty: list[list[T]] = []
    return sum([insert_everywhere(s[-1], t) for t in permute(s[:-1])], empty)


#permutaciones sin repetecicones
def permutations[T](s: list[T], k: int) -> list[list[T]]:
    empty: list[list[T]] = []
    return sum([permute(e) for e in combinations(s, k)], empty)


#-------------------------------------------------------------------------------------------
def insert_everywhereP[T](x: T, s: list[T]) -> list[list[T]]:
    result: list[list[T]] = []
    for i in range(len(s) + 1):
        result.append(insert(x, s, i))
        if i < len(s) and s[i] == x:  # a partir de aquí serían repetidas
            break
    return result


def combinationsP[T](s: list[T], k: int) -> list[list[T]]: # filtra las psobles combianciones con la cantidad K
    if k == 0:
        return [[]]
    
    temp: list[list[T]] = []

    for i in range(len(s)): #para i que ira hasta el tamnao de la lista de s
     valorInicial:T = s[i]; #apenas toma el primer valor
     for x in combinationsP(s[i:], k-1):
         temp.append([valorInicial] + x)
    return temp

def permuteP[T](s: list[T]) -> list[list[T]]:
    if not s:
        return [[]]
    empty: list[list[T]] = []
    return sum([insert_everywhereP(s[-1], t) for t in permuteP(s[:-1])], empty)

def permutations_with_repetition[T](s: list[T], k: int) -> list[list[T]]:
    if not s:
        return []
    empty: list[list[T]] = []
    return sum([permuteP(e) for e in combinationsP(s, k)], empty)
    
    
    

#------------------------------------------------------------------------------------------------







def combinations_with_repetition[T](s: list[T],k: int) -> list[list[T]]:
    ...



    


















if __name__ == '__main__':
    # pprint(power_set([]))  # type: ignore
    # pprint(power_set([1]))
    # pprint(power_set(['a', 'b']))
    # pprint(power_set(['a', 'b', 'c']))
    # pprint(nicely_sorted(power_set(['a', 'b', 'c', 'd'])))
    # pprint(sorted(combinations([1, 2, 3, 4], 2)))
    # pprint(sorted(combinations([1, 2, 3, 4], 1)))
    # pprint(sorted(combinations([1, 2, 3, 4], 3)))
    # pprint(sorted(combinations([1, 2, 3, 4], 4)))
    # pprint(insert(7, [1, 2, 3], 0))
    # pprint(insert(7, [1, 2, 3], 1))
    # pprint(insert(7, [1, 2, 3], 2))
    # pprint(insert(7, [1, 2, 3], 3))
    #pprint(insert_everywhere(7, [1, 2, 3, 4, 5, 6]))
    # pprint(sorted(permute([1, 2, 3])))
    # pprint(sorted(permute([1, 2, 3, 4])))
    # pprint(sorted(permutations([1, 2, 3], 1)))
    # pprint(sorted(permutations([1, 2, 3], 2)))
    # pprint(sorted(permutations([1, 2, 3], 2)))
    # pprint(insert_everywhereP(7, [1, 2, 3], 2))
    #  pprint(sorted(combinationsP([1,2,3], 2)))
     pprint(sorted(permutations_with_repetition([0,1], 4)))
