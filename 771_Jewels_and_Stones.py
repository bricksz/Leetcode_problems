"""
:type J: str
:type S: str
:rtype: int
"""

#J = "z", S = "ZZ"

#J = "aA", S = "aAAbbbb"

J = 'abcAbC'
S = 'abnhyasvsaxavvanbdsajsbhewqbdascnhasbgvdaASFSBERDASDASDASGVDSGVSB'

# separates string into a set [ 'a', 'b', 'c', 'A', 'B', 'C' ]
# for each letter in S that is contained in set, value = 1, otherwise = 0


def numJewelsInStones(J, S):
    setJ = set(J)
    return sum(s in setJ for s in S)

print(numJewelsInStones(J,S))