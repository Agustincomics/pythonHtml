from flask import Flask, render_template, request
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.txt'):
            filename = file.filename.replace('.txt', '')
            document = Document()
            estilo_parrafo = document.styles['Normal']
            estilo_fuente = estilo_parrafo.font
            estilo_parrafo.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
            estilo_parrafo.paragraph_format.line_spacing = Pt(28)  # Interlineado de 28 puntos
            estilo_fuente.name = 'Arial Narrow'
            estilo_fuente.size = Pt(11)
            content = file.read().decode('utf-8')  # Leer el contenido como una cadena de texto
            document.add_paragraph(content, style='Normal')
            document.save(f'static/{filename}.docx')
            return render_template('success.html', filename=f'{filename}.docx')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)