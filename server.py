from flask import Flask , render_template ,request
from werkzeug import secure_filename
from segmentation.segment import segmentImage
from segmentation.masksubtract import mask_subtract
from color_detection.k_means import detect_color
app = Flask(__name__)


@app.route('/',methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		f = request.files.get('file')
		if(f.filename == ''):
			return "No input image Provided!"
		else:
			f.save("received_images/"+secure_filename(f.filename))

			#segmentation[masked.png]
			segmentImage(f.filename)
			mask_subtract(f.filename , 'out.jpeg') 
			#color detection[]
			color_detected = detect_color('masked.png')
			return(str(color_detected))
			#feature detection [sleeves]

			#feature detection [pattern]

			#feature detection [collar]


	return render_template('index.html')


if __name__ == '__main__':
   app.run(host= '0.0.0.0',port=5000,debug=True)