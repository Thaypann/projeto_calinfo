from flask import Flask, render_template, redirect

app = Flask(__name__)

app.debug = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/primeiro')
def primeiro():
    return render_template('primeiro.html')

@app.route('/segundo')
def segundo():
    return render_template('segundo.html')

@app.route('/terceiro')
def terceiro():
    return render_template('terceiro.html')

@app.route('/quarto')
def quarto():
    return render_template('quarto.html')

@app.route('/inscricao1')
def inscricao1():
    return redirect('https://suap.ifrn.edu.br/projetos_ensino/editais_abertos/')

@app.route('/inscricao2')
def inscricao2():
    return redirect('https://suap.ifrn.edu.br/projetos_ensino/editais_abertos/')


@app.route('/portal')
def portal():
    return redirect('https://suap.ifrn.edu.br/accounts/login/?next=/')

@app.route('/noticia1')
def noticia1():
    return redirect('https://www.metropoles.com/mundo/brasil-e-china-devem-fechar-acordo-para-baratear-maquinario-agricola')

@app.route('/noticia2')
def noticia2():
    return redirect('https://saibamais.jor.br/2025/05/ifrn-avanca-com-centro-de-tecnologia-e-cultura-que-vai-funcionar-na-cidade-alta/')

@app.route('/noticia3')
def noticia3():
    return redirect('https://blogantenado.com/partiuif-divulgada-a-terceira-chamada-de-estudantes-para-pre-matricula/')

@app.route('/noticia4')
def noticia4():
    return redirect('https://portal.conif.org.br/comunicacao/gerais/conif-assina-acordo-e-confirma-alianca-de-ciencia-tecnologia-e-inovacao-com-a-embrapa')

@app.route('/noticia5')
def noticia5():
    return redirect('https://concursosrn.com.br/ifrn-divulga-concurso-publico-com-52-vagas-em-diversos-cargos/')



if __name__ == '__main__':
    app.run(debug=True)
