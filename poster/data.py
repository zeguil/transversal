import requests
from decouple import config
from translate import Translator
from time import sleep

def obter_clima(cidade):
    chave_api = 'ebe9323dd4d66a4bb1b75ea1fc85302c'
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric"
        resposta = requests.get(url)
        print(resposta.status_code)
        dados_clima = resposta.json()
        print(dados_clima)
        # Verifica se a chave 'main' está presente nos dados do clima
        if 'main' not in dados_clima:
            print("Erro: 'main' não encontrado nos dados do clima")
            return None

        temperatura = int(dados_clima['main']['temp'])
        sensacao_termica = int(dados_clima['main']['feels_like'])
        umidade = dados_clima['main']['humidity']
        velocidade_vento = dados_clima['wind']['speed']
        descricao_tempo = dados_clima['weather'][0]['description']
    
    except Exception as e:
        print(f"ERRO: {e}")

    translator = Translator(to_lang='pt')
    descricao_tempo = translator.translate(descricao_tempo)
    if descricao_tempo.lower() == "nuvens partidas":
        descricao_tempo = "Nuvens dispersas"

    if descricao_tempo.lower() == "nuvens nubladas":
        descricao_tempo == "Céu nublado"

    dados_clima = {
        "cidade" : cidade,
        'descricao_tempo': descricao_tempo.capitalize(),
        'temperatura': temperatura,
        'sensacao_termica': sensacao_termica,
        'umidade': umidade,
        'velocidade_vento': (f'{velocidade_vento} km/h')
    }

    return dados_clima

def obter_qualidade_ar(cidade):
    estado = ""
    if cidade == "Manaus":
        estado = "Amazonas"
    elif cidade == "Sao Paulo":
        estado = "Sao Paulo"
    elif cidade == "Curitiba":
        estado = "Parana" 
    elif cidade == "Recife":
        estado = "Pernambuco"
    elif cidade == "Rio Branco":
        estado = "Acre"
    elif cidade == "Brasilia":
        estado = "Federal Distric"
    elif cidade == "Palmas":
        estado = "Tocantins"
    elif cidade == "Santarem":
        estado = "Para"

    cidade_formatada = cidade.replace(" ", "%20")

    estado_formatado = estado.replace(" ", "%20")

    api_key = '2bc993ef-b477-4921-a92c-6f4befc22ffe'
    headers = {'Content-Type': 'application/json'}
    url = f"https://api.airvisual.com/v2/city?city={cidade_formatada}&state={estado_formatado}&country=Brazil&key={api_key}"
    response = requests.get(url, headers=headers)

    resultado = {}

    if response.status_code == 200:
        response_data = response.json()
        city_name = response_data['data']['city']
        aqius = response_data['data']['current']['pollution']['aqius']
        mainus = response_data['data']['current']['pollution']['mainus']

        if aqius <= 20:
            status = "Ótimo"
        elif 21 <=aqius <= 50:
            status = "Bom"
        elif 51 <= aqius <= 100:
            status = "Moderado"
        elif 101 <= aqius <= 150:
            status = "Não Saudável para Grupos Sensíveis"
        elif 151 <= aqius <= 200:
            status = "Não Saudável"
        elif 201 <= aqius <= 300:
            status = "Muito Não Saudável"
        else:
            status = "Perigoso"

        mainus_sig = {
            'p1': "Indica partículas finas (PM1.0), com diâmetro aerodinâmico menor ou igual a 1.0 micrômetros.Podem ser inaladas profundamente nos pulmões, mas geralmente representam menos risco à saúde.",
            'p2': "Indica partículas finas (PM2.5), com diâmetro aerodinâmico menor ou igual a 2.5 micrômetros. Podem ser inaladas profundamente nos pulmões e representam um risco maior à saúde do que as PM1.0.",
            'pm10': "Indica partículas inaláveis (PM10), com diâmetro aerodinâmico menor ou igual a 10 micrômetros. Podem ser inaladas, mas são menos propensas a entrar profundamente nos pulmões do que as PM2.5.",
            'co': "Indica monóxido de carbono. O CO é um gás tóxico que pode ser inalado e entrar na corrente sanguínea, reduzindo a capacidade do sangue de transportar oxigênio.",
            'so2': "Indica dióxido de enxofre. O SO2 é um gás irritante que pode ser inalado e causar problemas respiratórios, especialmente em pessoas com condições pulmonares pré-existentes.",
            'o3': "Indica ozônio. O ozônio no nível do solo é um poluente atmosférico prejudicial à saúde humana quando inalado. Pode causar irritação nos olhos, nariz e garganta, e a exposição a níveis elevados pode piorar condições respiratórias existentes.",
            'desconhecido': "Valor desconhecido."
        }

        if estado == "Federal Distric":
            estado = "Distrito Federal"
        resultado['cidade'] = city_name
        resultado['estado'] = estado
        resultado['iqa'] = aqius
        resultado['poluente'] = mainus
        resultado['status'] = status
        resultado['poluente_sig'] = mainus_sig.get(mainus, mainus_sig['desconhecido'])

    else:
        resultado['error'] = f"Falha na solicitação. Código de status: {response.status_code}\n Não achei {cidade}"
        print(response.json())

    return resultado

def main():
    contador = 0
    while True:
        cidades = ["Manaus", "Sao Paulo", "Curitiba", "Recife", "Rio Branco", "Palmas", "Santarem"]

        for cidade in cidades:
            print(f"\n### CADASTRANDO {cidade.upper()} ###")
            clima = obter_clima(cidade)
            sleep(2)
            iqa = obter_qualidade_ar(cidade)
            clima.update(iqa)
            sleep(5)
            url = "http://localhost:8080/dados_climaticos/create"

            try:
                # Enviando solicitação POST
                response = requests.post(url, json=clima)

                # Verificando se a solicitação foi bem-sucedida
                if response.status_code == 200:
                    print("- Dados climáticos enviados com sucesso!")
    
            except Exception as e:
                print(f"Erro ao enviar dados climáticos. {e}")

            sleep(5)

        contador += 1
        print(f"#{contador}#")
        if contador % 3 == 0:
            url = "http://localhost:8080/dados_climaticos/delete/1"
            try:
                response = requests.delete(url)
                if response.status_code == 200:
                    print("- Dados climáticos deletados com sucesso!")

            except Exception as e:
                print(f"Erro ao deletar dados climáticos. {e}")
        sleep(100)

if __name__ == "__main__":
    main()