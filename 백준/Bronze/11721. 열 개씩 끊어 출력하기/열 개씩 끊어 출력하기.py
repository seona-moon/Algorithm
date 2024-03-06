sentence = input()
while len(sentence) > 10:
    print(sentence[0:10])
    sentence = sentence[10:]
if sentence:
    print(sentence)