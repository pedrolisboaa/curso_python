"""
Operador ternário
"""

logged_user = False
msg = 'Usuario logado.' if logged_user else 'Usuário precisa logar'

idade = 18
msg_idade = 'Maior de idade' if idade >= 18 else 'Menor de idade'

print(msg)
print(msg_idade)

# if logged_user:
#     msg = 'Usuário logado'
# else:
#     msg = 'Usuário precisa fazer login'
#
# print(msg)
