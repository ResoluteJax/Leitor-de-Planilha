import os
from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
from openpyxl import load_workbook
import xlrd

app = Flask(__name__)

# Pasta de upload
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/resultados', methods=['GET'])
def resultados():
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_file')
    
    # Verifica se o arquivo .xlsx ou .xls existe
    if os.path.exists(filepath + '.xlsx'):
        filepath += '.xlsx'
    elif os.path.exists(filepath + '.xls'):
        filepath += '.xls'
    else:
        return redirect(url_for('index'))

    try:
        if filepath.endswith('.xlsx'):
            df = pd.read_excel(filepath, header=9)
        elif filepath.endswith('.xls'):
            wb = xlrd.open_workbook(filepath)
            sheet = wb.sheet_by_index(0)
            headers = sheet.row_values(9)  # Assume que a linha 10 é o cabeçalho
            data = [sheet.row_values(i) for i in range(10, sheet.nrows)]
            df = pd.DataFrame(data, columns=headers)
        else:
            return redirect(url_for('index'))
    except Exception as e:
        return render_template('result.html', error='Erro ao ler arquivo: ' + str(e))

    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    table_html = df.to_html(classes='table table-bordered table-striped')

    return render_template('result.html', table=table_html)

@app.route('/limpar_resultados', methods=['GET'])
def limpar_resultados():
    # Lógica para limpar os resultados (apagar o arquivo de resultados, se necessário)
    filepath_xlsx = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_file.xlsx')
    filepath_xls = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_file.xls')

    if os.path.exists(filepath_xlsx):
        os.remove(filepath_xlsx)
    if os.path.exists(filepath_xls):
        os.remove(filepath_xls)
    
    return redirect(url_for('index'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html', error='Nenhum arquivo enviado')
        
        file = request.files['file']
        
        if file.filename == '':
            return render_template('upload.html', error='Nenhum arquivo selecionado')

        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_file')
            file.save(filepath + os.path.splitext(file.filename)[1])
            
            return redirect(url_for('resultados'))

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
