import os
import requests

api = {
    "MEDICARE_API": {
        "url": "https://data.cms.gov/data-api/v1/dataset/{dataset_id}/data",
        "datasets": {
            "nursing_home_dataset": "d086edc0-4953-4fb9-a663-b35526371add",
            "deficit_reduction_dataset": "01edb62e-5c45-4f43-8c91-16cba21cbb74"
        }
    }
}

def fetch_dataset(api_name: str, dataset_name: str):
    """Fetch a Medicare dataset by its name."""
    dataset_id = api[api_name]["datasets"][dataset_name]
    url = api[api_name]["url"].format(dataset_id=dataset_id)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def read_document(document_store: str, document_set: str, filename: str) -> str:
    doc_path = os.path.join(document_store, document_set, filename)
    if not os.path.isfile(doc_path):
        return "File not found."
    with open(doc_path, "r", encoding="utf-8") as f:
        return f.read()
    
def iter_document_filenames(document_store: str, category: str):
    doc_dir = os.path.join(document_store, category)
    if not os.path.isdir(doc_dir):
        return []
    return [f for f in os.listdir(doc_dir) if os.path.isfile(os.path.join(doc_dir, f))]