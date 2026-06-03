from flask import Flask , render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/form')
def exibir_form():
    return render_template('form.html', resultado= "Total")
@app.route('/processar', methods=['POST'])
def processar():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operacao = request.form['operacao']

    if operacao == 'adicao':
        resultado = num1 + num2
    elif operacao == 'subtracao':
        resultado = num1 - num2
    elif operacao == 'multiplicacao':
        resultado = num1 * num2
    elif operacao == 'divisao':
        resultado = num1 / num2

    return render_template('form.html', resultado=resultado)
if __name__ == '__main__':
    app.run(debug=True , port=5000 , host='0.0.0.0')