# Setting up the analysis function.
def analyzeMedals(data:list) -> list:
    totalMedals = []
    for country in range(len(data)):
        total = sum(data[country][1])
        c, t = data[country][0], total
        analyzedCountry = (c, t)
        totalMedals.append(analyzedCountry)
    return sorted(totalMedals, reverse=True)

def main():
    olympicData = [("USA", (10, 8, 6)), ("China", (8, 10, 5)), ("Germany", (5, 3, 4)), ("Japan", (6, 5, 7))]
    analyzed = analyzeMedals(olympicData)
    analysisWinner = analyzed[0][0]
    for c in range(len(analyzed)):
        winner = olympicData[0].index(analysisWinner)
    for country in range(len(analyzed)):
        print(f"{analyzed[country][0]} with {analyzed[country][1]} medals")
    print(f"The country with the most total gold medals is {olympicData[winner][0]}, with {olympicData[winner][1][0]} gold medals.")
    
if __name__ == '__main__':
    main()