def solution(A, F, M):
    N = len(A)
    current_sum = sum(A)
    target_sum = M * (N + F)
    missing_sum = target_sum - current_sum

    if missing_sum < F or missing_sum > 6 * F:
        return [0]  

    
    possible_rolls = []

    for roll1 in range(1, 7):
        for roll2 in range(1, 7):
            
            roll_sum = roll1 + roll2

            if roll_sum == missing_sum:
                rolls = [roll1] * (F - 1) + [roll2]
                possible_rolls.append(rolls)

    if not possible_rolls:
        return [0]

    return possible_rolls[0] 