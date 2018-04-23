from sympy import *
from maths.split import splitting
from maths.splitFinal import splitFinal
from maths.containsChar import ContainsChar
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
    def checkInequalities(input_exp): # a>b Correct; a+c > b+c                   3<=5 Correct; 5 >=3
        status =False

        try:
             input_exp1, input_exp2  = input_exp.split(';')
        except Exception as e:
            return('Wrong')

        try:
            expressionFirst, statusFirst = splitFinal(input_exp1)
        except Exception as e:
            return('Wrong')

        try:
            leftPartOne,rightPartOne,signOne = splitting(expressionFirst)
        except Exception as e:
            return('Wrong')

        try:
            leftPartTwo,rightPartTwo,signTwo = splitting(input_exp2)
        except Exception as e:
            return('Wrong')

        subtractionFirst = leftPartOne - rightPartOne
        subtractionSecond = leftPartTwo - rightPartTwo

        divisionLeft = leftPartOne / rightPartOne
        divisionRight = leftPartTwo / rightPartTwo

        if((subtractionFirst == subtractionSecond) and (statusFirst == 'Correct')
            and ((signOne == signTwo) and (signOne != '=')) and (simplify(input_exp2)==True)):
            status = True
        elif((divisionLeft ==divisionRight) and (statusFirst == 'Correct') and (simplify(input_exp2)==True) ):
            status = True
        elif((leftPartOne == rightPartTwo) and (rightPartOne == leftPartTwo) and (statusFirst == 'Correct')
            and  (signOne!= signTwo) and (simplify(input_exp2)==True) ):
            status = True
        elif((leftPartOne == 1/leftPartTwo) and (rightPartOne == 1/ rightPartTwo) and (statusFirst == 'Correct')
            and  (signOne!= signTwo) and (simplify(input_exp2)==True)):
            status = True

        if status == True:
                return('Correct!')
        return('Wrong')

    def threeInputsEquality(input_exp):
        status =False

        try:
             input_exp1, input_exp2, input_exp3 = input_exp.split(';')
        except Exception as e:
            return('Wrong')

        try:
            expressionFirst, statusFirst = splitFinal(input_exp1)
        except Exception as e:
            return('Wrong')

        try:
            leftPartOne,rightPartOne,signOne = splitting(expressionFirst)
        except Exception as e:
            return('Wrong')

        try:
            expressionSecond, statusSecond = splitFinal(input_exp2)
        except Exception as e:
            return('Wrong')

        try:
            leftPartTwo,rightPartTwo,signTwo = splitting(expressionSecond)
        except Exception as e:
            return('Wrong')

        try:
            leftPartThree,rightPartThree,signThree = splitting(input_exp3)
        except Exception as e:
            return('Wrong')

        if(signOne == signTwo == signThree):
            if( (leftPartThree == leftPartOne+leftPartTwo) and (rightPartThree == rightPartOne+ rightPartTwo) ):
                status = True
            elif( (leftPartThree == leftPartOne-leftPartTwo) and (rightPartThree == rightPartOne - rightPartTwo) ):
                status = True
            elif( (leftPartThree == leftPartOne*leftPartTwo) and (rightPartThree == rightPartOne * rightPartTwo) ):
                status = True

        if status == True:
                return('Correct!')
        return('Wrong')

    def threeInputsEquality2(input_exp):
        status =False

        try:
             input_exp1, input_exp2, input_exp3 = input_exp.split(';')
        except Exception as e:
            return('Wrong')

        try:
            expressionFirst, statusFirst = splitFinal(input_exp1)
        except Exception as e:
            return('Wrong')

        try:
            leftPartOne,rightPartOne,signOne = splitting(expressionFirst)
        except Exception as e:
            return('Wrong')

        try:
            expressionSecond, statusSecond = splitFinal(input_exp2)
        except Exception as e:
            return('Wrong')

        try:
            leftPartTwo,rightPartTwo,signTwo = splitting(expressionSecond)
        except Exception as e:
            return('Wrong')

        try:
            leftPartThree,rightPartThree,signThree = splitting(input_exp3)
        except Exception as e:
            return('Wrong')

        one = {leftPartOne, rightPartOne}
        two = {leftPartTwo, rightPartTwo}
        three = {leftPartThree, rightPartThree}
        union = {leftPartOne, rightPartOne,leftPartTwo, rightPartTwo, leftPartThree, rightPartThree}
        inter = one.intersection(two)

        if((signOne == signTwo == signThree) and (three == union.difference(inter))):
            status = True

        if status == True:
                return('Correct!')
        return('Wrong')
    def threeInputsGreaterZero(input_exp):
        status =False

        try:
             input_exp1, input_exp2, input_exp3 = input_exp.split(';')
        except Exception as e:
            return('Wrong')

        try:
            expressionFirst, statusFirst = splitFinal(input_exp1)
        except Exception as e:
            return('Wrong')

        try:
            leftPartOne,rightPartOne,signOne = splitting(expressionFirst)
        except Exception as e:
            return('Wrong')

        try:
            expressionSecond, statusSecond = splitFinal(input_exp2)
        except Exception as e:
            return('Wrong')

        try:
            leftPartTwo,rightPartTwo,signTwo = splitting(expressionSecond)
        except Exception as e:
            return('Wrong')
        try:
            leftPartThree,rightPartThree,signThree = splitting(input_exp3)
        except Exception as e:
            return('Wrong')

        #lemma 15
        if(rightPartOne == rightPartTwo == rightPartThree == 0):
            if((statusFirst == statusSecond == 'Correct') and ((simplify(input_exp3) == True) or (leftPartOne/leftPartTwo == leftPartThree) or ((leftPartTwo/leftPartOne == leftPartThree)))):
                if(signOne == signTwo and signThree == '>'):
                    status = True
            #lemma16
                elif(signOne != signTwo and signThree == '<'):
                    status = True

        if status == True:
                return('Correct!')
        return('Wrong')
    def threeInputsInequality(input_exp): # a>b Correct; x>y Correct; a*x +b*y > a*y +b*x
        status =False

        try:
             input_exp1, input_exp2, input_exp3 = input_exp.split(';')
        except Exception as e:
            return('Wrong')

        try:
            expressionFirst, statusFirst = splitFinal(input_exp1)
        except Exception as e:
            return('Wrong')

        try:
            leftPartOne,rightPartOne,signOne = splitting(expressionFirst)
        except Exception as e:
            return('Wrong')

        try:
            expressionSecond, statusSecond = splitFinal(input_exp2)
        except Exception as e:
            return('Wrong')

        try:
            leftPartTwo,rightPartTwo,signTwo = splitting(expressionSecond)
        except Exception as e:
            return('Wrong')
        try:
            leftPartThree,rightPartThree,signThree = splitting(input_exp3)
        except Exception as e:
            return('Wrong')
        #lemma17

        if(signOne == signTwo and signThree == '>='): # and simplify(input_exp3) == True
            left = leftPartOne * leftPartTwo + rightPartOne * rightPartTwo
            right = leftPartOne * rightPartTwo + leftPartTwo * rightPartOne
            if(sympify(leftPartThree) == sympify(left) and sympify(rightPartThree) == sympify(right)):
                status = True
        if status == True:
                return('Correct!')
        return('Wrong')
    def fourInputsEquality(input_exp):
        status =False

        try:
             input_exp1, input_exp2, input_exp3,input_exp4 = input_exp.split(';')
        except Exception as e:
            return('Wrong')

        try:
            expressionFirst, statusFirst = splitFinal(input_exp1)
        except Exception as e:
            return('Wrong')

        try:
            leftPartOne,rightPartOne,signOne = splitting(expressionFirst)
        except Exception as e:
            return('Wrong')

        try:
            expressionSecond, statusSecond = splitFinal(input_exp2)
        except Exception as e:
            return('Wrong')

        try:
            leftPartTwo,rightPartTwo,signTwo = splitting(expressionSecond)
        except Exception as e:
            return('Wrong')
        try:
            expressionThree, statusThree = splitFinal(input_exp3)
        except Exception as e:
            return('Wrong')

        try:
            leftPartThree,rightPartThree,signThree = splitting(expressionThree)
        except Exception as e:
            return('Wrong')
        try:
            leftPartFour,rightPartFour,signFour = splitting(input_exp4)
        except Exception as e:
            return('Wrong')

        left = leftPartOne + leftPartTwo + leftPartThree
        right = rightPartOne + rightPartTwo + rightPartThree

        leftMul = leftPartOne * leftPartTwo * leftPartThree
        rightMul = rightPartOne * rightPartTwo * rightPartThree
        #lemma18
        if(signOne == signTwo == signThree == signFour == '='): # and simplify(input_exp4) == True

            if(sympify(left) == sympify(leftPartFour) and sympify(right) == sympify(rightPartFour)):
                status = True

            elif(sympify(leftMul) == sympify(leftPartFour) and sympify(rightMul) == sympify(rightPartFour)):
                status = True

        if status == True:
                return('Correct!')
        return('Wrong')
    print(fourInputsEquality('a=b Correct; c=d Correct; e=f Correct; a*c*e = b*d*f'))