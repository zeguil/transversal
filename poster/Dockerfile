# Use a imagem oficial do Python 3.9
FROM python:3.10

# Define o diretório de trabalho no contêiner
WORKDIR /

# Copia todo o conteúdo da pasta poster/ para o diretório de trabalho no contêiner
COPY . .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para executar o bot quando o contêiner for iniciado
CMD ["python", "data.py"]
