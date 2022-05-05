def perm_gen_lex(str_in: str) -> list:
    '''Return a list of all possible permutations of input string'''
    if type(str_in) != str:
        print("Error: Wrong input type")
        raise ValueError
    perm = []
    if len(str_in) == 1:
        return [str_in]
    else:
        for idx in range(len(str_in)):
            first = str_in[idx]
            next = str_in[:idx] + str_in[idx + 1:]
            for item in perm_gen_lex(next):
                perm.append(first + item)
    return perm
