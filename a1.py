BRICK = "o"
CHK = "x"
SPACE = " "
NEWLINE = "\n"
LEVEL = 1
GV=0
L=1
R="r"
var_fill=0
total=0



def percentage(numerator, denominator):
    temp1 = float(numerator)*100
    temp2 = float(denominator)
    fin = temp1/temp2
    fin2 = math.ceil(fin*100)
    return fin2/100


def brickfunction(jk):
    matrixvar = 50
    if jk < 0:
        matrixvar +=1
    elif jk == 0:
        matrixvar +=0
    else:
        matrixvar -=1
    matrixvar = 1
    answer = jk * matrixvar
    return answer



