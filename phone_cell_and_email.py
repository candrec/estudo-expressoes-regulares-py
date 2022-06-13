#! /usr/bin/python3
# phone_cell_and_email.py - encontra números de telefone, celular e endereço de e-mail clipboard

import pyperclip, re

# bloco - regex telefone fixo
phone_regex = re.compile(r'''(
    (\d{2}|\(\d{2}\))?             # código de área
    (\s|-|\.)?                     # separador
    (\d{4})                        # primeiros 4 dígitos
    (\s|-|\.)                      # separador
    (\d{4})                        # últimos 4 díditos
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extensão
    )''',re.VERBOSE)

# bloco - regex celular
cell_regex = re.compile(r'''(
    (\d{2}|\(\d{2}\))?             # código de área
    (\s|-|\.)?                     # separador
    (\d{5})                        # primeiros 5 dígitos
    (\s|-|\.)                      # separador
    (\d{4})                        # últimos 4 dígitos
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extensão
    )''',re.VERBOSE)

# bloco - regex e-mail: pode não englobar todos os tipos de e-mail, mas será a maioria
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+              # nome do usuário
    @                              # símbolo @
    [a-zA-Z0-9.-]+                 # nome do domínio
    (\.[a-zA-Z]{2,4})              # ponto seguido de outros caracteres (geralmente .com)
    (\.[a-zA-Z]{2,4})?             # ponto seguido de outros caracteres (no Brasil pode ter ainda o .br)
    )''',re.VERBOSE)

# bloco - encontra correspondências no texto do clipboad
text = str(pyperclip.paste())

matches = []

for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)

for groups in cell_regex.findall(text):
    cell_num = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        cell_num += ' x' + groups[8]
    matches.append(cell_num)

for groups in email_regex.findall(text):
    matches.append(groups[0])
# bloco - copia o resultado para o clipboard e exibe na tela
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No Phone numbers, cell numbers or email addresses found.')
