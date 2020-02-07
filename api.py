"""
API module
"""

from flask import Flask, request, render_template
import database_access as dba


app = Flask(__name__)
@app.route('/')
def home_page():
    # Home page
    return render_template("index.html")


@app.route('/catalog')
def get_all_catalog():
    # Returns all the objects in the catalog
    return dba.get_all_objects()
    

@app.route('/objects', methods=['GET'])
def filter_objects():
    # Gets entered arguments and returns all filtered objects
    arguments = request.args.copy()
    # Removes all empty arguments
    args_to_remove = [k for k,v in arguments.items() if v == ""]
    for arg in args_to_remove:
        arguments.pop(arg)
    return dba.get_objects(['*'], arguments) 
    



if __name__ == '__main__':
    app.run(debug=True)
