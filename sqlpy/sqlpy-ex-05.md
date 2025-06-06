# Excluindo Dados em uma Tabela com Python e SQLite3

Este roteiro ensina como excluir dados de uma tabela de um banco de dados SQLite usando Python.

## Passos

1. **Importe o módulo sqlite3**  
   O módulo `sqlite3` é usado para interagir com bancos de dados SQLite.

2. **Conecte-se ao banco de dados**  
   Use `sqlite3.connect()` para criar ou abrir um banco de dados existente.

3. **Crie um cursor**  
   O cursor permite executar comandos SQL.

4. **Escreva a consulta de exclusão**  
   Use o comando SQL `DELETE` para remover os dados.

5. **Execute a consulta**  
   Utilize o método `execute()` do cursor para executar a consulta.

6. **Confirme as alterações**  
   Use `commit()` para salvar as alterações no banco de dados.

7. **Feche a conexão**  
   Sempre feche a conexão com o banco de dados após terminar.

## Exemplo de Código

```python
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')

# Criando um cursor
cursor = conn.cursor()

# Consulta SQL para excluir dados
sql_delete_query = """
DELETE FROM tabela_exemplo
WHERE coluna1 = ?;
"""

# Condição para exclusão
dados = ('valor_a_excluir',)

# Executando a consulta
cursor.execute(sql_delete_query, dados)

# Confirmando as alterações
conn.commit()

# Fechando a conexão
conn.close()
```

## Explicação do Código

- **`DELETE FROM tabela_exemplo`**: Especifica a tabela de onde os dados serão excluídos.
- **`WHERE coluna1 = ?`**: Condição para selecionar as linhas a serem excluídas.
- **`cursor.execute(sql_delete_query, dados)`**: Substitui o `?` pelo valor em `dados`.

## Dicas

- Sempre use placeholders (`?`) para evitar ataques de SQL Injection.
- Teste a consulta SQL diretamente no banco de dados antes de implementá-la no código.
- Certifique-se de que a condição no `WHERE` é específica para evitar excluir várias linhas acidentalmente.
- Caso queira excluir todos os dados da tabela, use `DELETE FROM tabela_exemplo;` sem o `WHERE`. **Cuidado ao usar isso!**
