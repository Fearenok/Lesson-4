# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


def remake(equation):
    dictEqution = {}
    equation = equation.replace(' - ', ' -').replace(' + ', ' +')
    equation = equation.split()
    equation = equation[:-2]
    for i in range(len(equation)):
        equation[i] = equation[i].replace('+','').split('x**')
        dictEqution[int(equation[i][1])] = int(equation[i][0])
    return dictEqution

def sumEquation(dict1, dict2):
    dictFinal = {}
    maximum = (max(max(dict1), max(dict2)))
    for i in range(maximum, -1, -1):
        first = dict1.get(i)
        second = dict2.get(i)
        if first != None or second != None:
            dictFinal[i] = (first if first != None else 0) + (second if second != None else 0)
        return dictFinal

def coefResult(dictFinal):
    result = ''
    for i in dictFinal.items():
        if result == '':
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
            elif i[1] > 0:
                result += str(abs(i[1])) + 'x^' + str(abs(i[0]))
        else:
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
            elif i[1] > 0:
                result += ' + ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
        result = result.replace('x^1', 'x').replace('x^0', '').replace('1x^', 'x')
    return result + ' = 0'


with open('file5.txt', 'r', encoding='utf-8') as text:
    equation = text.readline()
with open('file5.1.txt', 'r', encoding='utf-8') as text:
    equation2 = text.readline()
print(equation)
print(equation2)
dictEquation = remake(equation)
dictEquation2 = remake(equation2)
print(dictEquation)
print(dictEquation2)

dictFinal = sumEquation(dictEquation, dictEquation2)
print(dictFinal)

dictFinal = coefResult(dictFinal)
print(dictFinal)
with open('file6.txt', 'w', encoding='utf-8') as text:
    text.writelines(dictFinal)