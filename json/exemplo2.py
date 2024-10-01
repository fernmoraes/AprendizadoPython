import json

contatos = {
    'mariana': {'telefone': '12998756861', 'email': 'mariana@gmaul.com'},
    'clovis': {'telefone': '11991445858', 'email': 'clovis@gmaul.com'}
}

# dump serve para converter em str
# indent serve para identar o arquivos json
# ensure_ascii serve para incluir caracteres especiais

with open('contatos.json', 'w', encoding='utf-8') as arquivo:
    json.dump(contatos, arquivo, indent=4, ensure_ascii=False)


