def main():
    SENTINEL = 0
    num = -1
    numList = []
    while True:
        num = getInt()
        if(int(num) == SENTINEL):
            break
        else:
            numList.append(num)
    
    numList.sort()
    print(numList)
        

def getInt():
    while True:
        try:
            num = int(input("Please enter a number or enter 0 to exit: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
main()