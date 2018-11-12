import re

def Determinant(mat):
    sign = 1
    result = 0

    if (len(mat) == 1):
        return mat[0][0];

    for i in range(len(mat)):
        fragMatrix = [];
        for j in range (len(mat)):
            if(i!=j):
                fragMatrix.append(mat[j][1:])
        result+= sign * mat[i][0] * Determinant(fragMatrix);
        sign*=-1
    return result

def CreateMatrix():
    for row in range(matrixlength):
        length = len(SplittedEqMatrix[row]);
        for elmnt in range (length):
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

    lastknown = 0
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


if __name__ == '__main__':

    file = open('cremer_input.txt', 'r')
    str = file.read()
    equations = []
    lines=[]
    for line in str.splitlines():
        lines.append(line.strip())

    print("Equations : ")
    for i in lines:
        print(i)

    for i in lines:
        equations.append(i)

    matrixlength = len(equations)

    variables = []
    SplittedEqMatrix = []
    matrix = [[0] * (matrixlength + 1) for _ in range(matrixlength)]
    squareMatrix = []

    for str in equations:
        Parser(str)

    CreateMatrix()
    det = Determinant(squareMatrix)
    file = open('cremer_output.txt', 'w')
    dictionary={}

    for i in range(matrixlength):
        tempMatrix = []
        for j in range(matrixlength):
            tempMatrix.append(squareMatrix[j][:i] + matrix[j][len(squareMatrix):] + squareMatrix[j][i + 1:])
        variable_deter = Determinant(tempMatrix);
        ans = variable_deter / det;

        if(ans==0.0):ans = 0.0;
        dictionary[variables[i]]=ans

    print("\nSolutions : ")
    for element in sorted(dictionary.keys()):
        file.write(element+" = "+repr(dictionary[element])+ '\n')
        print("%s = %f"%(element,dictionary[element]))
    file.close()