def readFile(filename):
    return [float(i) for i in open(filename, 'r').read().strip().split('\n')]