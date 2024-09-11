# Atividade 09 de banco de dados
## Nesta atividade deveriamos alterar um codigo dado pelo professor para que realizasse essas duas funções, isso sendo feito em python no play with docker:
### a) Se o numero de faltas for maior ou igual a 20 setar o atributo Aprovado_SN com FALSO (REPROVADO) ;
### b) Se a média Aritmética de N1 e N2 for < 6.0   setar o atributo Aprovado_SN com FALSO (REPROVADO) ;
## Saida do docker hub:
![Captura de tela de 2024-09-11 14-28-01](https://github.com/user-attachments/assets/c6ee6744-742d-4b97-9c2a-959287d2154d)
## Codigo utilizado no Play with docker:
```
import mysql.connector

# Conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="myuser",  
    password="mypassword",  
    database="mydatabase"  
)

cursor = conexao.cursor()

# Criar a tabela TB_ALUNOS
cursor.execute("""
CREATE TABLE IF NOT EXISTS TB_ALUNOS (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    N1 FLOAT(4,2),
    N2 FLOAT(4,2),
    Faltas INT(2),
    Aprovado_SN BOOLEAN
)
""")
conexao.commit()

# Função para inserir um registro
def inserir_aluno(nome, N1, N2, Faltas, Aprovado_SN):
    sql = "INSERT INTO TB_ALUNOS (nome, N1, N2, Faltas, Aprovado_SN) VALUES (%s, %s, %s, %s, %s)"
    val = (nome, N1, N2, Faltas, Aprovado_SN)
    cursor.execute(sql, val)
    conexao.commit()

# Função para consultar os alunos
def consultar_alunos():
    cursor.execute("SELECT * FROM TB_ALUNOS")
    return cursor.fetchall()

# Função para atualizar o nome de um aluno pelo id
def atualizar_aluno(id, novo_nome):
    sql = "UPDATE TB_ALUNOS SET nome = %s WHERE id = %s"
    val = (novo_nome, id)
    cursor.execute(sql, val)
    conexao.commit()

# Função para excluir um aluno pelo id
def excluir_aluno(id):
    sql = "DELETE FROM TB_ALUNOS WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    conexao.commit()


inserir_aluno("João", 8.5, 7.0, 10, True)
inserir_aluno("Maria", 5.0, 4.5, 22, False)
inserir_aluno("Pedro", 6.0, 6.5, 18, True)
inserir_aluno("Ana", 9.0, 8.5, 5, True)
inserir_aluno("Lucas", 4.0, 5.0, 12, False)

# Consultar os alunos cadastrados
alunos = consultar_alunos()
for aluno in alunos:
    print(aluno)

# Atualizar o nome do aluno cujo id é 4
atualizar_aluno(4, "Ana Clara")

# Excluir o aluno cujo id é 3
excluir_aluno(3)

# Função para verificar e atualizar status de aprovação
def atualizar_status_aprovacao():
    cursor.execute("SELECT id, N1, N2, Faltas FROM TB_ALUNOS")
    alunos = cursor.fetchall()
    
    for aluno in alunos:
        id_aluno, N1, N2, Faltas = aluno
        media = (N1 + N2) / 2
        aprovado = True

        if Faltas >= 20 or media < 6.0:
            aprovado = False
        
        
        cursor.execute("UPDATE TB_ALUNOS SET Aprovado_SN = %s WHERE id = %s", (aprovado, id_aluno))
        conexao.commit()

# Função para ler todos os registros e mostrar o status de aprovação
def mostrar_status_aprovacao():
    cursor.execute("SELECT nome, Aprovado_SN FROM TB_ALUNOS")
    alunos = cursor.fetchall()
    
    for aluno in alunos:
        nome, aprovado_sn = aluno
        status = "APROVADO" if aprovado_sn else "REPROVADO"
        print(f"Aluno: {nome}, Status: {status}")

# Atualizar o status de aprovação dos alunos
atualizar_status_aprovacao()

# Mostrar o status de aprovação dos alunos
mostrar_status_aprovacao()
```
