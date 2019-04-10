from flask import Flask, render_template, jsonify
from data import ArticlesTemp
from database import OracleDB

app = Flask(__name__)
Articles = ArticlesTemp()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)

@app.route('/article/<string:id>')
def article(id):
    return render_template('article.html', id=id)

@app.route('/oracle')
def oracle():
    ora=OracleDB()
    ora.connect()
    l_res=ora.select()
    print(l_res)
    return jsonify(l_res)

if __name__ == '__main__':
    app.run(debug=True)