# Prova pratica de banco de dados
## Professor: Ricardo Duarte Taveira
## Aluno: Elbston Souza Lima Filho
### Proposta: 
1) Usar o PlaywithDocker com as seguintes operações: 
Instalação dos containers MYsql e PhpMyAdmin usando  o Docker Compose como definido na Avaliação-10;
2) Execução de Scripts similares aos scripts da Avaliação-10. 
3) Captura da imagem da saida do script;
4) Gerar no repositorio do GitHub a pasta avaliacao_pratica-2 e nela gravar as imagens dos resultados da execução dos scripts.
5) Copiar o link do github especificamente da pasta avaliacao_pratica_2 na Avaliação que será criada no GoogleClassrom.
## Codigo utilizado
```
import mysql.connector

# Conexão com o banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='myuser',
    password='mypassword',
    database='mydatabase'
)

cursor = conn.cursor()

# Função para executar uma consulta e exibir os resultados
# Função para executar uma consulta e exibir os resultados
def executar_consulta(query):
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        # Usar 'join' para formatar a saída sem parênteses ou vírgulas
        print(", ".join(str(item) for item in row))


# 1. Listar todos os alunos reprovados
query_reprovados = """
SELECT 
    TB_ALUNOS.nome AS Nome_Aluno, 
    TB_DISCIPLINA.nome AS Nome_Disciplina, 
    TB_PROFESSOR.nome AS Nome_Professor, 
    Matricula.nota_N1, 
    Matricula.nota_N2, 
    (Matricula.nota_N1 + Matricula.nota_N2) / 2 AS Media, 
    Matricula.faltas, 
    CASE 
        WHEN (Matricula.nota_N1 + Matricula.nota_N2) / 2 < 6 THEN 'Reprovado por Média' 
        WHEN Matricula.faltas > 5 THEN 'Reprovado por Falta' 
    END AS Status_Reprovacao
FROM Matricula
JOIN TB_ALUNOS ON Matricula.nome_aluno = TB_ALUNOS.id
JOIN TB_DISCIPLINA ON Matricula.disciplina = TB_DISCIPLINA.id
JOIN TB_PROFESSOR ON Matricula.nome_professor = TB_PROFESSOR.id
WHERE Matricula.Aprovado_SN = FALSE;
"""
print("Alunos Reprovados:")
executar_consulta(query_reprovados)

# 2. Listar todos os alunos aprovados
query_aprovados = """
SELECT 
    TB_ALUNOS.nome AS Nome_Aluno, 
    TB_DISCIPLINA.nome AS Nome_Disciplina, 
    TB_PROFESSOR.nome AS Nome_Professor, 
    Matricula.nota_N1, 
    Matricula.nota_N2, 
    (Matricula.nota_N1 + Matricula.nota_N2) / 2 AS Media, 
    Matricula.faltas, 
    'Aprovado por Média' AS Status_Aprovacao
FROM Matricula
JOIN TB_ALUNOS ON Matricula.nome_aluno = TB_ALUNOS.id
JOIN TB_DISCIPLINA ON Matricula.disciplina = TB_DISCIPLINA.id
JOIN TB_PROFESSOR ON Matricula.nome_professor = TB_PROFESSOR.id
WHERE Matricula.Aprovado_SN = TRUE;
"""
print("\nAlunos Aprovados:")
executar_consulta(query_aprovados)

# 3. Listar a quantidade de alunos aprovados
query_quantidade_aprovados = """
SELECT COUNT(*) AS Quantidade_Aprovados
FROM Matricula
WHERE Matricula.Aprovado_SN = TRUE;
"""
print("\nQuantidade de Alunos Aprovados:")
executar_consulta(query_quantidade_aprovados)

# 4. Listar a quantidade de alunos reprovados
query_quantidade_reprovados = """
SELECT COUNT(*) AS Quantidade_Reprovados
FROM Matricula
WHERE Matricula.Aprovado_SN = FALSE;
"""
print("\nQuantidade de Alunos Reprovados:")
executar_consulta(query_quantidade_reprovados)

# Fechando a conexão
cursor.close()
conn.close()
```
