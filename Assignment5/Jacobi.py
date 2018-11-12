import re

def Cutting(str):
    pattern = re.compile(r'\s+')
    str = re.sub(pattern, '', str)
    if(str[0]!="-" and str[0]!="+"): #sob varible same format e ana 1st +/- thakbe
        str="+"+str

    parsed = []
    lastknown = 0;

    for c in range(len(str[1:])): #delimiting
        if(str[c+1]=="+" or str[c+1]=="-" or str[c+1]=="="):
            parsed.append(str[lastknown:c+1])
            lastknown = c+1;
        if(str[lastknown]=="="):
            break

    for elmnt in parsed: #unique varible khuje bair kora
        c = list(re.finditer(r'[a-z]', elmnt, re.I))[0]
        if(not variables.__contains__(elmnt[c.start():])):
            variables.append(elmnt[c.start():])

    parsed.append(str[lastknown+1:])
    almostReady.append(parsed)

def BuildMatrix():
    for row in range(matrixlength):
        length = len(almostReady[row]);
        for elmnt in range (length):
            for itr in range(matrixlength):
                if almostReady[row][elmnt].__contains__(variables[itr]):
                    c = list(re.finditer(r'[a-z]', almostReady[row][elmnt], re.I))[0]
                    q = almostReady[row][elmnt][:c.start()];
                    if(len(q)==1):
                        q+="1";

                    num = float(q)
                    matrix[row][itr] = num;

        squareMatrix.append(matrix[row][:-1])
        matrix[row][-1] = float(almostReady[row][-1])

def Jacobi(ans):
    temp = []
    for i in range(100):
        prev = ans
        for j in range(matrixlength):
            temp.append(matrix[j][-1])
            for k in range(matrixlength):
                if(k!=j):
                    temp[j]-=(matrix[j][k]*ans[k])
            temp[j]/=matrix[j][j]
        ans = temp;
        temp=[]
    return ans


if __name__ == '__main__':

    equ = []
    #fname = '4a' ;

    f = open('input.txt', 'r')
    str = f.read()
    #data_string.split('\n\t *')
    datalines = [s.strip() for s in str.splitlines()]
    print(datalines)

    for i in datalines:
        equ.append(i)

    matrixlength = len(equ)

    variables = []
    almostReady = []
    matrix = [[0] * (matrixlength + 1) for _ in range(matrixlength)]
    squareMatrix = []
    ans = []

    for str in equ:
        Cutting(str)

    BuildMatrix()

    for i in range(matrixlength) :
        ans.append(float(input()))


    ans=Jacobi(ans)

    f = open('output.txt', 'w')

    for i in range(matrixlength):

        f.write(variables[i]+"="+repr(ans[i]) + '\n')

    f.close()
