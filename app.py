import mysql.connector

def create():
    produto = "abacaxi"
    valor = 5
    tipo = "fruta"

    comando = f'INSERT INTO information (produto, valor, tipo) VALUES ("{produto}", {valor}, "{tipo}")'
    cursor.execute(comando)
    conexao.commit() # quando editamos o banco temos que colocar o commit

def read():
    comando = f'SELECT * FROM information'
    cursor.execute(comando)
    resultado = cursor.fetchall() # quando está lendo o banco
    print(resultado)

def update():
    nome = "uva"
    valor = 5
    comando = f'UPDATE information SET valor = {valor} WHERE produto = "{nome}"'
    cursor.execute(comando)
    conexao.commit() # quando editamos o banco temos que colocar o commit

def delete():
    nome = "laranja"
    comando = f'DELETE FROM information WHERE produto = "{nome}"'
    cursor.execute(comando)
    conexao.commit() # quando editamos o banco temos que colocar o commit

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "total123**",
    database = "crud-python"
)

cursor = conexao.cursor()

# só chamar a função que queira executar aqui que da bom

cursor.close()
conexao.close()