import jwt
import time
import datetime
import uuid
from flask import Flask, jsonify, request

app = Flask(__name__)

# Define the secret key to use for signing the JWT
app.config['SECRET_KEY'] = 'a9ddbcaba8c0ac1a0a812dc0c2f08514b23f2db0a68343cb8199ebb38a6d91e4ebfb378e22ad39c2d01d0b4ec9c34aa91056862ddace3fbbd6852ee60c36acbf'

@app.route('/login/<user_id>')
def login(user_id):


    # Set the issued at (iat) time for the JWT to the current time
    issued_at = int(time.time())

    # Generate a unique identifier (jti) for the JWT
    jwt_id = str(uuid.uuid4())

    # Set date timestamp for the payload...
    date = str(datetime.date.today())

    # Define the payload for the JWT
    data = {
        'iat': issued_at,
        'jti': jwt_id,
        'payload': {
            'data': user_id,
            'date': date
        }
    }



    # Generate the JWT
    jwt_token = jwt.encode(data, app.config['SECRET_KEY'], algorithm='HS512')

    encrypted_token = jwt_token.decode('utf-8')
    # Return the JWT as a JSON response
    return jsonify({'toekn': encrypted_token})


@app.route('/validate/<token>')
def validate(token):


    # Decode and verify the JWT
    payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS512'])


    # Return the JWT as a JSON response
    return payload


if __name__ == '__main__':
    # Run the app on port 8080
    app.run(host='0.0.0.0', port=8080)
