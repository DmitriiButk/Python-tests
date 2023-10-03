import requests

token = ''
url_for_check_status = 'https://cloud-api.yandex.net'
url_for_create_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {
    'Authorization': token,
}

folder_name = 'for_hw'
params = {'path': f'/{folder_name}'}

response = requests.get(url_for_check_status, headers=headers)
print(response.status_code)

response_file = requests.put(url_for_create_folder, headers=headers, params=params)
print(response_file.status_code)
