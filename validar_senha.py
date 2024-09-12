def validar_senha():  # Essa varíavel ira validar a senha.
    senha_correta = "segura123"  
    
    while True:  
        senha_usuario = input("Insira a senha: ") # Insira a senha do úsuario. 
        
        if senha_usuario == senha_correta: # Digite a senha correta para obter acesso.
            print("Acesso permitido")  
            break  # Sai do loop se a senha estiver correta  
        else:  
            print("Senha incorreta")  # Caso o programa fale que etá incorreto, caso erre a senha. 

# Chama a função para validar a senha  
validar_senha()