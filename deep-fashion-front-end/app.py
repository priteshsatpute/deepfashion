from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

data = [
	{
		"companyName": "FlipKart", "site":"https://www.flipkart.com",
		"img": "https://picsum.photos/200/300?random=1",
		"desc": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
		"price": "Rs. 2500"
	},
	{
		"companyName": "FlipKart", "site":"https://www.flipkart.com",
		"img": "https://picsum.photos/200/300?random=2",
		"desc": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
		"price": "Rs. 2500"
	},
	{
		"companyName": "FlipKart", "site":"https://www.flipkart.com",
		"img": "https://picsum.photos/200/300?random=3",
		"desc": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
		"price": "Rs. 2500"
	},
	{
		"companyName": "FlipKart", "site":"https://www.flipkart.com",
		"img": "https://picsum.photos/200/300?random=4",
		"desc": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
		"price": "Rs. 2500"
	},
	{
		"companyName": "FlipKart", "site":"https://www.flipkart.com",
		"img": "https://picsum.photos/200/300?random=5",
		"desc": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
		"price": "Rs. 2500"
	},
	{
		"companyName": "FlipKart", "site":"https://www.flipkart.com",
		"img": "https://picsum.photos/200/300?random=6",
		"desc": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
		"price": "Rs. 2500"
	},
	{
		"companyName": "FlipKart", "site":"https://www.flipkart.com",
		"img": "https://picsum.photos/200/300?random=7",
		"desc": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
		"price": "Rs. 2500"
	},
	{
		"companyName": "FlipKart", "site":"https://www.flipkart.com",
		"img": "https://picsum.photos/200/300?random=8",
		"desc": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
		"price": "Rs. 2500"
	},
	{
		"companyName": "FlipKart", "site":"https://www.flipkart.com",
		"img": "https://picsum.photos/200/300?random=9",
		"desc": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
		"price": "Rs. 2500"
	},
	{
		"companyName": "FlipKart", "site":"https://www.flipkart.com",
		"img": "https://picsum.photos/200/300?random=10",
		"desc": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
		"price": "Rs. 2500"
	},
	{
		"companyName": "FlipKart", "site":"https://www.flipkart.com",
		"img": "https://picsum.photos/200/300?random=11",
		"desc": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
		"price": "Rs. 2500"
	},
	{
		"companyName": "FlipKart", "site":"https://www.flipkart.com",
		"img": "https://picsum.photos/200/300?random=12",
		"desc": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
		"price": "Rs. 2500"
	},
	{
		"companyName": "FlipKart", "site":"https://www.flipkart.com",
		"img": "https://picsum.photos/200/300?random=13",
		"desc": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
		"price": "Rs. 2500"
	},
	{
		"companyName": "FlipKart", "site":"https://www.flipkart.com",
		"img": "https://picsum.photos/200/300?random=14",
		"desc": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
		"price": "Rs. 2500"
	},
	{
		"companyName": "FlipKart", "site":"https://www.flipkart.com",
		"img": "https://picsum.photos/200/300?random=15",
		"desc": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
		"price": "Rs. 2500"
	},
	{
		"companyName": "FlipKart", "site":"https://www.flipkart.com",
		"img": "https://picsum.photos/200/300?random=16",
		"desc": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
		"price": "Rs. 2500"
	},
	{
		"companyName": "FlipKart", "site":"https://www.flipkart.com",
		"img": "https://picsum.photos/200/300?random=17",
		"desc": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
		"price": "Rs. 2500"
	}
]

@app.route("/", methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):
		return render_template("index.html")

@app.route("/getdata", methods = ['GET', 'POST'])
def getData():
	if(request.method == 'GET'):
		return jsonify(data)

if __name__ == '__main__':
	app.run(debug = True)