#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
import requests
from respuestas import Respuestas

app = Flask(__name__)

ACCESS_TOKEN = 'EAANTw325zN4BAJkZB9PAbDIaaS1dLmZCbVkATEAaiFGKhgWUnPKBzspqyYZCpPM0VyTCKdFrMmnAqtJqhfblAuRkaQJVSZBoGb8sNo4dUzfXGmdFRgdHoQQ2ksQ6fRT6ZA8ZCRw9HGIDIV6IIkFBlgydic7sBFoZBGpkESZAqkblAAZDZD'
VERIFY_TOKEN = 'cintaroja'
@app.route('/')
def home():
	return 'Inicio del servidor'

@app.route('/webhook', methods = ['GET', 'POST'])
def webhook():
	if request.method == 'POST':
		mensaje = request.json
		print(mensaje)

		for event in mensaje['entry']:
			messaging = event ['messaging']
			for event_message in messaging:
				sender_id = event_message['sender']['id']
				try:
					message = event_message['message']['text']
					###pln = event_message['message']['nlp']['entities']['intent'][0]['value']
				except:
					message = "HOLA"

				print(message + 'por' + sender_id + " " + str("nlp"))
				respuestas = Respuestas()

				if message.upper() == 'HOLA':
					respuestas.saluda(sender_id)
				elif message.upper()  == 'TIENEN SERVICIO A DOMICILIO':
					respuestas.servicio(sender_id)
				elif message.upper() == 'OK':
					r = requests.get('http://95eae9c0.ngrok.io/api/v1/stores/details/')
					x = respuestas.generic(sender_id, r.json())
					#respuestas.quick(sender_id)
					print(x)
				#elif pln.upper() == 'QUIERO':
					#r = requests.get('http://824679b4.ngrok.io/api/v1/stores/details/')
					#respuestas.pln(sender_id, r.json())



		return 'ok'
	elif request.method == 'GET':
		if request.args.get('hub.verify_token') == VERIFY_TOKEN:
			return request.args.get('hub.challenge')
		return 'Verificar token'

if __name__ == '__main__':
	app.run(port = 5000, debug = True)