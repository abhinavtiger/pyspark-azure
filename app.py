from flask import Flask, request, jsonify
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

# Set Azure Storage Connection string (or use environment variables)
connection_string = ''

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

@app.route('/list-files', methods=['GET'])
def list_files():
    folder = request.args.get('folder') 

    if not folder:
        return jsonify({"error": "Folder parameter is required!"}), 400  # Handle missing 'folder' parameter

    container_name = 'azure-assignment'

    try:
        # Get the container client and list blobs in the folder (prefix)
        blob_list = blob_service_client.get_container_client(container_name).list_blobs(name_starts_with=folder + "/")
        
        files = [blob.name for blob in blob_list]  # List all files in the folder
        return jsonify({"folder": folder, "files": files})

    except Exception as e:
        return jsonify({"error": str(e)}), 500 

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)