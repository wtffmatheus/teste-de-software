import xml.etree.ElementTree as ET
from jinja2 import Template
import os

# Verifica se o arquivo XML realmente existe antes de tentar ler
if not os.path.exists('resultado_testes.xml'):
    print("Erro: O arquivo 'resultado_testes.xml' nao foi encontrado!")
    exit(1)

# 1. Ler o XML gerado pelo Pytest
tree = ET.parse('resultado_testes.xml')
root = tree.getroot()

testes = []
for testcase in root.iter('testcase'):
    nome_tecnico = testcase.get('name')
    # Deixa o nome mais amigavel (ex: test_cep_sorocaba vira Cep Sorocaba)
    nome_amigavel = nome_tecnico.replace('test_', '').replace('_', ' ').title()
    status = "APROVADO ✅" if len(list(testcase)) == 0 else "REPROVADO ❌"
    testes.append({"item": nome_amigavel, "status": status})

# 2. Template do documento HTML
html_template = """
<html>
<body style="font-family: Arial; padding: 20px;">
    <h1>Termo de Aceite Técnico - Express CEP</h1>
    <p>Relatório de validação automatizada das regras de negócio:</p>
    <ul>
        {% for t in testes %}
        <li><strong>{{ t.item }}:</strong> {{ t.status }}</li>
        {% endfor %}
    </ul>
    <p>Gerado via GitHub Actions para Express CEP.</p>
</body>
</html>
"""

# 3. Gerar o arquivo final
template = Template(html_template)
with open("termo_de_aceite.html", "w", encoding="utf-8") as f:
    f.write(template.render(testes=testes))

print("Sucesso! O arquivo 'termo_de_aceite.html' foi criado.")