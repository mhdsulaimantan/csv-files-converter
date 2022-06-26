# csv-files-converter

### Overview:
This project is a web application that transforms CSV files into specific format. it built using python==3.10.5, Flask framework version: 2.1.2 in dockerized environment.
The website has an **upload page** that contains two methods:
1) Upload customised CSV file: Users can upload a CSV file with a specific format, and then they have the opportunity to download new transformed CSV file.
2) Samples files for testing:
   1. Users could use the build-in test files which will be transformed to the correct format.
   2. Users have the option to test using a generated random data which also will be tested and tranformed to the correct format.

### Build:
- Clone the repository `git clone repo`
- Build docker image: `docker build -t csv-files-converter .`

### Install:
- Create docker container that run on port 5000: `docker run -p 5000:5000 csv-files-converter`
- Open localhost on your web browser with port 5000: `localhost:5000` it will redirect to the upload page `localhost:5000/upload`
