# http://platform.wondershare.com/rest/v2/downloader/runtime/?client_sign={6C78A9C3-VB95-2721-9342-080027F47A94}&product_id=4222
# 4622 is the last

import requests
import xml.etree.ElementTree as ET
import time

start_time = time.time()
for i in range(1, 10000):
    key = '6C78A9C3-VB95-2721-9342-080027F47A94'
    not_i = 4222
    r = requests.get(f'http://platform.wondershare.com/rest/v2/downloader/runtime/?client_sign={key}&product_id={i}')
    root = ET.fromstring(r.content)
    info_ok = False
    product_ok = False

    for child in root.iter('*'):
        print("--- %s seconds ---" % round(time.time() - start_time))
        if child.tag == 'wsrp' and child.attrib['status'] == 'ok':
            info_ok = True
        if child.tag == 'name' and ('Filmora' in child.text):
            product_ok = True

        if info_ok and product_ok:
            print(i, 'is the right one')
            f = open("ex_ids.txt", "a")
            f.write(str(i) + "\n")
            f.close()
            break

print("--- %s seconds ---" % round(time.time() - start_time))
