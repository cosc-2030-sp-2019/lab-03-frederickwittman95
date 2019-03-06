
# coding: utf-8

# In[64]:


# Frederick Wittman
# Dr Robin Hill
# COSC 2030-01
# Lab 03
# 04 March 2019

import operator
import math
ops = {
    '+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv,
    '^':operator.pow,
    'neg':operator.neg
}

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    
def calculate(exp):
    stack = []
    stack1 = []
    result = 0

    # Load the elements of "exp", in order, into stack[]
    for i in exp:
        stack.append(i)
    
    # While stack[] is not empty, pop elements off stack[] and append them to stack1[] if they are numbers
    while len(stack) != 0:
        tmp = stack.pop()
        if is_number(tmp):
            stack1.append(tmp)
        else:
                
    # Implementation of unary operators.  
            if tmp == 'neg':
                print ('stack: ', stack1, 'where operation is', tmp)
                operand1 = float(stack1.pop())
                result = ops[tmp](operand1)
                stack1.append(result)
            elif tmp == 'sqrt':
                print ('stack: ', stack1, 'where operation is', tmp)
                operand1 = float(stack1.pop())
                result = math.sqrt(operand1)
                stack1.append(result)
                
    # If a binary operator is encountered before two elements have been appended to stack1[], print an error message
            elif len(stack1) < 2:
                print ('Error: insufficient values in expression')
                break
                
    # Binary operations.  Note that the stack prints backwards
            else:
                print ('stack: ', stack1, 'where operation is ', tmp)
                operand1 = float(stack1.pop())
                operand2 = float(stack1.pop())
                result = ops[tmp](operand1, operand2)
                stack1.append(result)
                
    return result

print ("Start of Polish Notation Evaluator")
exp_file = open("test.txt", 'r')
for line in exp_file:
        exp_list = line.rstrip().split(' ')
        answer = calculate(exp_list)
        print ('RESULT: %f' % answer)
print ("End of Polish Notation Evaluator")

