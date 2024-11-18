def mostrar_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}:{valor}")
mostrar_info(nome = 'Tiago', idade = 40, cidade = 'Fortaleza')        