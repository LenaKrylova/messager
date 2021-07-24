import Flask
from datetime import datetime

from flask import Flask, reguest


app = Flask(__name__)
@app.route('/status')
def ststus():
    return {
        'status': True,
        'time': datetime.now(),
        'name': 'Barashek'
    }

app.run()


#@app.route('/send')
#def send_message():

#    return {'OK': True}






#db = []
#@app.route("/status")




#@app.route("/send")
#def send_message()





