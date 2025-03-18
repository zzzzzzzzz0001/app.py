"""
This is the entry point/main module for our web application project
"""
#importing flask which gives our python program the ability to host a web service with URL end points
from flask import Flask, jsonify, request
#importing the PAYE module as we will be taking one of its functions and turning it into a web service
#that can be used anywhere in the world
import PAYE

#oh god don't make me talk about CORS. it triggers bad memories.
#basically it helps to reduce security issues while our web requests are flying around.
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



app = Flask(__name__)


# here we can set the different URL routs for our web service / is generally our home page
#e.g https://www.trademe.com/ is trademes home page
# https://www.trademe.co.nz/c/community/about-us is trademes about us page
#everything after that / can lead to different parts of a website/ web service
@app.route('/')
def hello_world():
    return 'WHAT IS GOIN ON GUYS? WHATS GOOD?!. lol This is a website of sorts...obviously not a very pretty one but it is functional'


@app.route('/getNetIncome/', methods=['POST'])
#this method will be triggered by the above URL end point. take its input and send it to the totalTax() function in PAYE.py
def netIncome():
    gross_income = request.get_json()
    print(gross_income)
    gross = float(gross_income["gross_income"])
    return jsonify(gross - PAYE.totalTax(gross))


if __name__ == '__main__':
    app.run()