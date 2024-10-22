import requests

cep = input('DIGITE O CEP: ')
response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

if response.status_code == 200:
    dicionario = response.json()

    if 'erro' in dicionario:
        print('CEP inexistente')

print(response.status_code)