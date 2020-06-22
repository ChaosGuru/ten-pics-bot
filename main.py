import requests as rqs

def main():
    r = rqs.get('https://google.com')
    print(r.status_code)

if __name__ == '__main__':
    main()