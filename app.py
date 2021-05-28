from flask import Flask, render_template, request, json, jsonify


#declare app
app = Flask(__name__)

#start app route which is /
@app.route("/sum ", methods=['GET', 'POST'])
#takes json info from php file
def main():
        #with open("app.php","rb") as f:
        #    jsonData = json.loads(f.read())

        #for key,value in jsonData['numbers'].items():
        #    if key == 'number1':
        #        x = value
        #    else:
        #        y = value
        if request.method == 'POST':
            num1 = request.form['num1']
            num2 = request.form['num2']

        sum = num1 + num2 

        return sum

#declare function
@app.route("/calculator")
def calculator():
   return render_template('sum.html')



if __name__ == '__main__':
    app.run(port=5000, debug=True)