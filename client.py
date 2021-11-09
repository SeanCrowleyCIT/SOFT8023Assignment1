from __future__ import print_function

import grpc
import spellingBee_pb2
import spellingBee_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051', options=(('grpc.enable_http_proxy', 0),))
    stub = spellingBee_pb2_grpc.SpellingBeeStub(channel)

    response = stub.TestConnection(spellingBee_pb2.HelloRequest(name="you"))
    print("Client Received: " + response.message)

    match = stub.StartGame(spellingBee_pb2.StartRequest(name=""))
    print(match)
    #print(type(stub))

    #game
    score = 0
    print("Spelling Bee")
    print("Press Q to Exit")

    #create game loop
    exit = False
    while (exit == False):
        word = input("Enter word")
        response = stub.CheckWord(spellingBee_pb2.WordRequest(word=word))
        print(response)
        if (word == 'q') or (word == 'Q'):
            exit = True
