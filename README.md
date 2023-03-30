# Solução do desafio de programação

## Sobre a solução
A aplicação foi desenvolvida utilizando Python e o Framework Django. O banco de dados utilizado foi o PostgreSQL.

A aplicação conta com um código limpo, variáveis bem descritivas e funções com responsabilidades bem definidas.

O código foi escrito de forma que seja fácil de ser entendido e de ser mantido.

A aplicação conta também com uma série de bibliotecas voltada para a qualidade do código, como o flake8, black, isort e o mypy. Que ajudam
bastante na manutenção do código.

Além disso, conta com um sistema de testes automatizados com uma cobertuda de 99% do código. O que ajuda muito na confiabilidade do código durante a evolução e refatoração do mesmo.

Para facilitar o deploy, o sistema também conta com a configuração do docker e docker-compose. Onde está configurado a aplicação Django, um banco de dados PostgreSQL e o Nginx.

## Como rodar a aplicação
A aplicação pode ser rodada de duas formas, utilizando o docker-compose ou rodando localmente.

### Utilizando Docker (recomendado)
#### Requisitos:
- Docker
- Docker-compose
- Git

#### Passos:
- Clone o repositório
- Acesse a pasta raiz do projeto
- Faça uma cópia do arquivo `.env.example` e renomeie para `.env`
- Execute o comando `docker-compose up -d --build`
- Acesse a aplicação pelo endereço `http://localhost` (observe que está na porta padrão do nginx, que é a 80)

### Rodando localmente
#### Requisitos:
- Python 3.10
- Poetry 1.3.1
- Git

#### Passos:
- Clone o repositório
- Acesse a pasta raiz do projeto
- Instale as dependências com o comando `poetry install`
- Acesse o virtual env criado pelo poetry com o comando `poetry shell`
- Faça uma cópia do arquivo `.env.example` e renomeie para `.env`
- Descomente DATABASE_URL que está abaixo do comentário `# local example with sqlite`
- Comente as quatro linhas que estão abaixo do comentário `# example with docker and postgres`
- Execute as migrações com o comando `python manage.py migrate`
- Execute o comando `python manage.py runserver`
- Acesse a aplicação pelo endereço `http://localhost:8000`


## Executando testes unitários
Para checar a cobertura de testes, execute o comando `pytest --cov --cov-report=html` e abra o arquivo `index.html` que vai ser
gerado na pasta `htmlcov`.

## Executando os linters
Já existe um arquivo configurado com todos os linters do projeto.

Para executar, basta executar o comando `./scripts/.lint.sh` na raiz do projeto.

## Como utilizar a aplicação
### Fazer upload do arquivo
- Acesse o endereço `http://localhost:8000/upload/` ou `http://localhost/upload/` (se estiver utilizando o docker)
- Clique no botão `Choose File` e selecione o arquivo CNAB desejado
- Clique no botão `Upload`
- Aguarde o processamento do arquivo
  - Será exibido uma mensagem de sucesso ou erro. E em caso de sucesso, você será redirecionado para a página de listagem das transações

### Listar as transações
- Acesse o endereço `http://localhost:8000/transactions/` ou `http://localhost/transactions/` (se estiver utilizando o docker)
    - Esta página exibe todas as transações importadas colocando em vermelho as que são de saída.

### Listar as lojas e suas respectivas transações
- Acesse o endereço `http://localhost:8000/store-transactions/` ou `http://localhost/store-transactions/` (se estiver utilizando o docker)
    - Esta página exibe todas as lojas e suas respectivas transações. E também exibe o saldo de cada loja.
    - Para ver as transações de uma loja, basta clicar no nome da loja.

### Login e registro
- Para fazer o cadastro, acessar o endereço `http://localhost:8000/register/` ou `http://localhost/register/` (se estiver utilizando o docker) e preencha os seus dados
- Para fazer o login, acessar o endereço `http://localhost:8000/login/` ou `http://localhost/login/` (se estiver utilizando o docker) e preencha os seus dados

### Acessndo o admin
A aplicação conta com o admin padrão do django que pode ser acessado da seguinte forma
- crie um superuser com o comando `python manage.py createsuperuser` (se estiver rodando localmente) ou `docker-compose exec app python manage.py createsuperuser` (se estiver utilizando o docker)
- Acesse o endereço `http://localhost:8000/admin/` ou `http://localhost/admin/` (se estiver utilizando o docker)

### Melhorias e próximos passos
Devido ao tempo limitado e concorrente com o trabalho, não foi possível implementar algumas funcionalidades que eu gostaria de ter implementado.

As melhorias a serem discutidas seriam:

- Implementar Paginação nas listagens
- Implementar filtros nas listagens
- Implementar uma api REST utilizando o Django Rest Framework com autenticação JWT
- Implementar um sistema de processo em background para processar os arquivos CNAB e não travar a aplicação na hora da resposta
  - Seria implementado com o DjangoQ
- Melhorias na parte visual da aplicação



