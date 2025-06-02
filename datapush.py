from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

storage_account_key = <Storage-account-key>
storage_account_name = <Storage-account-name>
connection_string = <Connection-Endpoint>
container_name = <Container-name>

def uploadToBlobStorage(file_path,file_name):
   blob_service_client = BlobServiceClient.from_connection_string(connection_string)
   blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
   with open(file_path,'rb') as data:
      blob_client.upload_blob(data)
      print(f'Your {file_name} is successfully Uploaded to azure container .')

# calling a function to perform upload
uploadToBlobStorage(file_path, file_name)
