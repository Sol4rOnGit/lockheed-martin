import sys

cases = int(sys.stdin.readline().rstrip())

for case in range(cases):
    dimensions = sys.stdin.readline().rstrip().split()

    height, width = map(int, dimensions)

    for i in range(height):
        current_line = sys.stdin.readline().rstrip()