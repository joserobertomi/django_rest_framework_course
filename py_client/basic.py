import requests 

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/?this_arg=this_value"

get_response = requests.get(endpoint,json={"product_id": 123}) # HTTP request
print(get_response.text)
print(get_response.json())
print(get_response.status_code)
