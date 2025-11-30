#!/usr/bin/env python
import pika
import sys
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='transacoes.suspeitas', exchange_type='fanout')

with open('transacoes.json',"r") as file:
    jsonData = json.load(file)
#    print(json.dumps(jsonData, indent=4))
jsonData = ''.join(sys.argv[1:]) or json.dumps(jsonData)    
channel.basic_publish(exchange='transacoes.suspeitas', routing_key='', body=jsonData)
#print(f" [x] Sent {jsonData}")
connection.close()
