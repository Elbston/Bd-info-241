# Atividade 10 de Banco de dados
## Nesta atividade deveriamos criar 1 banco de dados com 4 tabelas e fazer um codigo em python para ler e mostrar os dados
### Saida do codigo:
![Captura de tela de 2024-09-18 15-19-49](https://github.com/user-attachments/assets/9a8cfde4-a9cc-4018-8cc0-ac8da3c5ee4d)
### Codigo em python:
```
import mysql.connector

# Conexão com o banco de dados
connection = mysql.connector.connect(
    host="localhost",
    user="myuser",
    password="mypassword",
    database="mydatabase"
)

cursor = connection.cursor()

query = """
    SELECT a.nome, d.nome_disciplina, m.N1, m.N2, m.faltas, 
           ((m.N1 + m.N2) / 2) AS media, 
           CASE 
               WHEN ((m.N1 + m.N2) / 2) >= 7 AND m.faltas <= 5 THEN 'Aprovado'
               ELSE 'Reprovado'
           END AS status
    FROM TB_MATRICULA m
    JOIN TB_ALUNO a ON m.id_aluno = a.id_aluno
    JOIN TB_DISCIPLINA d ON m.id_disciplina = d.id_disciplina
"""

print("Executando consulta...")

cursor.execute(query)
results = cursor.fetchall()

if not results:
    print("Nenhum resultado encontrado.")
else:
    for (nome_aluno, nome_disciplina, N1, N2, faltas, media, status) in results:
        print(f"Aluno: {nome_aluno}, Disciplina: {nome_disciplina}, N1: {N1}, N2: {N2}, Faltas: {faltas}, Média: {media}, Status: {status}")

cursor.close()
connection.close()

```
