from __future__ import division
from copy import copy
import Base

"""
    Module for key operations on Python lists or FoxDot Patterns
"""

#: The following return operand patterns

class POperand:

    def __init__(self, func):
        
        self.operate = func

    def __call__(self, A, B):

        # Multiple patterns

        pat1, pat2 = self.setup(A, B)

        for i, item in pat1.items():

            try:

                # Perform the operation

                pat1[i] = self.operate(item, pat2[i])

            except ZeroDivisionError:

                # Numbers divided by 0 are set to 0

                pat1[i] = 0

        return pat1

    @staticmethod
    def setup(A, B):
        """ Prepares two Patterns, A & B, for correct use in operands"""
        #A, B = copy(A), copy(B)
        cls = Base.Dominant(A, B)

        A, B = cls(A), cls(B)

        length = LCM(len(A), len(B))

        A.stretch(length)
        B.stretch(length)
        
        return A, B

# General operations
Nil  = lambda a, b: a
Add  = lambda a, b: a + b
Sub  = lambda a, b: a - b
Mul  = lambda a, b: a * b
Div  = lambda a, b: a / b
Mod  = lambda a, b: a % b
Pow  = lambda a, b: a ** b
rDiv = lambda a, b: b / a
rSub = lambda a, b: b - a
rMod = lambda a, b: b % a

# Pattern operations
PAdd = POperand(Add)
PSub = POperand(Sub)
PMul = POperand(Mul)
PDiv = POperand(Div)
PMod = POperand(Mod)
PPow = POperand(Pow) # a ^ b also calls this



# --- Cases
#
#       [0,1] + 2 = [2,3]
#       (0,1) + 2 = (2,3)
#
#   [0,1] + [2,3] = [2,4]
#   [0,1] + (2,3) = [(2,3),(3,4)] -> [0,1] + [(2,3)] = [(2,3),(3,4)]
#
#   (0,1) + (2,3) = (2,4)
#   (0,1) + [2,3] = [(2,3),(3,4)]
#
#  [(0,1),2] + 3  = [(3,4),5]
#
#
#

#: Misc. Operations

def LCM(*args):
    """ Lowest Common Multiple """
    # Base case
    if len(args) == 1: return args[0]

    X = list(args)
    
    while any([X[0]!=K for K in X]):

        i = X.index(min(X))
        X[i] += args[i]        

    return X[0]

def patternclass(a, b):
    return Base.PGroup if isinstance(a, Base.PGroup) and isinstance(b, Base.PGroup) else Base.Pattern


def modi(array, i, debug=0):
    """ Returns the modular index i.e. modi([0,1,2],4) will return 1 """
    try:
        return array[i % len(array)]
    except:        
        return array

def max_length(*patterns):
    """ Returns the largest length pattern """
    return max([len(p) for p in patterns])  


