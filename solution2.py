def solution_task2(S):
    max_sum = -1  

    for i in range(len(S) - 2):
        fragment1 = int(S[i:i+2])
        for j in range(i + 2, len(S) - 1):
            fragment2 = int(S[j:j+2])
            max_sum = max(max_sum, fragment1 + fragment2)

    return max_sum
