import confluent_kafka
import time

topic = 'test'


def confluent_kafka_producer_performance():
    topic = 'test'
    conf = {'bootstrap.servers': '172.20.10.10:9092'}
    producer = confluent_kafka.Producer(**conf)
    print(producer)
    messages_to_retry = 0
    msg_payload = 'This is message'

    producer_start = time.time()
    for i in range(10):
        try:
            producer.produce(topic, value=msg_payload)
            print(msg_payload)
        except BufferError as e:
            messages_to_retry += 1

    # hacky retry messages that over filled the local buffer
    for i in range(messages_to_retry):
        producer.poll(0)
        try:
            producer.produce(topic, value=msg_payload)
        except BufferError as e:
            producer.poll(0)
            producer.produce(topic, value=msg_payload)
    # producer.flush()
    return (time.time() - producer_start)


if __name__ == "__main__":
    time_span = confluent_kafka_producer_performance()
    print(time_span)
