# Getting started

申請Line Message API, 取得Channel secret與Channel access token
```
https://developers.line.me/en/docs/messaging-api/overview/

Example :
Channel secret 
a8a677c1556cee2b391d9c9bf48e9886
Channel access token (long-lived) 
M4p9wTXd1lVh1b/JEsZEWJYWh0moL6uNfTwyv2cSZHgGpAXgHKlwpMYi0sQOrHQTQnPxg2A5NKgFpJpKf7JX8HPnTmbl7XyCmBbnmk0dZ1gVsVBj4qCh8IvLjOuS70JafPpbQal89oWMKUT3XfUbGAdB04t89/1O/w1cDnyilFU=
```



申請IBM Cloud, 開通Python Flask與IBM Watson Language Translator服務 
```
Python Flask (Python 3.6)
https://console.bluemix.net/catalog/starters/python-flask

Language Translator
https://console.bluemix.net/catalog/services/language-translator
並取得apikey

Example :
{
  "apikey": "tppoJc9atJQ6OdAxKowb--fobg3v37XBsctH9aN-hmxw",
  "iam_apikey_description": "Auto generated apikey during resource-key operation for Instance - crn:v1:bluemix:public:language-translator:us-south:a/e53593410850040145fe151f7ffc71ea:c5ffa4ab-cde0-4b5a-9805-c37c38636701::",
  "iam_apikey_name": "auto-generated-apikey-c0fb65ef-3801-4b61-903a-9635d35faae1",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/e53593410850040145fe151f7ffc71ea::serviceid:ServiceId-8f7a7fc4-3121-40e0-8949-a3c0d091bbcd",
  "url": "https://gateway.watsonplatform.net/language-translator/api"
}
```


GitHub下載Sample專案
```
index.py :
    channel_secret = '改成你自己的'
    channel_access_token = '改成你自己的'
    language_translator = LanguageTranslatorV3( version='2018-05-31', iam_api_key='改成你自己的')

```



上傳至IBM Cloud
```
下載並且安裝IBM Cloud CLI
https://console.bluemix.net/docs/cli/index.html#overview

產生IBM Cloud API KEY
https://console.bluemix.net/iam/#/apikeys
並將API KEY存成apiKey.json放置IBM CLoud CLI預設的路徑 "C:\Program Files\IBM\Cloud\bin" 下

Example : 
    apiKey.json
    {
	"name": "kk",
	"description": "kk use only",
	"createdAt": "2018-07-02T18:32+0000",
	"apiKey": "0GAYaz_jDpeU3XfS88NUfHyiqrRq7rfOoBE7395YJP3M"
    }


以系統管理員身分執行Windows PowerShell
    登入 ibm cloud  ibmcloud login -o "你的帳號" -s "你的空間"
    Example :
        ibmcloud login -o "casparc@tw.ibm.com" -s "dev"
    
    上傳python專案 ibm cloud app push xxx(your pythone project name)
    Example :
        ibmcloud app push kkpython-line
```



預覽IBM Cloud Python
```
造訪 https://你的專案.mybluemix.net/ 出現HELLO代表已經安裝設置完成
    Example :
    https://kkpython-line.mybluemix.net/
    HELLO

前往Line Message API設定Webhook URL
    Example :
    https://kkpython-line.mybluemix.net/callback

設定完成後，就可以與Line機器人開始互動啦！
```



Project檔案說明
```
index.py :
    對話機器人主檔

Procfile :
    指定Flask的index首頁

requirements.txt :
    此專案需要的Library，使用pip install -r requirement.txt安裝 (需先安裝pip)

runtime.txt :
    告知IBM Cloud Python此專案使用的版本

setup.py :
    IBM Watson所需相關元件，使用ppip install -r requirement.txt的時候會順便處理安裝
```