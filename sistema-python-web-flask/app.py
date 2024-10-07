from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM noticias ORDER BY data_publicacao DESC")
    noticias = cur.fetchall()
    cur.close()
    return render_template('index.html', noticias=noticias)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        conteudo = request.form['conteudo']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO noticias (titulo, conteudo) VALUES (%s, %s)", (titulo, conteudo))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))
    return render_template('adicionar_noticia.html')

if __name__ == '__main__':
    app.run(debug=True)
