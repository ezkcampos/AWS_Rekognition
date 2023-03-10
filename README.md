
# Detecção de Preços em Imagens

Este é um código Python que usa a biblioteca boto3 para se conectar à API Rekognition da AWS e detectar preços em imagens.





## Pré-requisitos

Antes de executar este código, você precisará:
- Uma conta AWS com acesso à API Rekognition
- Credenciais da AWS em um arquivo credentials.csv
- Python 3.x instalado em seu computador
- As bibliotecas Python boto3, csv, openpyxl e re instaladas em seu ambiente Python.

## Como Usar
- Clone este repositório em seu computador
- Abra um terminal ou prompt de comando e navegue até a pasta onde você clonou o repositório
- Execute o seguinte comando: python detect_preco.py
- Se o programa encontrar preços válidos na imagem, ele exibirá uma lista deles na tela. Caso contrário, exibirá uma mensagem informando que não foram encontrados preços válidos na foto.

## Como Funciona
Este programa faz o seguinte:
- Cria um cliente da API Rekognition da AWS, lendo as credenciais do arquivo credentials.csv
- Converte uma imagem em um array de bytes
- Usa o cliente para detectar texto na imagem
- Verifica o texto detectado e armazena os preços válidos em uma lista
- Exibe os preços válidos detectados
- O programa usa expressões regulares para identificar preços em formato brasileiro (por exemplo, "R$ 10,50").