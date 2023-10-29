from flask import Flask, request, render_template
from flask import request
import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import CBC
import encrypting
import decrypting


app = Flask(__name__)

templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app.template_folder = templates_dir     


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/work_mode', methods=['GET'])
def work_mode():
    return render_template('work_mode.html')

@app.route('/work_mode/encryptText', methods=['GET','POST'])
def work_encrypt():
    if request.method == 'POST':
        data = request.get_json()
        inputText = data['inputText']
        inputKey = data['inputKey']
        padding = data['padding']
        seed = 12345
        result, padding = CBC.CBC_encryption(inputText, inputKey, seed, padding)
        response_data = {
            'result': result,
            'padding': padding
        }
        json_response = json.dumps(response_data)
        return json_response
    else:
        return 'Invalid request method'
    
@app.route('/work_mode/decryptText', methods=['GET','POST'])
def work_decrypt():
    if request.method == 'POST':
        data = request.get_json()
        inputText = data['inputText']
        inputKey = data['inputKey']
        padding = data['padding']
        seed = 12345
        result = CBC.CBC_decryption(inputText, inputKey, seed, padding)
        return result
    else:
        return 'Invalid request method'

@app.route('/test_mode', methods=['GET'])
def test_mode():
    return render_template('test_mode.html')

@app.route('/test_mode/encryptMessage', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        data = request.get_json()
        form = data['form']
        message = data['message']
        key = data['key']
        if form == 'Binary':      
            res = encrypting.encrypting_binaryStr(message, key)
        elif form == 'ASCII':
            res = encrypting.encrypting_ascii(message, key)
        else:
            res = encrypting.encrypting_hexadecimal(message, key)
        return res
    else:
        return "Invalid request method."
    
@app.route('/test_mode/decryptMessage', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        data = request.get_json()
        form = data['form']
        message = data['message']
        key = data['key']
        if form == 'Binary':      
            res = decrypting.decrypting_binaryStr(message, key)
        elif form == 'ASCII':
            res = decrypting.decrypting_ascii(message, key)
        else:
            res = decrypting.decrypting_hexadecimal(message, key)
        return res
    else:
        return "Invalid request method."



@app.route('/multi_mode', methods=['GET'])
def multi_mode():
    return render_template('multi_mode.html')

@app.route('/multi_mode/encryptMessage', methods=['GET', 'POST'])
def multi_encrypt():
    if request.method == 'POST':
        data = request.get_json()
        form = data['form']
        message = data['message']
        key = data['key']
        if form == 'double':      
            res = encrypting.encrypting_double(message, key)
        else:
            res = encrypting.encrypting_three(message, key)
        return res
    else:
        return "Invalid request method."
    
@app.route('/multi_mode/decryptMessage', methods=['GET', 'POST'])
def multi_decrypt():
    if request.method == 'POST':
        data = request.get_json()
        form = data['form']
        message = data['message']
        key = data['key']
        if form == 'double':      
            res = decrypting.decrypting_double(message, key)
        else:
            res = decrypting.decrypting_three(message, key)
        return res
    else:
        return "Invalid request method."



if __name__=="__main__":
    app.run()
