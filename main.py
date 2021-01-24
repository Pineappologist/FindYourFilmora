# http://platform.wondershare.com/rest/v2/downloader/runtime/?client_sign={6C78A9C3-VB95-2721-9342-080027F47A94}&product_id=4222
# 4622 is the last

import requests
import xml.etree.ElementTree as ET
import time

info_ok = False
product_ok = False
version_ok = False

# f = open("ids_9(3).txt", "x")
start_time = time.time()
for i in range(717, 4622):
    key = '6C78A9C3-VB95-2721-9342-080027F47A94'
    not_i = 4222
    r = requests.get(f'http://platform.wondershare.com/rest/v2/downloader/runtime/?client_sign={key}&product_id={i}')
    root = ET.fromstring(r.content)

    for child in root.iter('*'):
        print("--- %s seconds ---" % round(time.time() - start_time))
        if child.tag == 'wsrp' and child.attrib['status'] == 'ok':
            info_ok = True
        if child.tag == 'version' and str(child.text)[0:1] == '9':
            version_ok = True
        if child.tag == 'name' and ('Filmora' in child.text):
            product_ok = True

        if info_ok and product_ok and version_ok:
            print(i, 'is the right one')
            f = open("ids_9(3).txt", "a")
            f.write(str(i) + "\n")
            f.close()
            info_ok = False
            product_ok = False
            version_ok = False

        # print("--- %s seconds ---" % round(time.time() - start_time))
        # print(child.tag)
        # if child.tag == 'wsrp' and child.attrib['status'] == 'ok':
        #     for child3 in root.iter('*'):
        #         if child3.tag == 'name' and ('Filmora' in child3.text):
        #             for child2 in root.iter('*'):
        #                 if child2.tag == 'version' and str(child2.text)[0:1] == '8':
        #                     print('Filmora found!', 'id =', i)
        #                     f = open("ids.txt", "a")
        #                     f.write(str(i) + "\n")
        #                     f.close()

print("--- %s seconds ---" % round(time.time() - start_time))
