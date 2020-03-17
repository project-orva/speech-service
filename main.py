#!python2.7.16
from concurrent import futures

import grpc

import service_pb2
import service_pb2_grpc

class SpeechServicer(service_pb2_grpc.grpcSpeechServicer):
    def DetermineSpeech(self, request, context):
        return service_pb2.SpeechResponse(message="dis working!?!")
    def DetermineSkill(self, request, context):
        return service_pb2.SkillResponse(URL="http://localhost:3000/test")

def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_grpcSpeechServicer_to_server(
        SpeechServicer(), server
    )
    server.add_insecure_port('[::]:5355')
    server.start()
    print("server started on ported 5355")
    server.wait_for_termination()

if __name__ == "__main__":
    run()    