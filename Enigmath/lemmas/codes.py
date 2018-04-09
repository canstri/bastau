from sympy import *
from lemmas.split import splitting
from lemmas.splitFinal import splitFinal
from sympy.parsing.sympy_parser import parse_expr
class LemmaCode(object):
    def isequal(input_exp):
        status = False
        newStr = str(input_exp)
        RHS = ""
        LHS = ""
        znak = ""

        bool = False
        try:
            LHS,RHS,znak = splitting(newStr)
        except Exception as e:
            return('Wrong')

        if LHS.factor() == RHS.factor() and znak == '=':
            status = True
        if status == True:
            return('Correct')
        return('Wrong')

    def is_sequence(input_exp):
        print(input_exp)
        status = False

        newStr = str(input_exp)
        for i in range(len(newStr) - 1):
            if (newStr[i] == ';'):
                return('Wrong')

        try:
            part1, part2,part3 = newStr.split('*')
            print(part1)
        except Exception as e:
            return('Exception')  # later need to change to Wrong

        input1 = parse_expr(part1)
        input2 = parse_expr(part2)
        input3 = parse_expr(part3)

        arr = [input1,input2,input3]
        array = sympify(arr)

        delta = 1
        for index in range(len(array) - 1):
            if (array[index + 1] - array[index] == delta):
                status = True
        if status == True:
            return('Correct')
        return('Wrong')


    def finalCheck(input_exp): #n**3-n =(n-1)*n*(n + 1) Correct
                                                  #(n-1)*n*(n + 1)#24 Correct
                                                  # n**3-n#24

        print(input_exp)
        try:
             input_exp1, input_exp2, input_exp3  = input_exp.split(';')
        except Exception as e:
            return('Exception')  # later need to change

        status = False
        expressionFirst, statusFirst = splitFinal(input_exp1)
        expressionSecond, statusSecond = splitFinal(input_exp2)

        partOne, partTwo, sign = splitting(expressionFirst)
        partThree, dividerOne, sign = splitting(expressionSecond)
        partFour, dividerTwo, sign = splitting(input_exp3)

        if((factor(partOne) == factor (partThree)) and (statusFirst == statusSecond == 'Correct')
            and (sympify(partOne) == sympify(partFour)) and (dividerOne == dividerTwo)):
            status = True
        if((factor(partTwo) == factor(partThree)) and (statusFirst == statusSecond == 'Correct')
            and (sympify(partTwo) == sympify(partFour)) and (dividerOne == dividerTwo)):
            status = True

        if status == True:
                return('Correct')
        return('Wrong')
