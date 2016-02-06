# Justin Camarena
# 02/05/2016

#!flask/bin/python
from flask import Flask, url_for, request, jsonify
import linecache
import requests
import json

app = Flask(__name__)

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

@app.route('/')
def api_root():
    return 'http://juscam.com\n'

#GET framework
@app.route('/api/<int:line_id>', methods= ['GET'])
def api_get(line_id):
    textLine = linecache.getline('api.txt',line_id)
    return textLine

#PUT framework
@app.route('/api/<string:line>', methods= ['PUT'])
def api_put(line):
    with open("api.txt", "a") as myfile:
        myfile.write(line + '\n')
    return str(count)
#Post framework
@app.route('/api/', methods= ['POST'])
def api_post():
    #learn how to handle as json not text
    data =request.data
    dataDict = json.loads(data)

    postLine = int(dataDict.get("line"))
    postString = dataDict.get("string")
    replace_line('api.txt', postLine - 1, postString + "\n")
    return "Line " + dataDict.get("line") + " replaced\n"
#DELETE framework
@app.route('/api/<int:line_id>', methods= ['DELETE'])
def api_delete(line_id):
    replace_line('api.txt',line_id - 1, '')
    return "Line " + str(line_id) + " deleted\n"


if __name__ == '__main__':
    app.run(debug=True)

'''

curl -X GET http://127.0.0.1:5000/api/5
as an example etc

pass POST using apiclient.py with:
data = {"line" : "1", "string" : "Whatever you want here"}


'''