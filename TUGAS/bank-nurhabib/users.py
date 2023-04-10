# Di dalam file ini terdapat system penambahan dan pengambilan user

# Import

# Variable
users = [
    {
        "username" : "fitri",
        "password" : "271006",
        "role" : "admin"
    }
]

# Function
def login(**data_user):
    for i in range(len(users)):
        if data_user["username"] == users[i - 1]["username"]:
            if data_user["password"] == users[i - 1]["password"]:
                role = users[i - 1]["role"]
                if role == "admin":
                    return "lamanAdmin"
                elif role == "customor":
                    return "lamanCustomor"

def addUser(**data_user):
    username_users = []
    for i in range(len(users)):
        username_users.append(users[i-1]["username"])

    if data_user["username"] in username_users:
        print("Maaf data telah ada di database")
    else:
        users.append(
            {
                "username" : data_user["username"],
                "password" : data_user["password"],
                "role" : data_user["role"],
                "saldo" : 0
            }
        )
        print("Data Berhasil Ditambahkan")


def deleteUser(username):
    for i in range(len(users)):
        if username == "fitri":
            print("Maaf tidak bisa menghapus user default")
        elif users[i - 1]["username"] == username:
            id_user = i - 1
            users.remove(id_user)
            print("User behasil dihapus")

def showUsers(users):
    print('Daftar user : ')
    for u in range(len(users)):
        print(str(u+1), '. ', users[u]['username'], '(',users[u]['role'],')')

def admin():
    pass

def lihatSaldo(username):
    for i in range(len(users)):
        if users[i - 1]["username"] == username:
            print(users[i - 1]["saldo"])