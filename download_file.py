import requests

def download_file(url: str, filepath: str):
    with open(filepath, 'wb') as file:
        file_content = requests.get(url,allow_redirects = True).content
        file.write(file_content)
        file.close()
        

file_to_download = "https://www.linkedin.com/favicon.ico"
path = "C:\\Users\\Utente\\Desktop\\Data Engineering\\Community\\linkedin.ico"
download_file(file_to_download, path)
