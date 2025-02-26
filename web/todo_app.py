# Your index.html file should be inside a templates folder.


from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(200), nullable=False)
    Description = db.Column(db.String(500), nullable=False)
    Time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.Sno} - {self.Title}"

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        todo_title = request.form["title"]
        todo_desc = request.form["desc"]
        todo = Todo(Title=todo_title, Description=todo_desc)
        db.session.add(todo)
        db.session.commit()
        print(request.form["title"])
        print(request.form["desc"])
    all_todo = Todo.query.all()
    return render_template("index.html", alltodo=all_todo)

@app.route("/show")
def show():
    all_todo = Todo.query.all()
    return f"Total Todos: {len(all_todo)}"

@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(Sno=sno).first()
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect("/")


if __name__ == "__main__":
  app.run(debug=True)






# app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# # db = SQLAlchemy(app)


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/welcome/<name>')
# def welcome(name):
#     return '<h1>welcome user '+name+'!</h1>'    

# if __name__ == '__main__':
#     app.run(debug=True)

# for rendering the html file, we can add the bootstrap code in 
# html file and render it using render_template function



# # tells Flask to trigger the function when the user navigates to the / path using a web browser
# @app.route('/')
# def greeting():
#     return "hii welcome to flask"  

# @app.route('/welcome/<name>')
# def welcome(name):
#     return '<h1>welcome user " +name + "!</h1>'





# from markupsafe import escape

# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"

# from markupsafe import escape

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'
