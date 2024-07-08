# app.py
from flask import Flask, request, jsonify
import jwt
from utils import is_prime, is_valid_name, is_valid_role

app = Flask(__name__)

SECRET_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJTZWVkIjoiNzg0MSIsIk5hbWUiOiJUb25pbmhvIEFyYXVqbyJ9.QY05sIjtrcJnP533kQNk8QXcaleJ1Q01jWY_ZzIZuAg"

@app.route('/validate_jwt', methods=['POST'])
def validate_jwt():
    token = request.json.get('token')
    
    if not token:
        return jsonify({'error': 'Token is missing'}), 400
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token has expired'}), 400
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 400
    
    # Validate claims
    if len(payload) != 3:
        return jsonify({'error': 'Token must contain exactly 3 claims'}), 400
    
    name = payload.get('Name')
    role = payload.get('Role')
    seed = payload.get('Seed')
    
    if not name or not is_valid_name(name):
        return jsonify({'error': 'Invalid Name claim'}), 400
    
    if not role or not is_valid_role(role):
        return jsonify({'error': 'Invalid Role claim'}), 400
    
    if not seed or not isinstance(seed, int) or not is_prime(seed):
        return jsonify({'error': 'Invalid Seed claim'}), 400
    
    return jsonify({'message': 'JWT is valid'}), 200

if __name__ == '__main__':
    app.run(debug=True)
