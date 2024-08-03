import json
import subprocess

subprocess.run(["python", "parsers/imobiliaria.py"], check=True)

with open("gen/imobiliaria.json", encoding="utf-8") as json_file:
    data = json.load(json_file)

while (True):
    print("\n" + "="*10 + " IMOBILIARIA " + "="*10 + "\n")

    imoveis = data['imobiliaria']['imovel']
    for imovel in imoveis:
        imovel_id = imovel['id']
        descricao = imovel['descricao']
        print(f"{imovel_id}. {descricao}")
    print("\n0. Encerrar")

    terminal = input("\n Digite uma opção: ")
    if terminal == "0":
        break

    for imovel in imoveis:
        imovel_id = str(imovel['id'])
        if terminal == imovel_id:
            print("")
            descricao = imovel['descricao']
            print("="*10 + f" {descricao} " + "="*10 + "\n")

            proprietario = imovel['proprietario']
            print("Proprietario")
            nome = proprietario['nome']
            print(f"  Nome: {nome}")

            email = proprietario.get('email')
            if email:
                print(f"  Email: {email}")

            telefones = proprietario.get('telefones', [])
            if telefones:
                print("  Telefones")
                for telefone in telefones:
                    print(f"    {telefone}")

            endereco = imovel['endereco']
            print("\nEndereço")
            print(f"  Cidade: {endereco['cidade']}")
            print(f"  Bairro: {endereco['bairro']}")
            print(f"  Rua: {endereco['rua']}")
            print(f"  Número: {endereco['numero']}")

            caracteristicas = imovel['caracteristicas']
            print("\nCaracteristicas")
            print(f"  Tamanho: {caracteristicas['tamanho']} m²")
            print(f"  Número de Quartos: {caracteristicas['numQuartos']}")
            print(f"  Número de Banheiros: {caracteristicas['numBanheiros']}")

            valor = imovel['valor']
            print(f"\nValor: R${valor}")
            terminal = input("\nEnter. Voltar ao menu \n")