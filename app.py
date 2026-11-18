from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    massa = None
    altura = None
    diagnostico = None
    result = None

    if request.method == 'POST':
        massa = float(request.form.get('massa','').replace(',','.'))
        altura = float(request.form.get('altura','').replace(',','.'))
        imc = massa/(altura**2)
        if imc < 18.5:
            diagnostico = f'Você está abaixo do peso.'
        elif imc < 25:
            diagnostico = f'Você está no peso ideial.'
        elif imc < 30:
            diagnostico = f'Você está acima do peso.'
        elif imc < 35:
            diagnostico = f'Você está obeso.'
        elif imc < 40:
            diagnostico = f'Você está com obesidade nível II.'
        else:
            diagnostico = f'Você está com obesidade mórbida.'
        result = f'Seu IMC é {imc:.2f}. {diagnostico}'
    
    return render_template('index.html',result=result)


if __name__ == '__main__':
    app.run(debug=True)