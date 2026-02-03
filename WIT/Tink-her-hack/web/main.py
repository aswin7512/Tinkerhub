from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# Mock Database (Just a list of dictionaries for now)
profiles = [
    {
        "id": 1,
        "name": "Alex Developer",
        "role": "Frontend Enthusiast",
        "bio": "I love building beautiful interfaces."
    },
    {
        "id": 2,
        "name": "Sam Backend",
        "role": "Python Guru",
        "bio": "I make things work behind the scenes."
    }
]

# 1. Get ALL Profiles
@app.route("/<int:user_id>", methods=['GET'])
def get_profiles(user_id):
    # jsonify converts Python List -> JSON String
    user_name = next((item["name"] for item in profiles if item["id"] == user_id), None)
    user_role = next((item["role"] for item in profiles if item["id"] == user_id), None)
    return render_template("index.html", name = user_name, role = user_role, id = user_id)

# 2. Get a SPECIFIC Profile (Dynamic Routing)
@app.route("/index/<int:user_id>", methods=['GET'])
def get_single_profile(user_id):
    # Search for the user in our list
    user = next((item for item in profiles if item["id"] == user_id), None)
    
    return render_template("index1.html", name = user["name"], role = user["role"], id = user_id)

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Simple logic (In reality, you'd check a database)
        if username == "admin" and password == "secret":
            return redirect(url_for('dashboard'))
        else:
            return "Access Denied. Wrong credentials."
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return "<h1>Welcome to your Dashboard!</h1>"

if __name__ == "__main__":
    app.run(debug=True)