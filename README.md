#REST-architecture for Kurdi

A card is a word and its data:
	· id 
	· kurdish TEXT
	· danish TEXT
	· ipa TEXT
	· type TEXT
	· notes TEXT
	· category TEXT
	· views INT
	· score INT

GET 	/cards
GET		/cards/new
POST	/cards 	-d 'x=1'

GET 	/cards/id
DELETE	/cards/id
GET		/cards/id/edit
PUT		/cards/id	data for fields that need to be updated


