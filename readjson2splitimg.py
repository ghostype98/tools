# -*- coding: utf-8 -*-
# @Time     : 2/16/22 2:45 PM
import os
import json
import shutil

#{"images": [{"id": 0, "file_name": "VOC2007/JPEGImages/budaodian180924104841.jpg",
def get_jsname(jsfile, jspath):
    f = open(os.path.join(jspath, jsfile))
    sf = json.load(f)       #将字符串转化为字典
    #print(sf['images'])
    nas = []
    for i, n in enumerate(sf['images']):
        na = n['file_name']

        nas.append(na)
    return nas

def main():
    #遍历json
    for f in os.listdir(js_path):
        dir_na = f.split('.')[0].split('_')[1]
        juedui_pt = os.path.join(out_path, dir_na)
        if not os.path.exists(juedui_pt):
             os.mkdir(os.path.join(out_path, dir_na))
        name_list = get_jsname(f, js_path)
        print(len(name_list))

        for n in name_list:
            n = n.split('/')[2]
            if n in os.listdir(img_path):
                shutil.copy(os.path.join(img_path, n), os.path.join(out_path, dir_na))
            else:
                print('no file in img_path')
                print(n)
        print(f)

if __name__ == '__main__':
    js_path = '/home/michael/PycharmProjects/mmdet0214/data/coco/annotations/'
    img_path = '/home/michael/PycharmProjects/mmdet0214/data/VOCdevkit/VOC2007/JPEGImages/'
    out_path = '/home/michael/PycharmProjects/mmdet0214/data/coco/'

    main()





