#! /usr/bin/python3
# phone_cell_and_email.py - encontra números de telefone, celular e endereço de e-mail clipboard

import pyperclip, re

# bloco - regex telefone fixo
phone_regex(r'''(
    (\d{2}|\(\d{2}\))?             # código de área
    (\s|-|\.)?                     # separador
    (\d{4})                        # primeiros 4 dígitos
    (\s|-|\.)                      # separador
    (\d{4})                        # últimos 4 díditos
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extensão
    )''',re.VERBOSE)

# bloco - regex celular

# bloco - regex e-mail

# bloco - encontra correspondências no texto do clipboad

# bloco - copia os resultados para o clipboard
