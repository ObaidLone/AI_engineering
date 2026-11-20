import requests
from dotenv import load_dotenv
import os

# response = requests.get("https://httpbin.org/get",
#                         params={"q":"test"},timeout=10)


# response = requests.post("https://httpbin.org/post",
#                         json={"test":"testpost"},timeout=10)
try:
    # response=requests.get("https://httpbin.org/status/404",params={"test":"testerrors"},timeout=10)
    response=requests.get("https://httpbin.org/delay/5",timeout=2)
    response.raise_for_status()
    print("Request success")
except requests.exceptions.RequestException as error:
    print("seomthing went wrong",error)   
    
load_dotenv()
key=os.getenv("MY_API_KEY")

print(key is not None) 

# data=response.json()
    
# print(data["json"]) 
    