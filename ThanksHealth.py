import json
from datetime import datetime

consultas_agendadas = []

def is_numeric(entrada):
    return entrada.replace('.', '', 1).isdigit() or (entrada[0] == '-' and entrada[1:].replace('.', '', 1).isdigit())

def validar_entrada(entrada):
    while not is_numeric(entrada):
        entrada = input("Entrada inválida. Por favor, insira um valor numérico: ")

    return float(entrada)

def calcular_idade(data_nascimento):
    partes = data_nascimento.split('/')
    if len(partes) != 3 or not all(is_numeric(p) for p in partes):
        return None

    hoje = datetime.today()
    data_nascimento = datetime(int(partes[2]), int(partes[1]), int(partes[0]))

    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

def agendar_consulta():
    data = input("Insira a data da consulta (formato DD/MM/AAAA): ")
    hora = input("Insira a hora da consulta (formato HH:MM): ")

    # Verificar se a data é a partir de novembro de 2023
    partes_data = data.split('/')
    if len(partes_data) != 3 or not all(is_numeric(p) for p in partes_data):
        print("Formato de data inválido. Consulta não agendada.")
        return

    if not (int(partes_data[2]) == 2023 and int(partes_data[1]) >= 11):
        print("Só é possível agendar consultas a partir de novembro de 2023. Consulta não agendada.")
        return

    # Verificar se o horário está disponível
    for consulta in consultas_agendadas:
        if consulta['data'] == data and consulta['hora'] == hora:
            print("Horário indisponível. Por favor, escolha outro horário.")
            return

    paciente = input("Insira o nome do paciente: ")
    data_nascimento = input("Insira a data de nascimento do paciente (formato DD/MM/AAAA): ")
    idade = calcular_idade(data_nascimento)
    tipo_consulta = input("Insira o tipo de consulta: ")

    # Solicitar todas as informações necessárias para o paciente
    telefone = input("Insira o número de telefone do paciente: ")
    endereco = input("Insira o endereço do paciente: ")
    # Adicione mais campos conforme necessário

    consultas_agendadas.append({
        'data': data,
        'hora': hora,
        'paciente': paciente,
        'data_nascimento': data_nascimento,
        'idade': idade,
        'tipo_consulta': tipo_consulta,
        'telefone': telefone,
        'endereco': endereco,
        # Adicione mais campos conforme necessário
    })

    # Exibir todos os dados do paciente
    print("\nDados do Paciente:")
    print(f"Nome: {paciente}")
    print(f"Data de Nascimento: {data_nascimento}")
    print(f"Idade: {idade}")
    print(f"Tipo de Consulta: {tipo_consulta}")
    print(f"Telefone: {telefone}")
    print(f"Endereço: {endereco}")
    # Adicione mais campos conforme necessário
    print(f"\nConsulta agendada para {data} às {hora}.")

def visualizar_consultas():
    print("\nConsultas Agendadas:")
    for consulta in consultas_agendadas:
        idade = consulta.get('idade', 'N/A')
        print(f"{consulta['data']} às {consulta['hora']} - Paciente: {consulta['paciente']} - Idade: {idade} - Tipo de Consulta: {consulta['tipo_consulta']}")

def buscar_paciente_por_nome():
    nome_paciente = input("Insira o nome do paciente: ")
    encontrado = False

    for consulta in consultas_agendadas:
        if consulta['paciente'].lower() == nome_paciente.lower():
            print("\nDados do Paciente:")
            print(f"Nome: {consulta['paciente']}")
            print(f"Data de Nascimento: {consulta['data_nascimento']}")
            print(f"Idade: {consulta['idade']}")
            print(f"Tipo de Consulta: {consulta['tipo_consulta']}")
            print(f"Telefone: {consulta['telefone']}")
            print(f"Endereço: {consulta['endereco']}")
            # Adicione mais campos conforme necessário
            encontrado = True

    if not encontrado:
        print(f"Paciente '{nome_paciente}' não encontrado.")

# Restante do código permanece inalterado

def main():
    while True:
        opcao = input("\nEscolha uma opção:\n1 - Agendar nova consulta\n2 - Visualizar consultas agendadas\n3 - Buscar paciente por nome\n4 - Sair\nOpção: ")

        if opcao == '1':
            agendar_consulta()
        elif opcao == '2':
            visualizar_consultas()
        elif opcao == '3':
            buscar_paciente_por_nome()
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
