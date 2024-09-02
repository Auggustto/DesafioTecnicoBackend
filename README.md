## Resolução do Desafio Técnico Brasilprev – Backend

### Linguagem e Framework Utilizados

- Linguagem: Python
- Framework: FastAPI

### Ferramentas e Tecnologias

- Ferramenta de Testes: Pytest
- Banco de Dados: PostgreSQL
- ORM Utilizado: SQLAlchemy

### Instruções de Uso

1. **Clonagem e Inicialização**

   Navegue até a pasta do projeto e abra um terminal. Em seguida, execute o seguinte comando:

   ```bash
   docker-compose up --build
   ```

   Este comando criará as imagens e os containers necessários para a aplicação.

   **Observações Importantes:**
   - As portas configuradas no projeto são:
     - Banco de Dados (PostgreSQL): `2222:5432`
     - Aplicação (FastAPI): `0.0.0.0:8000`
   - Se houver alguma aplicação local rodando nessas portas, pode ocorrer um erro. Recomenda-se temporariamente liberar essas portas ou modificar as configurações em `Dockerfile` e `/app/models/database/connect_database.py`.

2. **Processo de Inicialização**

   - Uma imagem e container PostgreSQL serão criados com as configurações necessárias.
   - Uma imagem e container da aplicação FastAPI serão criados.
   - Os testes automáticos serão iniciados.

3. **Acessar a Aplicação**

   Para acessar a aplicação, abra um navegador e insira a seguinte URL:

   - [http://localhost:8000](http://localhost:8000)

   Isso abrirá a documentação da API, gerada pelo FastAPI com base no OpenAPI, utilizando o Swagger UI para interação.

### Como Utilizar a Documentação da API

1. **Explorar os Endpoints**

   Na página inicial da documentação, você encontrará uma lista de todos os endpoints (rotas) disponíveis na API, cada um acompanhado por uma breve descrição, métodos HTTP permitidos e possíveis parâmetros.

2. **Testar os Endpoints**

   Para testar um endpoint específico:

   - Selecione o Endpoint: Clique no endpoint desejado na lista para ver detalhes.
   - Envie uma Requisição: Dentro da visualização do endpoint, clique em "Try it out" para expandir o formulário de teste.
   - Preencha os Parâmetros: Insira os parâmetros necessários para a requisição.
   - Execute a Requisição: Clique em "Execute" para enviar a requisição para o servidor FastAPI.

3. **Visualizar a Resposta**

   Após enviar a requisição, a resposta retornada pelo servidor será exibida diretamente na interface do Swagger UI, incluindo o código de status HTTP, cabeçalhos de resposta e corpo da resposta (se houver).
