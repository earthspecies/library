import numpy as np
import pandas as pd
import torch

class ShowType():
    # Initial version 20190504 Malcolm McLean

    def __init__(self, width=4):
        self._width = width  #Traverse lists only this far

    def type_str(self, o):  # generate a string that tells us the type and dimensions of o.
        def getLastWord(s):
            ix = s.rfind('.')
            return s if (ix == -1) else s[1 + ix:]

        ts = getLastWord(type(o).__name__)  #The base type name
        rs = ts              # starts the result string

        if hasattr(o, 'shape'):
            if ts == 'Tensor':
                rs += '('+str(o.device)+')'  #Append the device

            rs += str([d for d in o.shape]) #Append the shape dimensions in square brackets

            if ts=='DataFrame':  #List column names and their types
                rs += '<'
                for col, cte in zip(o.columns, o.dtypes):
                    rs += col + '<' + str(cte) + '> '
                rs += '>'
            elif ts=='Series':
                rs = rs+'<'+str(o.dtype)+'>' #Its type
            else:
                rs += '<'+getLastWord(str(o.dtype)) + '>' #If o has a shape, assume elements are homogeneous, append element type.

        elif hasattr(o, '__len__'):
            if (rs == 'str'): return rs  # String has a length but will not be disassembled further

            #o is likely to be a Python tuple or list.
            rs += '['+str(len(o)) + ']' #append the length
            #Show width members of the contents recursively.
            if len(o)>0:
                rs += '<'
                for i,m in enumerate(o):
                    if (i>=self._width): break
                    if i!=0: rs += ', '
                    rs += self.type_str(m)

                if i>=self._width:   #Were there more elements?
                    rs += ',...'
                rs+= '>'            #Close the list of elements

        return rs


# Python Tuple
# -length
# -anything
#
# Python list
#  -length
#  -anything
#
# Python function
#
# Numpy
#  - shape
#  - homogeneous
#  - len yields 1st dimension
#  - a.dtype
#
# PyTorch
#  -shape
#  -homgeneous, t.type()
#  -len
#  -device
#
# Pandas DataFrame
#  -shape
#  -columns,dtypes
#
#  Pandas Series
#  -shape
#  -dtype
#
