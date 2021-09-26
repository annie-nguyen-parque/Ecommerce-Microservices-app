import pika

params = pika.URLParameters('amqps://zecduogl:ITzRUmrbZiZSJKW42rXFUvDt857RTNnj@beaver.rmq.cloudamqp.com/zecduogl')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties) # publish in the main app