def calc(f_no,operand,l_no):
    if op == '+':
        return f_no + l_no
    elif op == '-':
        return f_no - l_no
    elif op == '*':
        return f_no * l_no
    elif op == '/':
        return f_no / l_no
    else:
        return "Wrong operand"


should_continue = 'y'
while(should_continue == 'y'):
    fno = int(input("Enter the 1st no: "))
    op = input("Enter the operator \n +\n-\n*\n/\n")
    lno = int(input("Enter the 2nd no: "))
    print(calc(fno,op,lno))
    should_continue = input("Do you want to continue y/n")

