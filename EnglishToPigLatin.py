import fileinput

inp = []
for line in fileinput.input():
    inp.append(line.strip())

# Initialize some variables we will need later
output = []
vowels = 'aeiouy'

# creates a list containing lines of english translated to pig latin
# each "line" is a list of the pig latin words
for line in inp:
    words = line.split(' ')
    outputLine = []
    for word in words:
        if word[0] not in vowels:
            firstVowelIndex = -1
            for x in range(len(word)):
                if word[x] in vowels:
                    firstVowelIndex = x
                    break
            beforeVowel = word[0:firstVowelIndex]
            word = word[firstVowelIndex:]
            word += beforeVowel
            word += 'ay'
            outputLine.append(word)
        elif word[0] in vowels:
            word += 'yay'
            outputLine.append(word)
    output.append(outputLine)

for line in output:
    for word in line:
        if word == line[-1]:
            print(word)
        else:
            print(word, ' ', end='')