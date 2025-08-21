from flask import Flask, Response
import os

app = Flask(__name__)
file_path = '/shared/myfile.txt'
#file_path = os.getenv('DATA_FILE_PATH', '/default/path/if/not/set.txt')

@app.route('/')
def read_file():
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        return Response(content, mimetype='text/plain')
    else:
        return Response("File not found", status=404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
