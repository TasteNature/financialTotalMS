import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)

socket.bind("tcp://*:5556")
total = 0

while True:
    transactions = socket.recv_json()
    print(transactions)
    for value in transactions.values():
        for numbers in value:
            total+=numbers
    stringTotal = str(total)
    socket.send_string(stringTotal)




