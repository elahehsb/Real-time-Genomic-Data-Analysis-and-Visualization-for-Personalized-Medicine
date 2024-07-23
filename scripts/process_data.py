from Bio import SeqIO
from pymongo import MongoClient

# Initialize MongoDB client
client = MongoClient('mongodb://localhost:27017/')
db = client['genomic_data']
collection = db['sequences']

def process_genomic_data(file_path):
    sequences = []
    for record in SeqIO.parse(file_path, "fasta"):
        sequence = {
            "id": record.id,
            "description": record.description,
            "sequence": str(record.seq)
        }
        sequences.append(sequence)
    return sequences

def store_genomic_data(sequences):
    collection.insert_many(sequences)

# Process and store genomic data
file_paths = [f'data/sample{i}.fasta' for i in range(1, 4)]
for file_path in file_paths:
    sequences = process_genomic_data(file_path)
    store_genomic_data(sequences)
