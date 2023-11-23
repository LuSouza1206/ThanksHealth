import json

consultas_agendadas = []

def validar_entrada(entrada):
    while True:
        if entrada.replace('.', '', 1).isdigit() or (entrada[0] == '-' and entrada[1:].replace('.', '', 1).isdigit()):
            return True
        else:
            entrada = input("Entrada inválida. Por favor, insira um valor numérico: ")

def coletar_registros():
    registros = []

    while True:
        valor = input("Insira um valor médico (ou 's' para sair, 'a' para agendar consulta): ")

        if valor.lower() == 's':
            break
        elif valor.lower() == 'a':
            agendar_consulta()
        else:
            while not validar_entrada(valor):
                pass

            registros.append(float(valor))
            print("Registro adicionado com sucesso.")

    return registros

def agendar_consulta():
    data = input("Insira a data da consulta (formato DD/MM/AAAA): ")
    hora = input("Insira a hora da consulta (formato HH:MM): ")


    if not (int(data.split('/')[2]) == 2023 and int(data.split('/')[1]) >= 11):
        print("Só é possível agendar consultas a partir de novembro de 2023. Consulta não agendada.")
        return


    for consulta in consultas_agendadas:
        if consulta['data'] == data and consulta['hora'] == hora:
            print("Horário indisponível. Por favor, escolha outro horário.")
            return

    paciente = input("Insira o nome do paciente: ")
    tipo_consulta = input("Insira o tipo de consulta: ")

    consultas_agendadas.append({'data': data, 'hora': hora, 'paciente': paciente, 'tipo_consulta': tipo_consulta})
    print(f"Consulta agendada para {data} às {hora} com o paciente {paciente}, tipo de consulta: {tipo_consulta}.")

def visualizar_consultas():
    print("\nConsultas Agendadas:")
    for consulta in consultas_agendadas:
        print(f"{consulta['data']} às {consulta['hora']} - Paciente: {consulta['paciente']} - Tipo de Consulta: {consulta['tipo_consulta']}")

def salvar_consultas():
    with open('consultas.txt', 'w') as file:
        json.dump(consultas_agendadas, file)

def carregar_consultas():
    try:
        with open('consultas.txt', 'r') as file:
            consultas_agendadas.extend(json.load(file))
    except FileNotFoundError:
        pass

def main():
    carregar_consultas()

    while True:
        opcao = input("\nEscolha uma opção:\n1 - Registrar novo valor médico\n2 - Visualizar consultas agendadas\n3 - Sair\nOpção: ")

        if opcao == '1':
            registros = coletar_registros()
            visualizar_consultas()
        elif opcao == '2':
            visualizar_consultas()
        elif opcao == '3':
            salvar_consultas()
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()

def agendar_consulta():
    data = input("Insira a data da consulta (formato DD/MM/AAAA): ")
    hora = input("Insira a hora da consulta (formato HH:MM): ")


    if not (int(data.split('/')[2]) == 2023 and int(data.split('/')[1]) >= 11):
        print("Só é possível agendar consultas a partir de novembro de 2023. Consulta não agendada.")
        return


    for consulta in consultas_agendadas:
        if consulta['data'] == data and consulta['hora'] == hora:
            print("Horário indisponível. Por favor, escolha outro horário.")
            return

    paciente = input("Insira o nome do paciente: ")
    tipo_consulta = input("Insira o tipo de consulta: ")

    consultas_agendadas.append({'data': data, 'hora': hora, 'paciente': paciente, 'tipo_consulta': tipo_consulta})
    print(f"Consulta agendada para {data} às {hora} com o paciente {paciente}, tipo de consulta: {tipo_consulta}.")

def visualizar_consultas():
    print("\nConsultas Agendadas:")
    for consulta in consultas_agendadas:
        print(f"{consulta['data']} às {consulta['hora']} - Paciente: {consulta['paciente']} - Tipo de Consulta: {consulta['tipo_consulta']}")

def salvar_consultas():
    with open('consultas.txt', 'w') as file:
        json.dump(consultas_agendadas, file)

def carregar_consultas():
    try:
        with open('consultas.txt', 'r') as file:
            consultas_agendadas.extend(json.load(file))
    except FileNotFoundError:
        pass

def main():
    carregar_consultas()

    while True:
        opcao = input("\nEscolha uma opção:\n1 - Registrar novo valor médico\n2 - Visualizar consultas agendadas\n3 - Sair\nOpção: ")

        if opcao == '1':
            registros = coletar_registros()
            visualizar_consultas()
        elif opcao == '2':
            visualizar_consultas()
        elif opcao == '3':
            salvar_consultas()
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
