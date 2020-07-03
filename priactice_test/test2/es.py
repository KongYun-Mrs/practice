from elasticsearch import Elasticsearch


class ES_search():
    def __init__(self, hosts):
        self.hosts = hosts
        self.ses = self.connect()

    def connect(self):
        try:
            es = Elasticsearch(self.hosts, timeout=30, max_retries=10, retry_on_timeout=True)
        except Exception as e:
            raise e
        return es

    def search(self):
        pass


s = ES_search(hosts='127.0.0.1:9200')
print s
