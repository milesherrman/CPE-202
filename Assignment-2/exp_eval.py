from Stacks import Stack

def infix_to_postfix(infixexpr: str) -> str:
    '''Converts an infix expression to an equivalent postfix expression'''
    stack = Stack(30)
    opStack = Stack(30)
    tokenList = infixexpr.split()
    postfixList = []
    
    for token in tokenList:
        try:
            float(token)
            postfixList.append(token)
        except:
            if token == "(":
                opStack.push(token)
            elif token == ")":
                while opStack.peek() != "(":
                    postfixList.append(opStack.pop())
                opStack.pop()
                
            elif token in "+-*/^":
                while True:
                    if opStack.size() == 0:
                        opStack.push(token)
                        break
                    elif check_precedence(token, opStack.peek()):
                        postfixList.append(opStack.pop())
                    else:
                        opStack.push(token)
                        break
    
    while opStack.size() > 0:
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

def check_precedence(op1: str, op2: str) -> bool:
    if op2 == "(":
        return False
    elif op2 == "^":
        if op1 == "^":
            return False
        return True
    elif op2 in "*/":
        if op1 != "^":
            return True
        return False
    elif op2 in "+-":
        if op1 in "*/^":
            return False
    return True

def postfix_eval(postfixExpr: str) -> float:
    """Evaluates and returns the value of a postfix expression"""
    if postfix_valid(postfixExpr) == False:
        raise ValueError
    tokenList = postfixExpr.split()
    valStack = Stack(30)
    for token in tokenList:
        try:
            float(token)
            valStack.push(token)
        except:    
            if token in "+-/*^":
                op2 = valStack.pop()
                op1 = valStack.pop()
                if token == "/" and op2 == "0":
                    raise ValueError
                else:
                    valStack.push(doMath(token,op1,op2))
    return valStack.pop()

def doMath(op: str, op1: str, op2: str) -> float:
    """Perform given mathmatical operation on two numbers"""
    if op == "+":
        return float(op1) + float(op2)
    elif op == "-":
        return float(op1) - float(op2)
    if op == "*":
        return float(op1) * float(op2)
    if op == "/":
        return float(op1) / float(op2)
    if op == "^":
        return float(op1) ** float(op2)

def postfix_valid(postfixexpr: str) -> bool:
    """Determines if a string consists of valid operands and operators"""
    valStack = Stack(20)
    tokenList = postfixexpr.split()
    if len(postfixexpr) < 5:
        return False
    if tokenList[0] in "+-/*^" or tokenList[1] in "+-/*^" or tokenList[len(tokenList) - 1] not in "+-/*^":
        return False 
    for token in tokenList:
        try:
            float(token)
            valStack.push(token)
        except:
            if token in "+-/*^":
                if valStack.size() == 0:
                    return False
                valStack.pop()
            else:
                return False
    if valStack.size() != 1:
        return False
    return True
    