from flask import Flask , render_template ,request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		f = request.files.get('file')
		f.save("received_images/"+secure_filename(f.filename))
		
		return "sas"

	return render_template('index.html')


if __name__ == '__main__':
   app.run(host= '0.0.0.0',port=5000,debug=True)