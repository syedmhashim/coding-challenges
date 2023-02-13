def two_sum_prob(sum, strArr):
    intSum = int(sum)
    strToInt = lambda s : int(s)
    arr = strArr.split(",")
    intArr = list(map(strToInt, arr))
    tempDict = {}
    outList = []
    for i in intArr:
        tempDict[i] = i
        if intSum - i in tempDict.keys() :
            outList.append([i,intSum - i])
    print(outList)

if __name__ == "__main__":
    def remove_new_line_char(line):
        return line.replace("\n","")
    
    with open("input.txt") as f:
        lines = f.readlines()    
        lines = list(map(remove_new_line_char, lines))
        sum = lines[0]
        print(f"sum: {sum}")
        test_cases = lines[1:]
        for i in range(len(test_cases)):
            print(test_cases[i])
            two_sum_prob(sum, test_cases[i])

