def solution_task1(S):
    deletions = 0
    letter_count = {}  
    for letter in S:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    for count in letter_count.values():
        if count % 2 != 0:
            deletions += 1

    return deletions
