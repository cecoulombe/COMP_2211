def main():
    print("Enter the person's age group", end ="")
    ageGroup = input("(child, minor, adult, or senior): ")
    print("The admission feee is", determineAdmissionFee(ageGroup), "dollars.")

def determineAdmissionFee(ageGroup):
    ageDict = {"child": 0, "minor" : 5, "adult" : 10, "senior" : 8}

    if ageGroup in ageDict:
        return ageDict[ageGroup]
    
main()