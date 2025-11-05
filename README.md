# ☁️ Azure Cloud Storage Management System

This project demonstrates how to use **Microsoft Azure Blob Storage** to upload and manage files on the cloud securely.

## 🎯 Objective
To implement a basic cloud-based file storage system using Microsoft Azure services that allows users to upload and retrieve files through a web or command-line interface.

## ⚙️ Tools & Technologies
- Microsoft Azure Portal
- Azure Blob Storage
- Python (with Azure SDK)
- Visual Studio Code
- HTML, CSS (optional)

## 🧱 Architecture
User → Web Interface / Script → Azure Blob Storage → Cloud Storage Container

## 🚀 Setup Steps
1. Create a Resource Group in Azure
2. Create a Storage Account
3. Inside the account, create a Blob Container (Access: Private or Blob)
4. Generate the Connection String from Azure Portal
5. Copy the Python script and replace with your connection string

## 🐍 Python Script
```python
from azure.storage.blob import BlobServiceClient

connection_string = "<YOUR_CONNECTION_STRING>"
container_name = "mycontainer"
file_path = "sample.txt"
blob_name = "uploaded-sample.txt"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

with open(file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print("✅ File uploaded successfully to Azure Blob Storage!")
```

## 🧩 Future Enhancements
- Add web-based UI for file uploads
- Integrate with Azure Functions for automation
- Implement user authentication via Azure AD

## 👨‍💻 Author
**Ganta Dany Vikram**
MCA Student, Lovely Professional University
Passionate about Cloud Computing & Web Technologies
