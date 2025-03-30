from flask import Flask, render_template, url_for, redirect, session
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
import os
import sqlite3
import pandas as pd

app = Flask(__name__)
app.secret_key = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!/xd5\xa2\xa0\x9fR"\xa1\xa8'

"""
    Set SERVER_NAME to localhost as twitter callback
    url does not accept 127.0.0.1
    Tip: set callback origin(site) for Facebook and Twitter
    as http://domain.com (or use your domain name) as these providers
    don't accept 127.0.0.1 / localhost
"""

app.config["SERVER_NAME"] = "www.super-pms.onrender.com"
oauth = OAuth(app)


# State variable
User_Level = "Unregistered"  # Four States "Unregistered", "Admin", "Student", "Teacher"

# Utilities
table_style = """
<style>
/* includes alternating gray and white with on-hover color */

table{
    margin:20px;
    width:94%;
    background-color: #fffffc;
    box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.15);
    border: 1px solid #e3e6f0;
}
th{
    text-align:left;
}
td, th {
    padding: 5px;
}

tr:nth-child(even) {
    background: #E0E0E0;
}

tr:hover {
    background: silver;

</style>
"""



@app.route("/")
@app.route("/home")
def index():
    global User_Level
    title = "home"
    user_name = session.get("user")
    print(user_name)
    user = ""
    k = ""
    # set user level
    if user_name:
        user = user_name["given_name"]
        if user_name["hd"] == "karunya.edu.in":
            User_Level = "Student"
            k = "S"
        elif user_name["email"] == "paulisaiah@karunya.edu.in":
            User_Level = "Admin"
            k = "A"
        elif user_name["hd"] == "karunya.edu.in":
            User_Level = "Teacher"
            k = "T"
        else:
            User_Level = "Unregistered"
        if len(user) > 20:
            user = user_name["given_name"][0:20]

    # given_name = user_name.split()[0]

    return render_template("index.html", user=user, title=title)


@app.route("/google/")
def google():
    # Google Oauth Config
    # Get client_id and client_secret from environment variables
    # For development purpose, you can directly put it
    # here inside double quotes
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")

    CONF_URL = "https://accounts.google.com/.well-known/openid-configuration"
    oauth.register(
        name="google",
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={"scope": "openid email profile"},
    )

    # Redirect to google_auth function
    redirect_uri = url_for("google_auth", _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@app.route("/google/auth/")
def google_auth():
    token = oauth.google.authorize_access_token()
    session["user"] = token["userinfo"]
    return redirect("/")


@app.route("/logout")
def logout():
    global User_Level
    User_Level = "Unregistered"
    session.pop("user", None)
    return redirect("/")


@app.route("/404")
def Error():
    return render_template("404.html")


# Protected pages

# Student pages
def StuDashBoard():
    global User_Level
    
    if(User_Level=="Unregistered"):
        return redirect("/404")
    
    print(User_Level)
    title = "dashboard"
    ##########################################     BOILER PLATE   ##########################################
    user_name = session.get("user")
    print(user_name)
    user = ""
    if user_name:
        if len(user) > 20:
            user = user_name["given_name"][0:20]
    ##########################################     BOILER PLATE   ##########################################
    ##########################################     BOILER PLATE   ##########################################
    print(User_Level)
    if User_Level == "Unregistered":
        title = "Unauthorized"
        return render_template("Unauthorized.html", user=user, title=title)
    ##########################################     BOILER PLATE   ##########################################

    conn = sqlite3.connect("data.sqlite")
    df_projects = pd.read_sql_query(
        "SELECT * FROM projects", conn
    )  # Replace 'your_table_name' with the name of your table
    df_projects = df_projects.to_html()
    df_projects = table_style+df_projects
    # print(df_projects)
    
    
    df_subjects = pd.read_sql_query(
        "SELECT * FROM subjects", conn
    )  # Replace 'your_table_name' with the name of your table
    df_subjects = df_subjects.to_html()
    df_subjects = table_style+df_subjects
    # print(df_subjects)
    
    
    df_courses = pd.read_sql_query(
        "SELECT * FROM courses", conn
    )  # Replace 'your_table_name' with the name of your table
    df_courses = df_courses.to_html()
    df_courses = table_style+df_courses
    # print(df_courses)

    
    conn.close()

    return render_template("StuDashBoard.html", user=user, title=title, df_projects=df_projects, df_subjects =df_subjects, df_courses=df_courses )






@app.route("/dashboard")
def DashBoard():
    global User_Level
    if(User_Level=="Unregistered"):
        return redirect("/404")
    elif(User_Level=="Student"):
        return StuDashBoard()

    return redirect("/")


@app.route("/StuRegPro")
def StuRegPro():
    
    if(User_Level=="Unregistered"):
        return redirect("/404")
    return render_template("StuRegPro.html")

@app.route("/StuRegSub")
def StuRegSub():
    
    if(User_Level=="Unregistered"):
        return redirect("/404")
    return render_template("StuRegSub.html")

@app.route("/StuRegCor")
def StuRegCor():
    
    if(User_Level=="Unregistered"):
        return redirect("/404")
    
    conn = sqlite3.connect("data.sqlite")
    
    df_courses = pd.read_sql_query(
        "SELECT * FROM courses", conn
    )  # Replace 'your_table_name' with the name of your table


    df_courses_table = df_courses.to_html()
    df_courses_table = table_style+df_courses_table


    df_courses = df_courses.values.tolist()

    conn.close()
    return render_template("StuRegCor.html",Courses=df_courses,corTable=df_courses_table)

if __name__ == "__main__":
    app.run(debug=True)
