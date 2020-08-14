import confluent_kafka
import uuid
import time


def confluent_kafka_consumer_performance():
    topic = 'test'
    msg_consumed_count = 0
    conf = {'bootstrap.servers': '172.20.10.10:9092',
            'group.id': 'test-consumer-group',
            'session.timeout.ms': 6000,
            'default.topic.config': {
                'auto.offset.reset': 'earliest'
            }
            }

    consumer = confluent_kafka.Consumer(**conf)
    print(consumer)

    consumer_start = time.time()
    # This is the same as pykafka, subscribing to a topic will start a background thread
    consumer.subscribe([topic])

    while True:
        msg = consumer.poll(1)
        if msg:
            msg_consumed_count += 1
            print(msg)

        if msg_consumed_count >= 10:
            break

    consumer_timing = time.time() - consumer_start
    consumer.close()
    return consumer_timing


if __name__ == "__main__":
    time_span = confluent_kafka_consumer_performance()
    print(time_span)
