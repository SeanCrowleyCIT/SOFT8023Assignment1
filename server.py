from concurrent import futures
import logging
import grpc
import dictionary
import spellingBee_pb2
from spellingBee_pb2_grpc import SpellingBeeServicer
import spellingBee_pb2_grpc

from dictionary import wordDictionary

class SpellingBeeServer(SpellingBeeServicer):

    def StartGame(self, request, context):
        words = wordDictionary()
        print(words)
        print(request.name)
        selection = words.get_selection()
        return spellingBee_pb2.StartResponse(words="message")

    def CheckWord(self, request, context):
        return spellingBee_pb2.WordResponse(valid='1', score='2', total_score='3')

    #def


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    spellingBee_pb2_grpc.add_SpellingBeeServicer_to_server(SpellingBeeServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()



