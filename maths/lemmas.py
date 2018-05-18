from sympy import *
from .split import splitting
from .splitFinal import splitFinal
from .containsChar import containsChar
from sympy.parsing.sympy_parser import parse_expr
from .findPower import findPower

class LemmaCode(object):
    def isEqual(input_exp):
        status = False
        newStr = str(input_exp)
        RHS = ""
        LHS = ""
        sign = ""

        bool = False
        try:
            LHS,RHS,sign = splitting(newStr)
        except Exception as e:
            return('Wrong')

        if LHS.factor() == RHS.factor() and sign == '=':
            status = True
        if status == True:
            return('Correct')
        return('Wrong')
    #print(isEqual('(a-1)*(a+1)=a**2-1'))

    def isSequence(input_exp):

        status = False
        try:
            expression, divider, sign1 = splitting(input_exp)
            expression = str(expression)
        except Exception as e:
            return('Wrong')


        try:
            part1, part2,part3 = containsChar(expression).split('*')

        except Exception as e:
            return('Wrong')

        arr = [int(expand(part1)),int(expand(part2)),int(expand(part3))]
        array = sorted(arr)

        delta = 1
        for index in range(len(array) - 1):
            if (array[index + 1] - array[index] == delta):
                status = True
        if status == True:
            return('Correct')
        return('Wrong')

    def checkForEven(input_exp):
        status = False
        try:
            expression, divider, signOne = splitting(input_exp)
            expression = str(expression)
        except Exception as e:
            return('Wrong')

        try:
            part1, part2 = expression.split('*')
        except Exception as e:
            return('Wrong')

        if(((abs(sympify(part1)-sympify(part2)))%4==2)):
            status = True

        if status == True:
            return('Correct')
        return('Wrong')

    def preLastCheck(input_exp): # (n-1)*n*(n + 1)#3 Correct; (n-1)*(n+1)#8 Correct; (n-1)*n*(n + 1)#24

        status = False
        result = 1
        try:
            input_exp1, input_exp2, input_exp3  = input_exp.split(';')
        except Exception as e:
            return('Wrong')

        try:
            expressionFirst, statusFirst = splitFinal(input_exp1)
        except Exception as e:
            return('Wrong')

        try:
            expressionSecond, statusSecond = splitFinal(input_exp2)
        except Exception as e:
            return('Wrong')
        try:
            partOne, dividerOne, signOne = splitting(expressionFirst)
        except Exception as e:
            return('Wrong')

        try:
            partTwo, dividerTwo, signTwo = splitting(expressionSecond)
        except Exception as e:
            return('Wrong')
        try:
            partThree, dividerThree, signThree = splitting(input_exp3)
        except Exception as e:
            return('Wrong')

        try:
            partOne = str(partOne)
            input1,input2,input3 = sympify(partOne.split('*'))
        except Exception as e:
            return('Wrong')
        try:
            partTwo = str(partTwo)
            input4,input5 = sympify(partTwo.split('*'))
        except Exception as e:
            return('Wrong')

        arr = set([input1,input2,input3,input4,input5])
        for value in arr:
            result = result * sympify(value)

        if((result == sympify(partThree)) and (gcd(sympify(dividerOne),sympify(dividerTwo)) == 1)
            and (dividerOne%3 == 0) and (statusFirst and statusSecond == 'Correct') ):
            status = True

        if (status == True):
            return('Correct')
        else:
            return('Wrong')
    #print(preLastCheck('(n-1)*n*(n + 1)#3 Correct; (n-1)*(n+1)#8 Correct; (n-1)*n*(n + 1)#24'))

    def finalCheck(input_exp): #n**3-n =(n-1)*n*(n + 1) Correct
                                                  #(n-1)*n*(n + 1)#24 Correct
                                                  # n**3-n#24
        status = False
        try:
             input_exp1, input_exp2, input_exp3  = input_exp.split(';')
        except Exception as e:
            return('Exception')  # later need to change


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
            return('Wrong')  # later need to change
        try:
            expressionFirst, statusFirst = splitFinal(input_exp1)
        except Exception as e:
            return('Wrong')  # later need to change

        try:
            part1,part2,sign = splitting(input_exp2)
        except Exception as e:
            return('Wrong')

        expressionFirst = str(expressionFirst)
        part1 = str(part1)
        part2 = str(part2)

        expressionFirst = expressionFirst.replace(part1, part2)
        return(expressionFirst)

    def checkInequalities(input_exp): # a>b; a+c > b+c                   3<=5 Correct; 5 >=3
        status =False
        print('hereee')
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

        subtractionFirst = (leftPartOne) - (rightPartOne)
        subtractionSecond = (leftPartTwo) - (rightPartTwo)

        print(leftPartOne, type(leftPartOne))

        divisionLeft = leftPartOne / rightPartOne
        divisionRight = leftPartTwo / rightPartTwo

        if((subtractionFirst == subtractionSecond) 
            and ((signOne == signTwo) and (signOne != '=')) ):
            status = True
        elif((divisionLeft ==divisionRight) ):
            status = True
        elif((leftPartOne == rightPartTwo) and (rightPartOne == leftPartTwo)
            and  (signOne!= signTwo)):
            status = True
        elif((leftPartOne == 1/leftPartTwo) and (rightPartOne == 1/ rightPartTwo) 
            and  (signOne!= signTwo)):
            status = True

        if statusFirst == 'Correct':
            if status == True:
                return('Correct')
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
        #lemma 12
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
            if((statusFirst == statusSecond == 'Correct')  or (leftPartOne/leftPartTwo == leftPartThree) or ((leftPartTwo/leftPartOne == leftPartThree))):
                if(signOne == signTwo and signThree == '>'): #and ((simplify(input_exp3) == True)
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

        print(leftMul, rightMul)
        #lemma18
        if(signOne == signTwo == signThree == signFour == '>'): # and simplify(input_exp4) == True

            if(sympify(left) == sympify(leftPartFour) and sympify(right) == sympify(rightPartFour)):
                status = True

            elif(sympify(leftMul) == sympify(leftPartFour) and sympify(rightMul) == sympify(rightPartFour)):
                status = True

        if status == True:
                return('Correct')
        return('Wrong')
    def powerInequality(input_exp):
        status = False
        checked = False
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

        baseArray,powerArray = findPower(input_exp2)
        for i in range(len(powerArray) - 1):
            if(powerArray[i] == powerArray[i+1]):
                checked = True

        if(signOne == signTwo and checked == True):
            if(leftPartOne == baseArray[0] and rightPartOne == baseArray[1]):
                status = True

        if status == True:
            return('Correct!')
        return('Wrong')
    #print(powerInequality('x>y Correct; x**n > y**n'))
