def main():
    scorebook = dict()
    scorebook["Alice"] = 88
    scorebook["Bob"] = 75
    scorebook["Charlie"] = 93
    scorebook["Dana"] = 80

    # For loop to print everything
    for key in scorebook:
        value = scorebook[key]
        print(f"{key}: {value}")
    scorebook["Dana"] = 85
    scorebook.pop("Bob")
    eveExists = scorebook.get("Eve", False)
    if eveExists:
        print("Eve was found in the scorebook!")
    else:
        print("Eve does not exist.")
    averageScore = round(sum(scorebook.values()) / len(scorebook))
    print(f"The average score is {averageScore}.")

if __name__ == '__main__':
    main()