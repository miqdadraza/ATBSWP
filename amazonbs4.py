import bs4, requests, pylint


def getAmazonPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#mediaNoAccordion > div.a-row > div.a-column.a-span7.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')
    return elems[0].text.strip() #strip will strip whitespace


#ideally this would display the price but since Amazon has changed their code this does raises an exception.

price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_1?dchild=1&keywords=automate+the+boring+stuff+with&qid=1605659482&sr=8-1')

print("Price is " + price)