-------------------------------------------------------------------------------------------------------



# Desafio programação - para vaga desenvolvedor

Por favor leiam este documento do começo ao fim, com muita atenção.
O intuito deste teste é avaliar seus conhecimentos técnicos em programação.
O teste consiste em parsear [este arquivo de texto(CNAB)](https://github.com/ByCodersTec/desafio-ruby-on-rails/blob/master/CNAB.txt) e salvar suas informações(transações financeiras) em uma base de dados a critério do candidato.
Este desafio deve ser feito por você em sua casa. Gaste o tempo que você quiser, porém normalmente você não deve precisar de mais do que algumas horas.

# Instruções de entrega do desafio

1. Primeiro, faça um fork deste projeto para sua conta no Github (crie uma se você não possuir).
2. Em seguida, implemente o projeto tal qual descrito abaixo, em seu clone local.
3. Por fim, envie via email o projeto ou o fork/link do projeto para seu contato Bycoders_ com cópia para rh@bycoders.com.br.

# Descrição do projeto

Você recebeu um arquivo CNAB com os dados das movimentações finanaceira de várias lojas.
Precisamos criar uma maneira para que estes dados sejam importados para um banco de dados.

Sua tarefa é criar uma interface web que aceite upload do [arquivo CNAB](https://github.com/ByCodersTec/desafio-ruby-on-rails/blob/master/CNAB.txt), normalize os dados e armazene-os em um banco de dados relacional e exiba essas informações em tela.

**Sua aplicação web DEVE:**

1. Ter uma tela (via um formulário) para fazer o upload do arquivo(pontos extras se não usar um popular CSS Framework )
2. Interpretar ("parsear") o arquivo recebido, normalizar os dados, e salvar corretamente a informação em um banco de dados relacional, **se atente as documentações** que estão logo abaixo.
3. Exibir uma lista das operações importadas por lojas, e nesta lista deve conter um totalizador do saldo em conta
4. Ser escrita na sua linguagem de programação de preferência
5. Ser simples de configurar e rodar, funcionando em ambiente compatível com Unix (Linux ou Mac OS X). Ela deve utilizar apenas linguagens e bibliotecas livres ou gratuitas.
6. Git com commits atomicos e bem descritos
7. PostgreSQL, MySQL ou SQL Server
8. Ter testes automatizados
9. Docker compose (Pontos extras se utilizar)
10. Readme file descrevendo bem o projeto e seu setup
11. Incluir informação descrevendo como consumir o endpoint da API

**Sua aplicação web não precisa:**

1. Lidar com autenticação ou autorização (pontos extras se ela fizer, mais pontos extras se a autenticação for feita via OAuth).
2. Ser escrita usando algum framework específico (mas não há nada errado em usá-los também, use o que achar melhor).
3. Documentação da api.(Será um diferencial e pontos extras se fizer)

# Documentação do CNAB

| Descrição do campo  | Inicio | Fim | Tamanho | Comentário
| ------------- | ------------- | -----| ---- | ------
| Tipo  | 1  | 1 | 1 | Tipo da transação
| Data  | 2  | 9 | 8 | Data da ocorrência
| Valor | 10 | 19 | 10 | Valor da movimentação. *Obs.* O valor encontrado no arquivo precisa ser divido por cem(valor / 100.00) para normalizá-lo.
| CPF | 20 | 30 | 11 | CPF do beneficiário
| Cartão | 31 | 42 | 12 | Cartão utilizado na transação 
| Hora  | 43 | 48 | 6 | Hora da ocorrência atendendo ao fuso de UTC-3
| Dono da loja | 49 | 62 | 14 | Nome do representante da loja
| Nome loja | 63 | 81 | 19 | Nome da loja

# Documentação sobre os tipos das transações

| Tipo | Descrição | Natureza | Sinal |
| ---- | -------- | --------- | ----- |
| 1 | Débito | Entrada | + |
| 2 | Boleto | Saída | - |
| 3 | Financiamento | Saída | - |
| 4 | Crédito | Entrada | + |
| 5 | Recebimento Empréstimo | Entrada | + |
| 6 | Vendas | Entrada | + |
| 7 | Recebimento TED | Entrada | + |
| 8 | Recebimento DOC | Entrada | + |
| 9 | Aluguel | Saída | - |

# Avaliação

Seu projeto será avaliado de acordo com os seguintes critérios.

1. Sua aplicação preenche os requerimentos básicos?
2. Você documentou a maneira de configurar o ambiente e rodar sua aplicação?
3. Você seguiu as instruções de envio do desafio?
4. Qualidade e cobertura dos testes unitários.

Adicionalmente, tentaremos verificar a sua familiarização com as bibliotecas padrões (standard libs), bem como sua experiência com programação orientada a objetos a partir da estrutura de seu projeto.

# Referência

Este desafio foi baseado neste outro desafio: https://github.com/lschallenges/data-engineering

---

Boa sorte!
