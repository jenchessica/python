def evaluate(arr):
    stack = []
    for i in range (0, len(arr)):
        if arr[i] == "+":
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operand1+operand2)
        elif arr[i] == "-":
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operand1-operand2)
        elif arr[i] == "*":
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operand1*operand2)
        elif arr[i] == "/":
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operand1/operand2)
        else:
            stack.append(arr[i])

    if len(stack)==1:
        return stack[0]
    else:
        return "dis bad :("

def thatscrazy(arr):
    stack = []
    for i in range (0, len(arr)):
        if arr[i] == "+":
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append("(" + str(operand1) + "+" + str(operand2) + ")")
        elif arr[i] == "-":
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append("(" + str(operand1) + "-" + str(operand2) + ")")
        elif arr[i] == "*":
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append("(" + str(operand1) + "*" + str(operand2) + ")")
        elif arr[i] == "/":
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append("(" + str(operand1) + "/" + str(operand2) + ")")
        else:
            stack.append(arr[i])

    if len(stack)==1:
        return stack[0]
    else:
        return "dis bad :("

postfix=[9, 3, 2, "+", 5, "*", 4, "-", "-"]

result=evaluate(postfix)
expression=thatscrazy(postfix)

print(expression + "=")
print(result)
