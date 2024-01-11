sentence = input()

number = sum([int(e) for e in sentence if e.isdigit()])
result = [e for e in sentence if not e.isdigit()]
result.sort()
result.append(str(number))

print("".join(result))