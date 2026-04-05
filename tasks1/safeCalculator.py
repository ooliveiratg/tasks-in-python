
def safe_calculator():
    try:
        input1 = int(input("Digite o primeiro número: "))
        input2 = int(input("Digite o segundo número: "))
        operation = input1/input2
        print("Resultado: ", operation)
    except: 
        print("Deu erro.")
safe_calculator()