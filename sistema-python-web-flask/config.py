class Config:
    # Configurações para o MySQL
    MYSQL_HOST = 'localhost'  # Endereço do servidor MySQL (no WampServer, geralmente é localhost)
    MYSQL_USER = 'root'  # Usuário padrão do MySQL no WampServer
    MYSQL_PASSWORD = ''  # Substitua pela sua senha do MySQL
    MYSQL_DB = 'noticias_db'  # Nome do banco de dados que você criou no MySQL
    MYSQL_CURSORCLASS = 'DictCursor'  # Opcional: para retornar os dados como dicionários
