password = "1234"
password_input = ""
attempts = 0

while password_input != password:
    password_input = int(input("Digite a senha: "))
    with open("attempts.txt", "a") as file:
        file.write(f"Tentativa {attempts}: {password_input}\n")
        
    attempts += 1