if __name__ == '__main__':
    scores = []
    lowestScore = 100.0
    secondLowestScore = float()
    secondLowestRank = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([name, score])
        if score < lowestScore:
            secondLowestScore = lowestScore
            lowestScore = score
        elif lowestScore < score < secondLowestScore:
            secondLowestScore = score

    for rank in scores:
        if rank[1] == secondLowestScore:
            secondLowestRank.append(rank[0])
    secondLowestRank.sort()
    print(*secondLowestRank, sep = "\n")