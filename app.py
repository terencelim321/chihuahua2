from flask import Flask, render_template, request

import json

#declare app
app = Flask(__name__)

#start app route which is /
@app.route("/")
#declare function
def main():
        with open("app.php","rb") as f:
            jsonData = json.loads(f.read())

        for key,value in jsonData['numbers'].items():
            if key == 'number1':
                x = value
            else:
                y = value

        sum = str(x + y)

        return sum

if __name__ == '__main__':
    app.run(port=5000, debug=True)