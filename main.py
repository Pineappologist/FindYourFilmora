# http://platform.wondershare.com/rest/v2/downloader/runtime/?client_sign={6C78A9C3-VB95-2721-9342-080027F47A94}&product_id=4222

import requests
import xml.etree.ElementTree as ET
import time

# f = open("ids.txt", "x")
start_time = time.time()
for i in range(1, 4622):
    key = '6C78A9C3-VB95-2721-9342-080027F47A94'
    not_i = 846
    r = requests.get(f'http://platform.wondershare.com/rest/v2/downloader/runtime/?client_sign={key}&product_id={i}')
    root = ET.fromstring(r.content)

    # optimize this!
    #  |
    #  |
    #  V

    # ---------------------------------------------------------------
    # for child in root.iter('*'):
    #     print("--- %s seconds ---" % round(time.time() - start_time))
    #     # print(child.tag)
    # # if child.tag == 'wsrp' and child.attrib['status'] == 'ok':
    #   #     for child3 in root.iter('*'):
    #   #         if child3.tag == 'name' and ('Filmora' in child3.text):
    #   #             for child2 in root.iter('*'):
    #   #                 if child2.tag == 'version' and str(child2.text)[0:1] == '8':
    #   #                     print('Filmora found!', 'id =', i)
    #   #                     f = open("ids.txt", "a")
    #   #                     f.write(str(i) + "\n")
    #   #                     f.close()
    # ---------------------------------------------------------------

print("--- %s seconds ---" % round(time.time() - start_time))
