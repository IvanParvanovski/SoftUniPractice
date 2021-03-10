from flask import Flask, render_template, request
from werkzeug.datastructures import FileStorage
from converters.factories.ConverterFactory import ConverterFactory

app = Flask(__name__)
converter = ConverterFactory()


@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f: FileStorage = request.files['file']
        return converter.get_converter(f.content_type)\
            .convert_from_stream(f.stream)


if __name__ == '__main__':
    app.run(debug=True)
