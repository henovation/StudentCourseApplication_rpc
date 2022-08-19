import rides_pb2 as pb
import redis
from datetime import datetime
from google.protobuf.json_format import MessageToJson


r = redis.Redis(
    host='localhost',
    port=6379)

loc = pb.Location(
    lat=32.463546,
    lng=35.75647,
)

request = pb.StartRequest(
    car_id=95,
    driver_id="McQueen",
    passenger_ids=['p1','p2','p3'],
    type=pb.POOL,
    location=loc,
)


time = datetime(2022, 8, 17, 14, 00, 00)
request.time.FromDatetime(time)
print(request.time.ToDatetime())
# print(type(request), request)

# Conver to Json
json_data = MessageToJson(request)
print(json_data)

# Serialize proto to bytes
data = request.SerializeToString()
r.set('test', data)
test_data = r.get('test')

# Unmarshall bytes to proto
request2 = pb.StartRequest()
request2.ParseFromString(test_data)




