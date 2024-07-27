# Flask File Sharing Application

This documentation covers the implementation of a simple file-sharing web application using Flask. The application allows users to upload and download files. It uses the `waitress` server for serving the app in a production environment.

## Directory Structure

```
.
├── main.py
├── functions.py
├── templates
│   └── index.html
└── files
```

## main.py

The main entry point for the application.

## functions.py

Contains utility functions used by the main application.

### Endpoints

- **GET `/`**: Renders the home page displaying the list of files and the server's IP address.
- **POST `/`**: Handles file uploads.
- **GET `/download/<file>/`**: Handles file downloads.


### Functions

- **make_unique(file, files)**: Ensures that the uploaded file has a unique name by appending a UUID if a file with the same name already exists.
- **my_ip_address()**: Returns the IP address of the server.

## Running the Application

1. Ensure the directory structure is as described above.
2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

The application will be served on `http://0.0.0.0:8000`. Access it from your browser to upload and download files.
