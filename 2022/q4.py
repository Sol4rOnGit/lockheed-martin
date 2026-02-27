#special treatment
import sys

cases = int(sys.stdin.readline().rstrip())

for case in range(cases):
    line = sys.stdin.readline().rstrip()

    s = []
    for i in range(len(line)):
        if(line[i].isalpha()):
            s.append(line[i])
        if(line[i].isnumeric()):
            s.append(line[i])
        if(line[i] == " "):
            s.append(line[i])

    answer = ""

    for j in range(len(s)):
        answer = answer + s[j]

    print(answer)