from flask import Flask, request, render_template, redirect, url_for


from models import generate_random_users, User

USERS = generate_random_users(10)

my_app = Flask(__name__)


# @my_app.route("/")
# def hello_world():
#     return "Hello, World!"

# @my_app.route("/user")
# def get_users():
#     data = ""
#     for user in USERS:
#         data += f"{str(user)}<br>"
#     print(data)
#     return data

# @my_app.route("/user/<uuid:pk>")
# def get_user_by_id(pk):
#     print(type(pk))
#     user = "Not found"
#     for u in USERS:
#         if u.id == pk:
#             user = u
#     return str(user)
@my_app.route("/", methods=['GET', 'POST'])
@my_app.route("/<uuid:pk>", methods=['GET', "PUT", "DELETE"])
def user_rout(pk=None):
    if request.method == 'GET':
        if pk is None:
            return render_template("users.html", data=USERS)
        else:
            for u in USERS:
                if u.id == pk:
                    return render_template("user_info.html", user=u)
        data = ""
        for user in USERS:
            data += f"{str(user)}<br>"
        print(data)
        return data
    elif request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        email = request.form['email']
        user = User(name=name, age=age, email=email)
        USERS.append(user)
        return redirect(url_for('user_rout'))

        

@my_app.route("/create")
def get_create():
    return render_template("create.html")

if __name__ == "__main__":
    for user in USERS:
        print(user)
    my_app.run(host="0.0.0.0", port=3000)
