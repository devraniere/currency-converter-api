# Conversor de Moedas: API Segura e Dockerizada

Este projeto é uma **API RESTful** desenvolvida em **Python com Flask**. Ela oferece um serviço robusto para conversão de moedas, consultando taxas de câmbio atualizadas via uma API externa (ExchangeRate-API).

---

## Vantagens Desta API

Esta API serve como uma camada intermediária, oferecendo benefícios importantes sobre o uso direto da API externa:

* **Segurança:** A chave da API externa é protegida no ambiente do servidor (contêiner Docker), não sendo exposta ao usuário final.
* **Abstração:** Permite trocar a fonte das taxas de câmbio no futuro sem afetar as aplicações que consomem esta API.
* **Resposta Simplificada:** Filtra a resposta da API externa, retornando apenas os dados essenciais em JSON.
* **Extensibilidade:** Possibilita a adição de lógica de negócio futura, como cache de taxas ou regras de negócio específicas.

---

## Vantagens do Docker

O uso do Docker neste projeto garante eficiência no desenvolvimento e na implantação:

* **Portabilidade:** A aplicação e suas dependências são empacotadas em um contêiner, permitindo a execução consistente em qualquer ambiente.
* **Isolamento:** A API opera em um ambiente isolado, prevenindo conflitos de dependências com outras aplicações no mesmo sistema.
* **Implantação Simplificada:** Padroniza e agiliza o processo de deploy.
* **Escalabilidade:** Facilita a execução de múltiplas instâncias da API para lidar com maior volume de requisições.

---

## Como Rodar o Projeto (Docker)

Siga os passos abaixo para configurar e executar a API localmente.

### Pré-requisitos

* **Docker Desktop** (ou Docker Engine) instalado.
* Uma **chave de API** válida da [ExchangeRate-API](https://www.exchangerate-api.com/).

### Passos

1.  **Clonar o Repositório:**
    ```bash
    git clone git@github.com:devraniere/currency-converter-api.git
    cd currency-converter-api
    ```

2.  **Construir a Imagem Docker:**
    ```bash
    docker build -t currency-api .
    ```

3.  **Executar o Contêiner Docker:**
    Substitua `SUA_CHAVE_DE_API_REAL_AQUI` pela sua chave da ExchangeRate-API.
    ```bash
    docker run -p 5000:5000 -e EXCHANGE_RATE_API_KEY="SUA_CHAVE_DE_API_REAL_AQUI" currency-api
    ```
    A API estará acessível em `http://localhost:5000`.

---

## Como Usar a API

### Endpoint Principal

* **URL:** `http://localhost
