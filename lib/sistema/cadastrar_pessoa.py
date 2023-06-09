import time
import datetime
import random
import requests
from db.cadastrar import cadastrar
from lib.interface import cabecalho,linha


def validar_cpf(cpf):
    # Remover os pontos e traços do CPF
    cpf = cpf.replace(".", "").replace("-", "")
    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    # Verificar se todos os dígitos do CPF são iguais
    if cpf == cpf[0] * 11:
        return False
    # Calcular o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto
    # Calcular o segundo dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (11 - i)
    soma += digito1 * 2
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto
    # Verificar se os dígitos verificadores são válidos
    if cpf[-2:] == str(digito1) + str(digito2):
        return True
    else:
        return False


def gerar_matricula():
    data_atual = datetime.datetime.now()
    data_formatada = data_atual.strftime('%Y%m%d')
    numero_aleatorio = random.randint(10, 99)
    matricula = f"{data_formatada}{numero_aleatorio}"
    return matricula


def cadastrar_pessoa():
    global data
    cabecalho("CADASTRAR PESSOA")

    matricula = gerar_matricula()
    nome = input("- Digite o nome da pessoa: ")
    celular = input("- Digite o celular: ")
    email = input("- Digite o email: ")
    data_nasc = input("- Digite a data de nasc.: ")
    sexo = input("- Digite o sexo: ")
    cpf = input("- Digite o CPF: ")
    cpf = cpf.replace(".", "").replace("-", "")

    cep = input("- Digite o CEP: ")

    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

    if validar_cpf(cpf):
        cadastrar(matricula, nome, celular, email, data_nasc, sexo, cpf, data)
        print(linha())
        print("Pessoa cadastrada com sucesso!")
        time.sleep(1)
    else:
        print('CPF inválido!')
        return cadastrar_pessoa()
