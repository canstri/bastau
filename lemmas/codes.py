from sympy import *
from lemmas.split import splitting
from lemmas.splitFinal import splitFinal
from lemmas.containsChar import ContainsChar
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

    def is_sequence(input_exp): #uncomment lines in codes.py

        status = False
        try:
            expression, divider, sign1 = splitting(input_exp)
            expression = str(expression)
        except Exception as e:
            return('Exception')  # later need to change to Wrong


        try:
            part1, part2,part3 = ContainsChar(expression).split('*')

        except Exception as e:
            return('Exception')  # later need to change to Wrong

        arr = [int(expand(part1)),int(expand(part2)),int(expand(part3))]
        array = sorted(arr)

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


        print('will try')
        try:
             input_exp1, input_exp2, input_exp3  = input_exp.split(';')
        except Exception as e:
            return('Exception')  # later need to change

        status = False
        expressionFirst, statusFirst = splitFinal(input_exp1)
        expressionSecond, statusSecond = splitFinal(input_exp2)

        partOne, partTwo, sign1 = splitting(expressionFirst)
        partThree, dividerOne, sign2 = splitting(expressionSecond)
        partFour, dividerTwo, sign3 = splitting(input_exp3)

        if((factor(partOne) == factor (partThree)) and (statusFirst == statusSecond == 'Correct')
            and (sympify(partOne) == sympify(partFour)) and (dividerOne == dividerTwo)):
            status = True
        if((factor(partTwo) == factor(partThree)) and (statusFirst == statusSecond == 'Correct')
            and (sympify(partTwo) == sympify(partFour)) and (dividerOne == dividerTwo)):
            status = True

        if status == True:
                return('Correct')
        return('Wrong')
    #print(is_sequence('(n-1)*n*(n + 1)#24'))
    def zamena(input_exp):

        print('here')
        status = False
        try:
             input_exp1, input_exp2  = input_exp.split(';')
        except Exception as e:
            return('Exception1')  # later need to change
        try:
            expressionFirst, statusFirst = splitFinal(input_exp1)
        except Exception as e:
            return('Exception2')  # later need to change

        try:
            part1,part2,sign = splitting(input_exp2)
        except Exception as e:
            return('Exception3')

        expressionFirst = str(expressionFirst)
        part1 = str(part1)
        part2 = str(part2)
       
        expressionFirst = expressionFirst.replace(part1, part2)
        return(expressionFirst)
        
