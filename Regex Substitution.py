'''
The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda).
The method is called for all matches and can be used to modify strings in different ways.
The re.sub() method returns the modified string as an output.

Task

You are given a text of  lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:
&& -> and
|| -> or

Both && and || should have a space " " on both sides.

Input Format

The first line contains the integer, N.
The next N lines each contain a line of the text.

Constraints
0<N<100

Neither && nor || occur in the start or end of each line.

Output Format

Output the modified text.

'''

import re
#text = '\n'.join([input() for _ in range(int(input()))])
for _ in range(int(input())):
    text = input()
    text = re.sub(r' &&(?= )', ' and',  text)
    text = re.sub(r' \|\|(?= )', ' or', text)
    print(text)
