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
        status = False
        newStr = str(input_exp)
        try:
            part1, part2,part3 = newStr.split('*')
        except Exception as e:
            return('Exception')  # later need to change

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
