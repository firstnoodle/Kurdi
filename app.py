from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = False

# GET FORM FOR ADDING NEW CARD
@app.route('/cards/new', methods=['GET'])
def new_card_form():
	return 'new card form'

# ADD NEW CARD
@app.route('/cards', methods=['POST'])
def add_new_card():
	word = request.form.get('word')
	return 'add ' + word

# GET CARD
@app.route('/cards/<int:id>', methods=['GET'])
def get_card(id):
	return 'get ' + str(id)

# GET FORM FOR EXISTING CARD
@app.route('/cards/<int:id>/edit', methods=['GET'])
def edit_card(id):
	return 'edit ' + str(id)

# UPDATE DATA TO EXISTING CARD
@app.route('/cards/<int:id>', methods=['PUT'])
def update_card(id):
	word = request.form.get('word')
	return 'update ' + str(id) + ' ' + word

# DELETE CARD
@app.route('/cards/<int:id>', methods=['DELETE'])
def delete_card(id):
	return 'delete ' + str(id)

# GET CARDS
@app.route('/cards', methods=['GET'])
def get_cards():
	return 'get cards'

@app.route('/practice')
def practice():
	return 'practice'


if __name__ == '__main__':
	app.run()
