from urllib.request import urlopen
with urlopen('http://higpen.jellybean.jp/') as web_file:
    with open('download.html', 'wb') as local_file:
        local_file.write(web_file.read())