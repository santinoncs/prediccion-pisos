from fastai.learner import load_learner
from flask import Flask, request, make_response, jsonify
import pandas as pd
from flask_cors import CORS,cross_origin

# Initialize the Flask app
app = Flask(__name__)
CORS(app)

# Load the model
def load_model(path):
    learn = load_learner(path)
    return learn


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    try:
        model_path = "model.pkl"
        learn = load_model(model_path)
        data = request.get_json()
        print(data)
        input = [data['ascensor'], data['parking'], data['calefaccion'], data['acondicionado'],
                 data['obarNueva'], data['terraza'], float(data['eurom2']), float(data['m2']),
                 int(data['rooms']), int(data['banos']), data['location'], data['transporte'], data['piscina'], data['jardin']]
        input_df = pd.DataFrame([input], columns=['ascensor', 'parking', 'calefaccion', 'acondicionado',
                 'obarNueva', 'terraza', 'eurom2', 'm2', 'rooms', 'banos', 'location', 'transporte', 'piscina', 'jardin'])
        #prediction = learn.predict(input_df)
        prediction = learn.predict(input_df.iloc[0])
        #output = {'prediction': str(prediction[0])}
        #output = {'Price': float(prediction[0])}
        output = {'price': float(prediction[0]['price'])}
        response = jsonify(output)
        return response
    except KeyError:
        return jsonify({'error': 'Invalid form data'})

if __name__ == "__main__":
    # Carga el modelo
    #model_path = "model.pkl"
    #model = load_model(model_path)
    # Inicia el servidor Flask
    app.run(debug=True, host='0.0.0.0', port=8080)
