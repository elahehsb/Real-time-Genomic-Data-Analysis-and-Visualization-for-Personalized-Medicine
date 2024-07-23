import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load processed data from MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['genomic_data']
collection = db['sequences']
data = pd.DataFrame(list(collection.find()))

# Convert sequences to numerical features (example: k-mer counting)
def sequence_to_kmers(sequence, k=3):
    return [sequence[i:i+k] for i in range(len(sequence) - k + 1)]

data['kmers'] = data['sequence'].apply(lambda seq: sequence_to_kmers(seq))

# Example of converting k-mers to features (simplified)
X = pd.get_dummies(data['kmers'].apply(pd.Series).stack()).sum(level=0)
y = data['disease']  # Assume disease labels are available

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Save the model
joblib.dump(model, 'models/genomic_disease_prediction_model.pkl')
