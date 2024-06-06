import requests
import datetime

PIXELA_URL = "https://pixe.la/v1/users"
USER_NAME = "DUMMY_USER"
TOKEN = "DUMMY_TOKEN"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# # create user
# response = requests.post(url=PIXELA_URL, json=user_params)
# print(response.text)

##############

graph_parameters = {
    "id": "graph1",
    "name": "Coding Crunch",
    "unit": "Hours",
    "type": "float",
    "color": "kuro"
}

header = {
    "X-USER-TOKEN": TOKEN
}
# # create graph
# response = requests.post(f"{PIXELA_URL}/{USER_NAME}/graphs", json=graph_parameters, headers=header)
# print(response.text)

##########

today = datetime.datetime.now()
formatted_date = today.strftime("%Y%m%d")

pixel_config ={
    "date": formatted_date,
    "quantity": input("How many hours did you code today? ")
}
# # post pixel
response = requests.post(f"{PIXELA_URL}/{USER_NAME}/graphs/graph1", json=pixel_config, headers=header)
print(response.text)

###########

UPDATE_ENDPOINT = f"{PIXELA_URL}/{USER_NAME}/graphs/graph1/{formatted_date}"

new_pixel_data = {
    "quantity": "3.5"
}
# # Update pixel
# response = requests.put(url= UPDATE_ENDPOINT, json=new_pixel_data, headers=header)
# print(response.text)

############

DELETE_ENDPOINT = f"{PIXELA_URL}/{USER_NAME}/graphs/graph1/{formatted_date}"

# response = requests.delete(url=DELETE_ENDPOINT, headers=header)
# print(response.text)

# visit https://pixe.la/v1/users/amoghborikar/graphs/graph1.html for results!