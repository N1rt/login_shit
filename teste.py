menu = (1,2,3,4)
menu_anwser = int(input('oque gostaria de fazer? \n [1] fazer login \n [2] adicionar usuario \n [3] remover usuario \n [4] sair \n:'.capitalize()))
#abrindo a lista
lista = open('the path to the text file here','r')
#passando o atributo object pra a var user_list
users_list = lista
#transformando-a em string e lendo ela
user_list_to_string = str(users_list.read())
#verificando oque o usuario quer fazer
if(menu_anwser == menu[0]):
	#esperando o resultado do input do nome do usuario
	user = input("digite seu nome:".capitalize())
	#checando se o nome do usuario é valido e existe na lista
	if(user_list_to_string.find(user) != -1):
	#se for valido prosseguir para a senha,caso contrario exibir 'usuario inexistente'
		password = input('digite sua senha:'.capitalize())
	#se a senha estiver na lista e ao lado do nome do usuario,permitir o acesso
		if(user_list_to_string.find(f'{user}:{password}') != -1):
			print(f'acesso concedido,bem vindo {user}'.capitalize())
		else:
			print('senha incorreta!'.capitalize())
	else:
		print('usuario inexistente!'.capitalize()) 
elif(menu_anwser == menu[1]):
	#adicionando um novo usuario
	new_user = str(input('digite seu novo usuario assim:"usuario:senha"'.capitalize()))
	lista_edit = open("the path to the text file here",'w')
	lista_edit.write(f'{user_list_to_string}\n{new_user}')
elif(menu_anwser == menu[2]):
	#deletando um novo usuario
	delete_user = str(input('digite "nome:senha" do seu usuario para apaga-lo:'))
	lista_edit = open("the path to the text file here",'w')
	lista_edit.write(f'{user_list_to_string.replace(delete_user,"")}')
if(menu_anwser == menu[3]):
	exit()
