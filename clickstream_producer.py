from confluent_kafka import Producer
import json

producer = Producer({
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'clickstream_producer'
})

clickstream_data = {
    'user_id': '12345',
    'page_id': 'homepage',
    'timestamp': '2023-06-26T10:15:00',
    'action': 'click',
    'data': {
        'button_id': 'btn-1',
        'location': 'header'
    }
}

def delivery_report(err, msg):
    if err is not None:
        print(f'Failed to deliver message: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

producer.produce(
    topic='clickstream',
    key=None,
    value=json.dumps(clickstream_data),
    callback=delivery_report
)

producer.flush()
