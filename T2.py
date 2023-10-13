import hashlib
from pick import pick

class UserControl:
    def __init__(self, username:str, password:str, role=0):
        if type(username)!= str or type(password) != str:
            raise TypeError("Nome de usuário e senha devem ser Strings")
        if type(role)!= int or role <0 or role >3:
            raise TypeError("Role deve ser um inteiro de 0 a 3")
        if not self.is_valid_username(username):
            raise ValueError("Nome de usuário inválido")
        if not self.is_valid_password(password):
            raise ValueError("Senha inválida")
        self.username = username
        self.password_hash = self.hash_password(password)
        self.role = role

    @staticmethod
    def is_valid_username(username):
        # Regras de validação de nome de usuário
        # Nome de usuário deve conter pelo menos 6 caracteres e pelo menos um caracter maiúsculo
        return (len(username) >= 6 and (not username.islower()))
    
    @staticmethod
    def is_valid_password(password):
        # Regras de validação de senha
        # Senha deve conter pelo menos 4 caracteres
        return (len(password)>=4)
   

    def hash_password(self, password):
        # Hash da senha usando hashlib 
        return hashlib.sha256(password.encode()).hexdigest()

    def assign_role(self, role):
        self.role = role

    def check_password(self, password):
        return self.password_hash == self.hash_password(password)

    def check_role(self):
        if(self.role==3):
            return "Admin"
        if(self.role==2):
            return "Editor"
        if(self.role==1):
            return "Reader"
        return "None"
    
    def check_edit(self):
        return self.role>=2
    
    def check_read(self):
        return self.role>=1

    def check_delete(self):
        return self.role==3
    
# Exemplo de uso:
if __name__ == "__main__":
    print("Criar usuário:\n\n")
    username = input("User:\n")
    password = input("Password:\n")
    options=["None","Reader","Editor","Admin"]
    title = "Ecolha a role:"
    (option, index)=pick(options,title,"=>",0)
    user1 = UserControl(username, password,index)

    
    login_username = input("Digite seu nome de usuário: ")
    login_password = input("Digite sua senha: ")
    
    if login_username == user1.username and user1.check_password(login_password):
        print("Login bem-sucedido!")
        print(user1.check_role())
    else:
        print("Nome de usuário ou senha incorretos.")
