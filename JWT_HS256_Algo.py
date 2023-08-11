import jwt
from datetime import datetime, timedelta

SECRET_KEY = '3l1pmyrsqv__#9g=ytzy21@a861jjr0smhc&kgtcd8yo#216f!(pq&utu&+#zx-yuyc7j)og)iq+)6e^s7tf54w&^c*-!l=d6+2c'

payload = {
    'user_id': 101,
    'username': 'Shivmurat Gupta',
    'exp': datetime.now() + timedelta(minutes=30)
}

encoded_data = jwt.encode(payload=payload,key=SECRET_KEY,algorithm="HS256")

print("Token",encoded_data)


decoded_token = jwt.decode(encoded_data, SECRET_KEY, algorithms=['HS256'])

print("Data",decoded_token)


