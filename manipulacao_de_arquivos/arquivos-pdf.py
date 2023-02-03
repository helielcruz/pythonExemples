import pydf
pdf = pydf.generate_pdf(""" <h1>Olá, mundo</h1>
<p>Aqui está</p>""")
with open('test_doc.pdf', 'wb') as arquivo:
    arquivo.write(pdf)