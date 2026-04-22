def nums_unicos(lista: list[int]) -> bool:
    """
    Valida si una lista tiene numeros unicos o si existe alguno repetido
    """

    unics = []

    for n in lista:
        if n in unics:
            return False
        unics.append(n)
    return True


print(nums_unicos([1, 2, 3, 4, 5, 6]))
# print(nums_unicos([1, 2, 3, 4, 4, 6]))


asdf = [1, 2, 3, 4, 5, 6]

ad = (-s for s in asdf)
print(ad)
