from azure.storage.blob import BlobServiceClient

# Replace with your Azure connection string
connection_string = "<YOUR_CONNECTION_STRING>"
container_name = "mycontainer"
file_path = "sample.txt"
blob_name = "uploaded-sample.txt"

# Connect to Azure Blob Service
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# Upload file
with open(file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print("✅ File uploaded successfully to Azure Blob Storage!")