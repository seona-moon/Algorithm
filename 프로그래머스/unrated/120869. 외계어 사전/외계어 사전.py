def solution(spell, dic):
    for e in dic:
        if set(e) - set(spell):
            continue
        if len(spell) == len(set(e)):
            return 1
    return 2