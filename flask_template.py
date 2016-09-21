from flask import Flask

app = Flask(__name__)
@app.route("/")
def doNow():
    return "<a href = '/page1'> Page1 </a>"
@app.route("/page1")
def page1():
    return "<a href = '/page2'>Page 1/3 BEGINNING</a>"
@app.route("/page2")
def page2():
    return "<a href = '/page3'>Page 2/3 MIDDLE</a>"
@app.route("/page3")
def page3():
    return "<a href = '/'>Page 3/3 END</a>"
if __name__ == '__main__':
    app.run()
