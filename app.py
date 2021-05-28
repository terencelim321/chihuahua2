from flask import Flask, render_template, request, json, jsonify


#declare app
app = Flask(__name__)

#start app route which is /
@app.route("/sum")
#takes json info from php file
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

#declare function
@app.route("/calculator")
def calculator():
   return render_template('sum.html')



if __name__ == '__main__':
    app.run(port=5000, debug=True)