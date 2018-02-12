from flask import request, render_template
from app import app
from app.utils.db_utils.read import sql_demo_to_html


@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html', data=sql_demo_to_html())
        # return sql_demo_to_html()
    elif request.method == 'POST':
        return "Bad request", 400
