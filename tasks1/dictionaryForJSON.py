import json

name = input("Digite o nome: ")
age = int(input("Digite a idade: "))
city = input("Digite a cidade: ")

data = {"name": name, "age": age, "city": city}


with open("data.json", "a") as file:
    json.dump(data, file)