# from flask import Flask, request, jsonify
# from azure.storage.blob import BlobServiceClient
# import os

# app = Flask(__name__)

# connect_str = 'DefaultEndpointsProtocol=https;AccountName=abhi1storage;AccountKey=IZuOEWTJz43scAc2KkBKmJn3OV5gB8ziCmjS4LxIjHYTsu9qvkRoqlvJXaSNb7IyUGMHWU25wZE3+AStI2X5hw==;EndpointSuffix=core.windows.net'
# container_name = "azure-assignment"
# blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# @app.route('/list-files')
# def list_files():
#     folder = request.args.get('folder')
#     blob_list = blob_service_client.get_container_client(container_name).list_blobs(name_starts_with=folder + "/")
#     files = [blob.name for blob in blob_list]
#     return jsonify(files)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')


from flask import Flask, request, jsonify
from azure.storage.blob import BlobServiceClient
import os

app = Flask(__name__)

# Set your Azure Storage Connection string (or use environment variables)
connection_string = 'DefaultEndpointsProtocol=https;AccountName=abhi1storage;AccountKey=IZuOEWTJz43scAc2KkBKmJn3OV5gB8ziCmjS4LxIjHYTsu9qvkRoqlvJXaSNb7IyUGMHWU25wZE3+AStI2X5hw==;EndpointSuffix=core.windows.net'

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

@app.route('/list-files', methods=['GET'])
def list_files():
    folder = request.args.get('folder')  # Get the 'folder' parameter from the URL query string

    if not folder:
        return jsonify({"error": "Folder parameter is required!"}), 400  # Handle missing 'folder' parameter

    # Assuming your container name is 'mycontainer'
    container_name = 'azure-assignment'

    try:
        # Get the container client and list blobs in the folder (prefix)
        blob_list = blob_service_client.get_container_client(container_name).list_blobs(name_starts_with=folder + "/")
        
        files = [blob.name for blob in blob_list]  # List all files in the folder
        return jsonify({"folder": folder, "files": files})

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return an error if something goes wrong

if __name__ == "__main__":
    app.run(debug=True)
