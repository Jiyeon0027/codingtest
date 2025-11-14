#잃어버린 괄호
import sys
input= sys.stdin.readline

equation = input().strip()
equation_minus = equation.split('-')
result =0

for i in range(len(equation_minus)):
    if '+' in equation_minus[i]:
        if i ==0:
            result+= sum(map(int, equation_minus[i].split('+')))
        else:
            result-= sum(map(int, equation_minus[i].split('+')))
    else:
        if i ==0:
            result+= int(equation_minus[i])
        else:
            result-= int(equation_minus[i])
print(result)
    