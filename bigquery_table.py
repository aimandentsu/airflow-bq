from google.cloud import bigquery
from google.oauth2 import service_account

def copy_bigquery():
    keypath = 'key/service_account.json'
    scope = ['https://www.googleapis.com/auth/cloud-platform',
             'https://www.googleapis.com/auth/bigquery',
             'https://www.googleapis.com/auth/bigquery.insertdata']
    
    credentials = service_account.Credentials.from_service_account_file(
        keypath, scopes = scope
    )

    client = bigquery.Client(credentials=credentials, project=credentials.project_id)

    source_table_id = 'project.dataset.table_name'
    destination_table_id = 'project.dataset.table_dest'

    job = client.copy_table(source_table_id, destination_table_id)
    job.result()

    # Done