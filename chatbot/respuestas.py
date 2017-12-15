import requests

class Respuestas():
	def saluda(self,sender_id):
		JSON = {"messaging_type": "RESPONSE",
		"recipient":{
  		"id":sender_id
		},
		"message":{
  		"text":"Hola, ¿en qué te podemos ayudar? :)"
			}
		}

		URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAANTw325zN4BAJkZB9PAbDIaaS1dLmZCbVkATEAaiFGKhgWUnPKBzspqyYZCpPM0VyTCKdFrMmnAqtJqhfblAuRkaQJVSZBoGb8sNo4dUzfXGmdFRgdHoQQ2ksQ6fRT6ZA8ZCRw9HGIDIV6IIkFBlgydic7sBFoZBGpkESZAqkblAAZDZD'
		respuesta = requests.post(URL,json = JSON)
		return respuesta

	def servicio(self,sender_id):
		JSON = {"messaging_type": "RESPONSE",
		"recipient":{
  		"id":sender_id
		},
		"message":{
  		"text": "¡Si! ¡Te mandamos nuestro catálogo"
			}
		}

		URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAANTw325zN4BAJkZB9PAbDIaaS1dLmZCbVkATEAaiFGKhgWUnPKBzspqyYZCpPM0VyTCKdFrMmnAqtJqhfblAuRkaQJVSZBoGb8sNo4dUzfXGmdFRgdHoQQ2ksQ6fRT6ZA8ZCRw9HGIDIV6IIkFBlgydic7sBFoZBGpkESZAqkblAAZDZD'
		respuesta = requests.post(URL,json = JSON)
		return respuesta


	def generic(self,sender_id, lista_response):

		elementos = []
		payload_number = 0
		for k,v in lista_response[0].items():
			print(lista_response[0]['name_store'])
			payload_number = payload_number + 10
			x = {'title': lista_response[0]['name_store'],
			'image_url': lista_response[0]['cut_flowers'][0]['image_cutflower'],
			'subtitle': lista_response[0]['cut_flowers'][0]['name_cutflower'],
			'buttons':[{'type': 'postback', 'title':'Cotiza tu arreglo', 'payload': 220}]
			}
			elementos.append(x)
			elementos = elementos[0:9]
		JSON = {
  		"recipient":{
    	"id":sender_id,
    },
      "message":{
      "attachment":{
        "type":"template",
        "payload":{
        "template_type":"generic",
        "elements": elementos
              }
          }
        }
    }

		print(elementos)
		URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAANTw325zN4BAJkZB9PAbDIaaS1dLmZCbVkATEAaiFGKhgWUnPKBzspqyYZCpPM0VyTCKdFrMmnAqtJqhfblAuRkaQJVSZBoGb8sNo4dUzfXGmdFRgdHoQQ2ksQ6fRT6ZA8ZCRw9HGIDIV6IIkFBlgydic7sBFoZBGpkESZAqkblAAZDZD'
		respuesta = requests.post(URL,json = JSON)
		return respuesta


