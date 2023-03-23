import requests
from socket import *
import urllib3
#Disable SSL warnings
urllib3.disable_warnings()


#Define API URL
api_url = "http://localhost:5255/api/File"
#Send GET request to API
response = requests.get(api_url, verify=False)
print(response.status_code)
#check if the response code is 200 (ok)
if response.status_code == 200:
    print('x')
    # If response is successful, extract data from JSON response
    data = response.json()
    print(data)
    ipadress = data[0]["ipAddress"]
    filename = data[0]["fileName"]
    portnumber = data[0]["portNumber"]
    print(ipadress, filename, portnumber)

    # Create a new socket object and connect to the specified IP address and port number
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((ipadress, portnumber))
    clientSocket.send(filename.encode())
    print('y')

    file = open('c:/temprecieve/' + filename, 'wb')
    file_data = clientSocket.recv(1024)
    print('b')
    while (file_data):
        print("Receiving...")
        file.write(file_data)
        file_data = clientSocket.recv(1024)
    file.close()

    print("Done Sending")
    clientSocket.close()

else:
    print("Request failed with status code:", response.status_code)







