import users_wrapper as us

opcao =  True

while opcao:
    opcao = input("Opções: \n 1 - Listar Usuários \n 2 - Detalhar Usuário \n 3 - Criar Usuário \n 4 - Atualizar Usuário \n 5 - Deletar Usuário \n 6 - Sair \n :")
    # listar
    if opcao == "1":
        print("Lista de Usuários:")
        users = us.list()
        if users:
            for user in users:
                print(f"{user['id']} - {user['name']}")
        else: 
            print("inválido")

    # detalhar
    if opcao == "2":
        user_id = input("Digite o id do usuário que quer detalhar:")
        user = us.read(user_id)
        if user:
            print(f"id: {user['id']}\n nome: {user['name']}\n telefone: {user['phone']} \n email:{user['email']}")
        else:
            print("inválido")

    # criar
    if opcao == "3":
        dados = {
            "name": input("Nome: "),
            "username": input("Username: "),
            "email": input("Email: "),
            "phone": input("Telefone: "),
            "website": input("Website: ")}
        
        user = us.create(dados)
        if user:
            print("criado com sucesso!")
        else:
            print("erro.")

    # atualizar
    if opcao == "4":
        user_id = input("Digite o id do usuário: ")
        dados = {
            "name": input("Novo nome: "),
            "username": input("Novo username: "),
            "email": input("Novo email: "),
            "phone": input("Novo telefone: "),
            "website": input("Novo website: "),}
        
        user = us.update(user_id, dados)
        if user:
            print("atualizado com sucesso!")
        else:
            print("erro ao atualizar.")

    # excluir
    if opcao == "5":
        user_id = input("digite o id do usuário que deseja excluir:")
        user = us.read(user_id)
        confirmar = input("digite 's' se deseja realmente excluir o usuário:")
        if confirmar == "s":
            excluir = us.delete(user_id)
            print("excluído.")
        else:
            print("cancelado.")

    # sair
    if opcao == "6":
        print("espero que não volte ;)")