import re
def CreateMatrix():
    for row in range(matrixlength):
        length = len(SplittedEqMatrix[row]);
        for elmnt in range(length):
            for itr in range(matrixlength):
                if SplittedEqMatrix[row][elmnt].__contains__(variables[itr]):
                    c = list(re.finditer(r'[a-z]', SplittedEqMatrix[row][elmnt], re.I))[0]
                    q = SplittedEqMatrix[row][elmnt][:c.start()];
                    if(len(q)==1):
                        q+="1";

                    num = float(q)
                    matrix[row][itr] = num;

        squareMatrix.append(matrix[row][:-1])
        matrix[row][-1] = float(SplittedEqMatrix[row][-1])

def Parser(line_string):
    pattern = re.compile(r'\s+')
    line_string = re.sub(pattern, '', line_string)
    if(line_string[0]!= "-" and line_string[0]!= "+"):
        line_string= "+" + line_string
    lastknown = 0;
    parsed = []
    for c in range(len(line_string[1:])):
        if(line_string[c + 1]== "+" or line_string[c + 1]== "-" or line_string[c + 1]== "="):
            parsed.append(line_string[lastknown:c + 1])
            lastknown = c+1;
        if(line_string[lastknown]== "="):
            break

    for elmnt in parsed:
        c = list(re.finditer(r'[a-z]', elmnt, re.I))[0]
        if(not variables.__contains__(elmnt[c.start():])):
            variables.append(elmnt[c.start():])

    parsed.append(line_string[lastknown + 1:])
    SplittedEqMatrix.append(parsed)



def RowOperation():
    k = 0;flag = 0;
    for i in range (matrixlength):
        if(matrix[i][i]==0):
            c=1;
            while(matrix[i+c][c]==0 and (i+c)<matrixlength):
                c+=1
            if(i+c==matrixlength):
                flag=1
                break
            j=i
            for k in range (matrixlength+1):
                matrix[j][k],matrix[j+c][k]=matrix[j+c][k],matrix[j][k]

        for j in range (matrixlength):
            if(i!=j):
                pro = matrix[j][i]/matrix[i][i]
                for k in range(matrixlength+1):
                    matrix[j][k]=matrix[j][k]-matrix[i][k]*pro
    return flag

def ConsistencyCheck():
    flag = 3
    for i in range(matrixlength):
        sum = 0
        for j in range(matrixlength):
            sum+=matrix[i][j]
        if(sum==matrix[i][j]):
            flag = 2;
    return flag

if __name__ == '__main__':

    equ = []

    file = open('ero_input.txt', 'r')
    str = file.read()
    datalines = [s.strip() for s in str.splitlines()]

    print("Equations : ")
    for i in datalines:
        print(i)

    for i in datalines:
        equ.append(i)

    matrixlength = len(equ)

    variables = []
    SplittedEqMatrix = []
    matrix = [[0] * (matrixlength + 1) for _ in range(matrixlength)]
    squareMatrix = []

    for str in equ:
        Parser(str)

    CreateMatrix()

    flag = 0
    flag = RowOperation()
    if(flag==1):
        flag=ConsistencyCheck()

    print("\nFinal augmented matrix : ")
    for i in matrix:
        print(i)
    print()

    if(flag==2):
        print("Infinte Solution")
    if(flag==3):
        print("No Solution")

    file = open('ero_output.txt', 'w')

    dictionary = {}
    for i in range (matrixlength):
        result = matrix[i][-1]/matrix[i][i]
        dictionary[variables[i]] = result

    print("\nSolutions : ")
    for element in sorted(dictionary.keys()):
        file.write(element + " = " + repr(dictionary[element]) + '\n')
        print("%s = %f" % (element, dictionary[element]))

    file.close()
