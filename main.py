from flask import Flask, request, jsonify
from shapely.geometry import Point, Polygon
import json

app = Flask(__name__)


countries = {
    'CountryID': Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
    
}

@app.route('/detect_country', methods=['POST'])
def detect_country():
    data = request.json
    point = Point(data['x'], data['y'])
    for country_id, polygon in countries.items():
        if polygon.contains(point):
            return jsonify({'country_id': country_id})
    return jsonify({'country_id': None})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
