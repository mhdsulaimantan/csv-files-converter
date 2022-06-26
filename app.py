from flask import Flask, redirect, render_template, request, send_file
from gevent.pywsgi import WSGIServer
from csv_convert.convertCSV import Convert

app = Flask(__name__)


@app.route('/')
def home():
    return redirect('upload')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # information will be send to the client side
    info = {'file': None,
            'msg': None,
            'error': None}

    if request.method == 'POST':
        # send the file to the client when click download
        if request.values.get("file"):
            return send_file(request.values.get("file"), as_attachment=True)

        # client upload csv file
        csv_file = request.files['csv_file']

        # check if the uploaded file's type is CSV
        if csv_file.filename.endswith('.csv'):

            # convert the uploaded file
            info['file'] = Convert(csv_file).create_new_file()
            
            if info['file'] is None:
                info['error'] = "Wrong type of formation. Please follow this formation:\n(id: digit,release date: yyyy/mm/dd,game name: mass-effect-3,country code: ISO 3166 alpha-3,copies sold: digit,price: digit + 'USD')"
            else:
                info['msg'] = "Your file was uploaded successfully. You can now download the transformed file."
        
        else:
            info['error'] = "Please upload the right type of files (.csv)"

    # method type is GET
    else:
        # if a test value sent from the client
        if request.values.get('test'):
            # convert the picked test file

            info['file'] = Convert(request.values.get('test'), True).create_new_file()

            # try to enter a file that is not exist
            if info['file'] is None:
                info['error'] = "Test File not found"
            else:
                info['msg'] = "The test file was converted. You can now download transformed file"

    return render_template('upload.html', info=info)


if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    
    # Production
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()