def execute(coins, coinTypeNum, sum, memory):
    if sum == 0:
        combinations = [[]]
        return combinations
    if sum < 0 or coinTypeNum < 0:
        return []
    key = str(coinTypeNum) + "->" + str(sum)
    if key not in memory:
        takenCombinations = execute(coins, coinTypeNum, sum - coins[coinTypeNum], memory)
        notTakenCombinations = execute(coins, coinTypeNum-1, sum, memory)
        combinations = []
        for combination in takenCombinations:
            takenCombination = combination[:]
            takenCombination.append(coins[coinTypeNum])
            combinations.append(takenCombination)
        combinations += notTakenCombinations
        memory[key] = combinations
    return memory[key]