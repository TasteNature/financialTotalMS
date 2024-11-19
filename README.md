REQUEST data

To request data from the microservice, a JSON file must be sent via a ZMQ socket from the client to the microservice. This is called from server program with the call of socket.send_json(date). The Pyton object being sent data is a dictionary. A Python object is sent as a message using JSON to serialize. The tester program initiates a dictionary and the key-value pair are populated in the data dictionary. The data dictionary will have the following format { date: list of transaction}. For example, the dictionary should look like this { 10/10/25, [15.25, 30, 549.45], 10/25/25, [32], 10/26/25, [1, 58, 23.2 ]}.


RECEIVE data

The total amount was calculated as a float type and converted to string in the microservice. To receive data from the microservice, the call to ZMQ socket with the command socket.recv() will receive the string message which can be decoded and printed on the UI or CLI in this example. 

![image](https://github.com/user-attachments/assets/31d92f54-d371-4339-b999-bbb609af33da)


![image](https://github.com/user-attachments/assets/bdc5c871-9d6f-494b-8fd6-90b3915f6c28)

