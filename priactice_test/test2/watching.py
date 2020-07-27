import requests


def main():
    try:
        resp = requests.request(method='GET', url='http://10.47.121.15:8088/api/v1/licenses', timeout=10.0,
                                auth=("admin", "admin"))
        print resp.status_code
        if resp.status_code == 200:
            conten = resp.content
            print conten
    except Exception as e:
        print e
        return 'http/https ERROR'


if __name__ == '__main__':
    main()
