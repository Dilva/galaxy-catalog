from flask import Flask

import database_access as dba


app = Flask(__name__)
@app.route('/')
def func():
    return "Galaxy Catalog"


@app.route('/api1')
def func1():
    return dba.get_all_objects()
    

@app.route('/api2')
def func2():
    return dba.get_objects(['ngc_id', 'constellation_latin'], {'season':'Autumn', 'type':'Galaxy'})


if __name__ == '__main__':
    app.run(debug=True)