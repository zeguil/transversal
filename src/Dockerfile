# Use a imagem oficial do Python 3.10
FROM python:3.10

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo do diretório atual para o diretório de trabalho no contêiner
COPY . .

# Comando para executar o aplicativo quando o contêiner for iniciado
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
