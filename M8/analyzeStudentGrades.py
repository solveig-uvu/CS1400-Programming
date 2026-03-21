def analyzeGrades(studentData: list) -> tuple:
    # Using a for loop to generate tuple of grades that will be used to calculate the average.
    grades = tuple(studentData[student][1] for student in range(len(studentData)))
    gradeAverage = sum(grades) / len(grades)
    # Using a lambda function to search through the student data input for the matching criteria, then assigning the variables based off of that.
    highest = max(studentData, key=lambda studentData: studentData[1])
    lowest = min(studentData, key=lambda studentData: studentData[1])
    highestStudent, lowestStudent = highest[0], lowest[0]
    highestGrade, lowestGrade = highest[1], lowest[1]
    analysis = (gradeAverage, highestGrade, highestStudent, lowestGrade, lowestStudent)
    return analysis
    

def main():
    students = [("Benji", 98), ("Sierra", 87), ("Tanner", 65), ("Whitney", 79)]
    analysis = analyzeGrades(students)
    print(f"Average Grade: {analysis[0]} \nHighest Grade: {analysis[1]} ({analysis[2]}) \nLowest Grade: {analysis[3]} ({analysis[4]})")

if __name__ == '__main__':
    main()