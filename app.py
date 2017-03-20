from flask import Flask

app = Flask(__name__)

@app.route('/friends', methods=['GET'])
def get_friends():
	return 'you don\'t have any friends'

if __name__ == '__main__':
	app.run()
