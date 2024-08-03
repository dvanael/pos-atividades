from xml.dom.minidom import parse

dom = parse("xsd/cardapio.xml")
cardapio = dom.documentElement
pratos = cardapio.getElementsByTagName("prato")

while (True):
  print("\n" + "="*10 + " CARDAPIO " + "="*10 + "\n")
  for prato in pratos:
    prato_id = prato.getAttribute("id")
    prato_nome = prato.getElementsByTagName("nome")[0]
    nome = prato_nome.firstChild.nodeValue
    print(f"{prato_id}. {nome}")
  print("0. Encerrar")

  terminal = input("\n Digite uma opção: ")
  if terminal == "0":
    break

  for prato in pratos:
    prato_id = prato.getAttribute("id")
    if terminal == prato_id:
      print("")
      prato_nome = prato.getElementsByTagName("nome")[0]
      nome = prato_nome.firstChild.nodeValue
      print("="*10 + f" {nome} " + "="*10 + "\n")

      prato_descricao = prato.getElementsByTagName("descricao")[0]
      descricao = prato_descricao.firstChild.nodeValue
      print(f"{descricao} \n")

      ingredientes = prato.getElementsByTagName("ingrediente")
      print("Ingredientes")

      numeracao = 1
      for ingrediente in ingredientes:
        ingrediente_nome = ingrediente.firstChild.nodeValue
        print(f"  {numeracao}. {ingrediente_nome}")
        numeracao += 1
      print("")

      prato_preco = prato.getElementsByTagName("preco")[0]
      preco = prato_preco.firstChild.nodeValue
      print(f"Preço: {preco}")

      prato_calorias = prato.getElementsByTagName("calorias")[0]
      calorias = prato_calorias.firstChild.nodeValue
      print(f"Calorias: {calorias}")

      prato_tempoPreparo = prato.getElementsByTagName("tempoPreparo")[0]
      tempoPreparo = prato_tempoPreparo.firstChild.nodeValue
      print(f"Tempo de Preparo: {tempoPreparo}")

      terminal = input("\nEnter. Voltar ao menu \n")