import requests
import os


class YaUploader:
    host = "https://cloud-api.yandex.net:443"

    def __init__(self, token: str):
        self.token = token
        self.set_headers()

    def set_headers(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_href(self, yadisk_file_path):
        method = "/v1/disk/resources/upload"
        href = self.host + method
        file_name = os.path.basename(yadisk_file_path)
        params = {"path": file_name, "overwrite": "true"}
        response = requests.get(url=href, headers=self.headers, params = params)
        res =  response.json()
        print(res)
        self.upload_href = res["href"]



    def upload(self, file_path: str):
        self.get_href(file_path)
        #cur_path = os.getcwd()
        #file_path = os.path.join(cur_path, file_path)
        #print(file_path)
        # with open(file_path, "rb") as upload_file:
        # aaa = upload_file.read()
        #     print(aaa)
        response = requests.put(url=self.upload_href, data=open(file_path, 'rb'))
        print(response.body)




if __name__ == '__main__':
    with open("yandex_token.txt") as token_file:
        token = token_file.read()
    #token = ""

    yandex = YaUploader(token)
    yandex.upload("files\\test2.txt")






