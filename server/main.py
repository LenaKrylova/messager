# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#from Tools.scripts.mailerdaemon import x


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#a = int(input())
#global fabial
#fabial=123
#def transfer(x):
#    arr = ''
#    print(fabial)
#    while x > 0:
#        arr = str(x%2)+arr
#        x//=2
#    return arr
#print(transfer(a))


from datetime import datetime

from flask import Flask, request


app = Flask(__name__)
@app.route('/status')
def status():
    return {
        'status': True,
        'time': datetime.now(),
        'name': 'Barashek'
    }

app.run()

TEST/

#@app.route('/send')
#def send_message():

#    return {'OK': True}






#db = []
#@app.route("/status")




#@app.route("/send")
#def send_message()









