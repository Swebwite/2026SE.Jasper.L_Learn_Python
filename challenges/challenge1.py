def main():
    num1 = int(input('First number?'))
    num2 = int(input('Second number?'))
    operator = input('Operator?')
    ui_output = ''
    if operator == '-':
        ui_output = num1 - num2
    elif operator == '+':
        ui_output = num1 + num2
    elif operator == '*':
        ui_output = num1 * num2
    elif operator == '/':
        ui_output = num1 / num2
    else:
        ui_output = 'Not a known operator'
    print(ui_output)
main()
