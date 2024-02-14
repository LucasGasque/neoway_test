
<h1 align="center">Teste para o processo seletivo da Neoway</h1>

# ✅ Descrição do projeto

Serviço de manipulação de dados e persistência em base de
dados relacional.

# ✅ Etapas da aplicação

- [x] Criação das tabelas: antes de rodar a pipeline a aplicação cria as tabelas do banco usando o ORM SQLModel e SQLAlchemy.
- [x] Extração: os dados são estraídos do documento base usando python.
- [x] Transformação: os dados são validados e transformados usando pydantic.
- [x] Carregamento: os dados são carregados usando o ORM SQLmodel em um banco PostgreSQL,  que roda em um container docker.

# ✅ Como rodar a aplicação

Você pode rodar a aplicação com o docker, para isso é necessário clonar o repositório, entra em sua raiz e rodar o comando:

```bash
  docker compose up
```
o Docker irá então criar dois containers, um para rodar a aplicação e outro para rodar o banco de dados PostgreSQL.

# ✅ Estatus do Projeto

<h3 align="center">
    🚀 Concluído 🚀
</h3>

# 🖥️ Dev

- Made with ❤️ by [Lucas Gasque](https://www.linkedin.com/in/lucasgasque/