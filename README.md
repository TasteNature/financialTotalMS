REQUEST data

To request data from the microservice, a JSON file must be sent via a ZMQ socket from the client to the microservice. This is called from server program with the call of socket.send_json(date). The Pyton object being sent data is a dictionary. A Python object is sent as a message using JSON to serialize. The tester program initiates a dictionary and the key-value pair are populated in the data dictionary. 

![image](https://github.com/user-attachments/assets/81bf1ddb-6ed4-46d8-996c-84b6eb07b63a)

RECEIVE data

The total amount was calculated as a float type to send data from the microservice. This must be cast to a string to send a message using the example call: send_string(string with the calculated total). 

![image](https://github.com/user-attachments/assets/1792b99b-52c3-4dda-9cfd-5a54781f9937)
![image](https://github.com/user-attachments/assets/97cc4f46-a4a7-49a6-adce-75229bd3e260)
