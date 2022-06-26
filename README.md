# csv-files-converter

### Description:
This project is a simple web application that transforms CSV files into specific formations. it was built using python language version: 3.10.5, Flask framework version: 2.1.2 in dockerized environment.

### How it works:
The website contains one page **upload page** that contains two methods:
- **uploading files**: users can upload a CSV file with a specific formation, and then they have the opportunity to download new converted CSV file.
- **test files**: users can use the test files that already exist where it will be converted to a new formated CSV file or to generate a test file then the application will convert it also.

### Run and install:
- extract the project's zip file.
- Build docker image named **csv-files-converter** for the project: `docker build -t csv-files-converter`
- create docker container that run on port 5000: `docker run -p 5000:5000 csv-files-converter`
- open localhost on your web browser with port 5000: `localhost:5000` it will redirect to the upload page `localhost:5000/upload`
