from flask import Flask, render_template, request
app = Flask(__name__)    
app.static_folder = 'static'


@app.route('/')          
def hello_world():
    return render_template("index.html")

@app.route('/jovenes')
def jove():
    return render_template('Jovenes.html')

@app.route('/sobre-nosotros')
def us():
    return render_template('Sobre_Nosotros.html')

@app.route('/adultos-mayores')
def viejos():
    return render_template('Adultos_mayores.html')
@app.route('/integrantes')
def intg():
    return render_template('Integrantes.html')


#EN LA NAV BAR PONGAN EN EL HREF DE CADA ELEMENTO DE LA BARRA EL NOMBRE QUE SALE AL LADO DE CADA APP.ROUTE QUE SALE EN ESTE ARCHIVO

   

@app.route('/adultos')
def adultos():
    return render_template("Adultos.html")  

@app.route('/IMC')
def imc():
    return render_template('IMC.html')

@app.route('/IMC', methods=['POST'])          
def IMC():
    print(request.form)
    nr1 = request.form['nr1']
    nr2 = request.form['nr2']
    nr3 = request.form['nr3']
    a=nr1
    b=int(nr2)
    c=int(nr3)
    cm= c/100
    x= cm*cm
    result= b*x
    result=result/10
    result=int(result)
    return render_template(
            'result.html',
            result = result
        )




if __name__=="__main__":  
    app.run(debug=True) 