from fastai.learner import load_learner
from flask import Flask, request, make_response, jsonify
import pandas as pd
from flask_cors import cross_origin

# Initialize the Flask app
app = Flask(__name__)

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
        input = [data['Elevator'], data['Parking'], data['Heating'], data['CoolAir'],
                 data['Construction'], data['Balcony'], float(data['RatioEurM']), float(data['Sqft_m2']),
                 int(data['Rooms']), int(data['Toilets'])]
        input_df = pd.DataFrame([input], columns=['Elevator', 'Parking', 'Heating', 'CoolAir',
                 'Construction', 'Balcony', 'RatioEurM', 'Sqft_m2', 'Rooms', 'Toilets'])
        #prediction = learn.predict(input_df)
        prediction = learn.predict(input_df.iloc[0])
        #output = {'prediction': str(prediction[0])}
        #output = {'Price': float(prediction[0])}
        output = {'Price': float(prediction[0]['Price'])}
        response = jsonify(output)
        return response
    except KeyError:
        return jsonify({'error': 'Invalid form data'})

if __name__ == "__main__":
    # Carga el modelo
    #model_path = "model.pkl"
    #model = load_model(model_path)
    # Inicia el servidor Flask
    app.run(debug=True, host='0.0.0.0')
