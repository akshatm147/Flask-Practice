from flask import *
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def file_upload():
    if request.method=='POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'File Uploaded Successfully'

if __name__ == '__main__':
    app.run(debug=True)
