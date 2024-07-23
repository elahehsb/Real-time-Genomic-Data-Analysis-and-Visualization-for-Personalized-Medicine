from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('models/genomic_disease_prediction_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    sequence = data['sequence']
    
    # Convert sequence to k-mers (example: k=3)
    kmers = sequence_to_kmers(sequence, k=3)
    feature_values = [kmers.count(kmer) for kmer in unique_kmers]  # unique_kmers should be defined

    prediction = model.predict(np.array([feature_values]))
    return jsonify({'disease_risk': prediction[0]})

def sequence_to_kmers(sequence, k=3):
    return [sequence[i:i+k] for i in range(len(sequence) - k + 1)]

if __name__ == '__main__':
    app.run(debug=True)
