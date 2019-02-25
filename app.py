import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:adminuser@db:3306/BOOKSINFO'
db= SQLAlchemy(app)

class Books(db.Model):
    title= db.Column(db.String(50),unique=True,primary_key=True)

    def __init__(self,title):
        self.title=title

    def __repr__(self):
        return self.title

db.create_all()
db.session.commit()

@app.route('/', methods=["GET","POST"])
def hello_world():
    if request.method == 'POST':
        book= request.form.get("title")
        book = Books(book)
        db.session.add(book)
        db.session.commit()
        return redirect('/')

    books= Books.query.all()
    return render_template('index.html',books=books)

@app.route('/update', methods=["POST"])
def update():
        oldTitle= request.form.get("oldTitle")
        newTitle= request.form.get("updatedTitle")
        value = Books.query.filter(Books.title == oldTitle).first()
        value.title=newTitle
        db.session.commit()
        return redirect("/")

@app.route('/delete', methods=['POST'])
def delete():
    title=request.form.get('title_to_delete')
    value = Books.query.filter(Books.title == title).first()
    db.session.delete(value)
    db.session.commit()
    return redirect('/')
if __name__== "__main__":
    app.run(host='0.0.0.0',port=5000)
