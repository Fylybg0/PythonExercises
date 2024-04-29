import sys
from readFile import readFile

def getAverage(array):
    if not array:
        return None
    return sum(array) / len(array)

def main():
    if len(sys.argv) != 2:
        print("Usage: python getAverage.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
       numbers = readFile(file_path)

    except FileNotFoundError:
        print("File not found:", file_path)
        sys.exit(1)

    except ValueError:
        print("Invalid data found in the file.")
        sys.exit(1)

    average = getAverage(numbers)
    print("Average:", average)

if __name__ == "__main__":
    main()