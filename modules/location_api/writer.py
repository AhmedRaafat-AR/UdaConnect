import grpc
import location_pb2
import location_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

# local
#channel = grpc.insecure_channel("localhost:5005")

# nodeport
channel = grpc.insecure_channel("localhost:30003")



stub = location_pb2_grpc.locationServiceStub(channel)

# Update this with desired payload
location = location_pb2.LocationMessage(
    userId=70,
    latitude=-50,
    longitude=100
)

response = stub.Create(location)