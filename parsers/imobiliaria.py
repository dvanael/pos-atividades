from xml.dom.minidom import parse
import json

dom = parse("xsd/imobiliaria.xml")
imobiliaria_xml = dom.documentElement
imoveis = imobiliaria_xml.getElementsByTagName("imovel")

lista_imoveis = []

number = 1
for imovel in imoveis:
    imovel_data = {}

    imovel_data['id'] = number
    number += 1

    descricao = imovel.getElementsByTagName("descricao")[0].firstChild.nodeValue
    imovel_data['descricao'] = descricao

    proprietario = imovel.getElementsByTagName("proprietario")[0]
    nome_proprietario = proprietario.getElementsByTagName("nome")[0].firstChild.nodeValue
    imovel_data['proprietario'] = {'nome': nome_proprietario}

    email = proprietario.getElementsByTagName("email")
    if email:
        lista_email = []
        imovel_data['proprietario']['email'] = email[0].firstChild.nodeValue

    telefones = proprietario.getElementsByTagName("telefone")
    if telefones:
        lista_telefones = []
        for telefone in telefones:
            lista_telefones.append(telefone.firstChild.nodeValue)
        imovel_data['proprietario']['telefones'] = lista_telefones

    endereco = imovel.getElementsByTagName("endereco")[0]
    rua = endereco.getElementsByTagName("rua")[0].firstChild.nodeValue
    bairro = endereco.getElementsByTagName("bairro")[0].firstChild.nodeValue
    cidade = endereco.getElementsByTagName("cidade")[0].firstChild.nodeValue

    numero = endereco.getElementsByTagName("numero")
    if numero:
        numero = numero[0].firstChild.nodeValue
    else:
        numero = "Sem número"

    imovel_data['endereco'] = {
        'rua': rua,
        'bairro': bairro,
        'cidade': cidade,
        'numero': numero
    }

    caracteristicas = imovel.getElementsByTagName("caracteristicas")[0]
    tamanho = caracteristicas.getElementsByTagName("tamanho")[0].firstChild.nodeValue
    num_quartos = caracteristicas.getElementsByTagName("numQuartos")[0].firstChild.nodeValue
    num_banheiros = caracteristicas.getElementsByTagName("numBanheiros")[0].firstChild.nodeValue
    imovel_data['caracteristicas'] = {
        'tamanho': tamanho,
        'numQuartos': num_quartos,
        'numBanheiros': num_banheiros
    }

    valor = imovel.getElementsByTagName("valor")[0].firstChild.nodeValue
    imovel_data['valor'] = valor

    lista_imoveis.append(imovel_data)

imobiliaria_json = {
    "imobiliaria": {
        "imovel": lista_imoveis
    }
}

with open("gen/imobiliaria.json", "w", encoding="utf-8") as json_file:
    json.dump(imobiliaria_json, json_file, indent=2, ensure_ascii=False)