# use flask to run the app and create a api localhost with http://127.0.0.1:5000

from flask import Flask,request,jsonify
app = Flask(__name__)

# create a route for get_users


# @app.route("/get_users/<user_id>")
# def get_users(user_id):
#     user_data = {
#         "user_id": user_id,
#         "name": "Akai",
#     }
#     extra = request.args.get("extra")
#     if extra:
#         user_data["extra"] = extra
#     return jsonify(user_data),200



# create a route for home
@app.route("/")
def home():
    return "Home"


if __name__ == "__main__":
    app.run(debug=True)



