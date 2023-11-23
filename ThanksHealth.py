def validar_entrada(entrada):
    while True:
        if entrada.replace('.', '', 1).isdigit() or (entrada[0] == '-' and entrada[1:].replace('.', '', 1).isdigit()):
            return True
        else:
            entrada = input("Entrada inválida. Por favor, insira um valor numérico: ")
def coletar_registros():
    registros = []

    while True:
        valor = input("Insira um valor médico (ou 's' para sair): ")

        if valor.lower() == 's':
            break

        validar_entrada(valor)

        registros.append(float(valor))
        print("Registro adicionado com sucesso.")

    return registros
def calcular_soma(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma
def processar_dados(registros):
    total_registros = len(registros)
    soma_valores = calcular_soma(registros)
    media_valores = soma_valores / total_registros if total_registros > 0 else 0
    return total_registros, soma_valores, media_valores
def apresentar_resultados(total, soma, media):
    print(f"\nTotal de Registros: {total}")
    print(f"Soma dos Valores: {soma}")
    print(f"Média dos Valores: {media:.2f}")
def main():
    print("Bem-vindo ao ThanksHealth - Otimizando a Gestão de Registros Médicos Eletrônicos\n")
    registros = coletar_registros()
    total, soma, media = processar_dados(registros)
    apresentar_resultados(total, soma, media)

if __name__ == "__main__":
    main()
