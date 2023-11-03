from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import joblib  # Assuming you have a trained model saved as a joblib file
import features

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Load your pre-trained ML model
model = joblib.load('mlp_xss_clf.joblib')

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    try:
        data = request.json
        print("Recieved json: ",data)
        url = data.get('url','')
        print("url: ",url)
        values = features.extract_features(url)
        predictions = model.predict([values])
        return jsonify({'prediction': '{}'.format(predictions[0]) })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)