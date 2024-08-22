print("For Addition Enter ' + '\nFor Subtraction Enter ' - '\nFor Multiplecation Enter ' * '\nFor division Enter ' / '\nFor Floor-Division Enter ' // '");
operator = input("Enter operator: ");

x = int(input("Enter num-1: "));
y = int(input("Enter num-2: "));


if operator == "+":
    print(f"{x} + {y} = {x + y}");
    
if operator == "-":
    print(f"{x} - {y} = {x - y}");
    
if operator == "*":
    print(f"{x} * {y} = {x * y}");
    
if operator == "/":
    print(f"{x} / {y} = {x / y}");
    
if operator == "//":
    print(f"{x} // {y} = {x // y}");
