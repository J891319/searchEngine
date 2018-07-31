index = []
page = ''
startLink = page.find("<a href=")
url = page[startLink + 9 : page.find('">', startLink)]
index.append(url)
print(index)
