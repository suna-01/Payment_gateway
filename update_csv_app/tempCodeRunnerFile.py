import os
current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.dirname(current_path)
upload_folder_path = os.path.join(parent_path, "static", "uploads")
app.config['UPLOAD_FOLDER'] = fr"{upload_folder_path}"
