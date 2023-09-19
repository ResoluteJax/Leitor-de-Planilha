import os
from flask import Flask, request, render_template, redirect, url_for
import pandas as pd

app = Flask(__name__)

def read_excel(file):
    # Lendo a planilha e ignorando as colunas da "F" até a "M"
    df = pd.read_excel(file)
    df = df.fillna('')
    return df


def generate_alert_message(df):
    # Verificando se as colunas 'Hora 1' e 'Hora 2' existem
    if 'Hora 1' not in df.columns or 'Hora 2' not in df.columns:
        return f"Colunas esperadas não encontradas. Colunas na planilha: {', '.join(df.columns)}"

    df['Presença'] = df.apply(lambda row: 'Presente' if row['Hora 1'] != '' and row['Hora 2'] != '' else 'Ausente', axis=1)
    return df

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "Nenhum arquivo enviado."
        
        file = request.files['file']
        
        if file:
            file_extension = os.path.splitext(file.filename)[1].lower()
            
            if file_extension in ['.xls', '.xlsx']:
                df = read_excel(file)
                result = generate_alert_message(df)
                
                if isinstance(result, str):  # Se for uma mensagem de erro
                    return result
                
                table = result.to_html(classes='table table-striped')
                
                # Redirecionar para a página de resultado com os dados da tabela
                return redirect(url_for('show_result', table=table))
            else:
                return "Formato de arquivo inválido. Por favor, envie um arquivo .xls ou .xlsx."
    
    return render_template('upload.html')

@app.route('/result')
def show_result():
    table = request.args.get('table')  # Obtenha os dados da tabela passados como parâmetro
    return render_template('result.html', table=table)

if __name__ == '__main__':
    app.run(debug=True)
