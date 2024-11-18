import zmq
import json

context = zmq.Context()
print("Client attempting to connect to server...")
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5556')

data = {}
while True:
    print(data)
    dateInput = str(input("Enter the date of transaction:  \n"))
    transactionAmount = float(input("Enter the transaction amount:  \n"))
    if dateInput not in data:
        data[dateInput]= [transactionAmount]
    else:
        currentList = data.get(dateInput)
        print(currentList)
        currentList.append(transactionAmount)
        data[dateInput] = currentList
        print(data)
    userPrompt = str(input("Enter \"y\" to continue entering transaction or \"n\" to quit:  "))
    if userPrompt == "n":
        print(data)
        break
socket.send_json(data)
message = socket.recv()
print(f"Server sent back the total: {message.decode()}")