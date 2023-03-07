import csv
# biblioteca que se conecta com a AWS
import boto3
import openpyxl
from pprint import pprint
import re

# Cria um cliente da AWS lendo as credenciais do arquivo credentials.csv
with open('C:/Users/ezequ/Desktop/UNICARIOCA/1TCC/AWS/credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

# Usa a foto
photo = "C:/Users/ezequ/Desktop/IBRE/AWS_REKOGNITION/preco1.jpg"


# Cria o cliente
client = boto3.client('rekognition',
                      aws_access_key_id=access_key_id,
                      aws_secret_access_key=secret_access_key,
                      region_name='us-east-1')

# Converte uma imagem em um array de bytes
with open(photo, 'rb') as source_image:
    source_bytes = source_image.read()

# Usa o cliente para detectar o texto na imagem
text_response = client.detect_text(Image={'Bytes': source_bytes})

# Expressão regular para identificar preços
preco_regex = r'\d+\,\d{2}'

# Lista para armazenar preços válidos
precos_validos = []

# Verifica o texto detectado e armazena os preços válidos na lista
if len(text_response["TextDetections"]) > 0:
    for text in text_response['TextDetections']:
        if text['Type'] == 'LINE':
            preco_match = re.search(preco_regex, text['DetectedText'])
            if preco_match:
                preco = float(preco_match.group(0).replace(',', '.'))
                precos_validos.append(preco)

# Exibe os preços válidos detectados
if precos_validos:
    print("Preços válidos detectados:")
    for preco in precos_validos:
        print(f"R$ {preco:.2f}")
else:
    print("Não foram encontrados preços válidos na foto.")

