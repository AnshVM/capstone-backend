from flask import Flask, request, jsonify
import joblib  # Assuming you have a trained model saved as a joblib file
import features

app = Flask(__name__)

# Load your pre-trained ML model
model = joblib.load('mlp_xss_clf.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        url = data.get('url','')
        values = features.extract_features(url)
        predictions = model.predict([values])
        return jsonify({'prediction': '{}'.format(predictions[0]) })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)