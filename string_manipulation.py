import requests
from bs4 import BeautifulSoup

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

cookies = {"HackThisSite": "2eed3nkvf2bkrfvqru2ir9mdl2"}
r = requests.get("https://www.hackthissite.org/missions/prog/12/", cookies=cookies)

soup = BeautifulSoup(r.text, 'html.parser')
input_tags = soup.find_all("input")
text_ = input_tags[0]
text = text_['value']

string = ""
prime_numbers = []
composite_numbers = []
for i in text:
    i_number = hasNumbers(i)
    if i_number:
        if int(i) > 1:
            i_is_prime = is_prime(int(i))
            if i_is_prime:
                prime_numbers.append(int(i))
            else:
                composite_numbers.append(int(i))
    else:
        string = string + i

prime_total = 0
for prime in prime_numbers:
    prime_total += prime

composite_total = 0
for composite in composite_numbers:
    composite_total += composite

product = prime_total * composite_total

new_string = ""
for char in string[:25]:
    ascii_value = ord(char) + 1
    new_string = new_string + chr(ascii_value)

solution = new_string + str(product)   

post_url = "https://www.hackthissite.org/missions/prog/12/index.php"
post_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "HackThisSite=2eed3nkvf2bkrfvqru2ir9mdl2",
    "Host": "www.hackthissite.org",
    "Origin": "https://www.hackthissite.org",
    "Referer": "https://www.hackthissite.org/missions/prog/12/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0"
}

payload = {"solution": solution, "submitbutton": "Submit+(remaining+time:+5+seconds)"}
r2 = requests.post(post_url, headers=post_headers, cookies=cookies, data=payload)

soup2 = BeautifulSoup(r2.text, 'html.parser')
print(soup2.body.prettify())