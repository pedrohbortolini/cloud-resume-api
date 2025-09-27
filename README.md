# ⚡ Cloud Resume Challenge – Backend

🔗 Integrado ao site: [pedrobortolini.com.br](https://pedrobortolini.com.br)

Este projeto faz parte do **Cloud Resume Challenge**, onde desenvolvi a segunda etapa do desafio: a criação de uma **API serverless** para registrar e exibir o número de visitantes do site.

---

## 🚀 Tecnologias utilizadas

* **AWS Lambda (Python)** – função que processa requisições e interage com o banco
* **Amazon DynamoDB** – banco NoSQL que armazena o contador de visitas
* **Amazon API Gateway** – expõe a Lambda como uma API HTTP pública
* **JavaScript (frontend)** – consome a API e atualiza o contador no site

---

## 📌 Funcionalidades

* Incremento automático de visitas a cada acesso do site
* Contador armazenado de forma persistente no DynamoDB
* Resposta em **JSON** consumida pelo frontend
* Configuração de **CORS** para aceitar chamadas apenas do domínio `pedrobortolini.com.br`

---

## 🔄 Fluxo de funcionamento

1. O usuário acessa meu site.
2. O **JavaScript** faz uma requisição `POST` para o **API Gateway**.
3. O API Gateway invoca a **função Lambda**.
4. A Lambda atualiza o contador no **DynamoDB** e retorna o valor atualizado.
5. O **frontend** mostra em tempo real o número de visitantes.

