import time
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc
import producer

locationProducer = producer
locationValue = {}

class LocationServicer(location_pb2_grpc.locationServiceServicer):
    def Create(self, request, context):

        request_value = {
            "userId": int(request.userId),
            "latitude": int(request.latitude),
            "longitude": int(request.longitude)
        }
        print(request_value)
        
        locationValue = request_value
        locationProducer.Create(locationValue)
        
        return location_pb2.LocationMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_locationServiceServicer_to_server(LocationServicer(), server)

print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)