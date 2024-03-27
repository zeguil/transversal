# TempAlert

TempAlert é uma aplicação web desenvolvida utilizando o framework FastAPI em Python, com o objetivo de fornecer aos usuários acesso fácil e rápido a informações meteorológicas e de qualidade do ar de várias cidades. Juntamente com um Bot em Python que é responsavel por fazer requisições para API's externas e atualizar os dados climaticos no banco.

A biblioteca RabbitMQ é utilizada como um sistema de mensageria para o processamento assíncrono dos envios de email, quando um novo email é cadastrada, ele é enviada para uma fila de processamento no RabbitMQ. O Celery, uma biblioteca de tarefas distribuídas, é responsável por consumir as mensagens da fila e realizar o processamento assíncrono dos emails. O resultado do processamento de uma proposta de empréstimo pode alterar o seu status. Após o processamento, o email é enviado com as informções climaticas atuais.

Através da integração de diferentes tecnologias e o uso de processamento assíncrono, o projeto proporciona uma experiência de usuário ágil, com atualizações em tempo real e um desempenho otimizado.

### Recursos Principais:

Visualização de Dados Meteorológicos e de Qualidade do Ar: Os usuários podem acessar informações detalhadas sobre o clima, incluindo temperatura atual, sensação térmica, umidade e velocidade do vento, além do Índice de Qualidade do Ar (IQA) para diferentes cidades.

Cadastro para Alertas por E-mail: Os usuários têm a opção de cadastrar seu e-mail juntamente com a cidade de interesse. Quando o IQA da cidade cadastrada atinge níveis considerados prejudiciais à saúde, um alerta por e-mail é automaticamente enviado ao usuário para informá-lo sobre a situação atual da qualidade do ar em sua região.

Interface Intuitiva e Responsiva: A aplicação possui uma interface intuitiva e responsiva, permitindo que os usuários naveguem facilmente pelas diferentes seções e visualizem os dados de forma clara e organizada, tanto em dispositivos móveis quanto em desktops.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados em sua máquina:

- Docker
- Git

## Como executar o projeto

Siga as etapas abaixo para executar o projeto localmente:

1. Clone o repositório:
   ```shell
   git clone https://github.com/zeguil/transversal.git
2. Navegue até o diretório do projeto:
    ```shell
    cd Transversal
3. Inicie o ambiente Docker:
    ```shell
    docker-compose up --build
Esse comando irá construir e iniciar os contêineres Docker para o backend, frontend, RabbitMQ e Celery.

Aguarde até que todos os contêineres sejam iniciados. Após a conclusão, você poderá acessar o aplicativo no navegador.

- Aplicação FastApi: http://localhost:8080

Certifique-se de que o ambiente Docker esteja em execução para acessar o Django Admin.
# Encerrando o projeto
Para encerrar o ambiente Docker, você pode pressionar *Ctrl + C* no terminal onde o comando *docker-compose up* foi executado. Isso irá parar todos os serviços.

# Estrutura do Projeto
O projeto é organizado da seguinte maneira:

- O código do FastApi está localizado na pasta src.
- O código do bot está localizado na pasta poster.
- O arquivo docker-compose.yml define a configuração do ambiente Docker, incluindo os serviços do FastApi, bot, RabbitMQ e Celery.

# Observações
- Certifique-se de ter as portas 8000 e 8080 disponíveis em sua máquina para evitar conflitos com outros serviços em execução.

## Créditos

- Desenvolvido por [José Guilherme Lins](https://github.com/zeguil)
