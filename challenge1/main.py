# Given a string, write a function that returns the top K most frequently occurring characters from it.
# Example: s =  "aabreijkje121a", k = 3
# frequency of every char:
# a => 3
# b => 1
# r => 1
# e => 2
# i => 1
# j => 2
# k => 1
# 1 => 2
# 2 => 1
# Order of Descending Frequency: a,e,j,1,b,r,i,k,2
# Top 3 most frequently occuring chars: a,e,j,1


def topK(s, k):
    out = []
    tempDict = dict((i, 0) for i in set(s))
    for i in s:
        tempDict[i] = tempDict[i] + 1
    sortedCharArray = [k for k, _ in sorted(
        tempDict.items(), key=lambda x: x[1], reverse=True)]
    for i in range(k):
        out.append(sortedCharArray[i])
    return out


if __name__ == "__main__":
    s = "aabreijkje121a"
    k = 4
    out = topK(s, k)
    print(out)
