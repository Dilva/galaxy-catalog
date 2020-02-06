from flask import Flask, request, render_template
import database_access as dba


app = Flask(__name__)
@app.route('/')
def func():
    # Home page
    return render_template("")


@app.route('/catalog')
def func1():
    # Returns all objects
    return dba.get_all_objects()
    

@app.route('/objects', methods=['GET'])
def func2():
    # Gets entered arguments and returns all filtered objects
    return dba.get_objects(['*'], request.args) 
    

if __name__ == '__main__':
    app.run(debug=True)