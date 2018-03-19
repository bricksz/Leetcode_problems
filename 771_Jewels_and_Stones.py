"""
:type J: str
:type S: str
:rtype: int
"""

#J = "z", S = "ZZ"

#J = "aA", S = "aAAbbbb"

J = 'abcAbC'
S = 'abnhyasvsaxavvanbdsajsbhewqbdascnhasbgvdaASFSBERDASDASDASGVDSGVSBasdasdcasdasdwewadasd'

# separates string into a set [ 'a', 'b', 'c', 'A', 'B', 'C' ]
# for each letter in S that is contained in set, value = 1, otherwise = 0


def numJewelsInStones(J, S):
    setJ = set(J)
    return sum(s in setJ for s in S)

c = (numJewelsInStones(J,S) / len(S))*100
c = round(c, 2)

print('Possible: ' ,numJewelsInStones(J,S))
print('Total: ', len(S))
print('Percent: {}' .format(c))