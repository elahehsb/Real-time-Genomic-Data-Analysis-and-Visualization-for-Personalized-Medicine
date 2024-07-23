import requests
import os

def download_genomic_data():
    base_url = 'https://example.com/genomic-data'
    sample_ids = ['sample1', 'sample2', 'sample3']
    for sample_id in sample_ids:
        url = f'{base_url}/{sample_id}.fasta'
        response = requests.get(url)
        with open(f'data/{sample_id}.fasta', 'wb') as file:
            file.write(response.content)

os.makedirs('data', exist_ok=True)
download_genomic_data()
