def readFile(filename):
    return [int(i) for i in open(filename, 'r').read().strip().split('\n')]

numbers = readFile('numbers.txt')

print(numbers)