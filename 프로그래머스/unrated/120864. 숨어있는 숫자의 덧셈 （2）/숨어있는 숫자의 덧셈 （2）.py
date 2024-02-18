def solution(my_string):
    nums = [e if e.isdigit() else 0 for e in my_string]
    result = 0
    letter = ""
    for i in range(len(my_string)):
        if nums[i]==0:
            if(letter):
                result += int(letter)
                letter = ""
        else:
            letter+=nums[i]
    if letter:
        result += int(letter)
    return result