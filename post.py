import requests
import json
from config import *
from sqlighter import SQLighter
import time
import random
from config import *
from PIL import Image
import urllib.request
import io
from io import BytesIO
import os
import logging

logging.basicConfig(level=logging.INFO)

db = SQLighter('posts.db')

def write_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def main():
    #while True:
    for group in vk_group:
        print("Group " + group)
        wallGet = requests.get(url="https://api.vk.com/method/wall.get", params={
                                                                                "owner_id":group,
                                                                                "count":count_wallGet,
                                                                                "filter":filter_wallGet,
                                                                                "extended":extended_wallGet,
                                                                                "access_token": VK_API_USER,
                                                                                "v": VK_API_V
                                                                            })
        jsonWallGet = wallGet.json()
        for post in jsonWallGet['response']['items']:
            attachments_MSG = ""
            text = post['text']
            post_id = post['id']
            owner_id = post['owner_id']
            wall_id = str(owner_id) + "_" + str(post_id)
            if(str(text) == ""):
                text = None
            else:
                for stop in stop_list:
                    if(text.find(stop) != -1):
                        if(not(db.post_exists(wall_id))):
                            db.add_post(post_id, owner_id, text, wall_id, attachments_MSG, stop)
                for black in blacklist:
                    text = text.replace(black, "")
            attachments = None
            vk_photo = ""
            audio_url = ""
            if(str(post.keys()).find("attachments") != -1):
                attachments_MSG = ""
                attachments = post['attachments'][0]
                type_attachments = attachments['type']
                vk_photo = ""
                audio_url = ""
                photo_url = None
                doc_url = ""
                for type in post['attachments']:
                    type_attachments = type['type']
                    if(type_attachments == 'photo'):
                        #print(type['photo']['id'])
                        photo_url = None
                        photo_url = type['photo']['sizes'][-1]['url']
                        audio_url = ""
                        doc_url = ""
                    if(type_attachments == 'audio'):
                        audio_url = ""
                        audio_url = 'audio' + str(type['audio']['owner_id']) + '_' + str(type['audio']['id']) + ','
                        photo_url = None
                        doc_url = ""
                    if(type_attachments == 'doc'):
                        doc_url = ""
                        doc_url = 'doc' + str(type['doc']['owner_id']) + '_' + str(type['doc']['id']) + ','
                        photo_url = None
                        audio_url = ""
                    if(not(type_attachments == 'photo') and not(type_attachments == 'audio') and not(type_attachments == 'doc')):
                        if(not(db.post_exists(wall_id))):
                            db.add_post(post_id, owner_id, text, wall_id, attachments_MSG, None)
                    if(photo_url != None):
                        if(not(db.post_exists(wall_id))):
                            vk_ = download_img(photo_url)
                            vk_photo = vk_photo + photos_save(vk_)
            if(not(db.post_exists(wall_id))):
                attachments_MSG = attachments_MSG + str(vk_photo) + str(audio_url) + str(doc_url)
                db.add_post(post_id, owner_id, text, wall_id, attachments_MSG, None)
                print("kringe")
                if(text == None):
                    PARAMS = {
                        "owner_id":ownerId_wallPost,
                        "from_group":"1",
                        "attachments":attachments_MSG,
                        "access_token": VK_API_STADALONE,
                        "v": VK_API_V
                        }
                    wallGet = requests.get(url="https://api.vk.com/method/wall.post", params=PARAMS)
                    print("kd poshlo")
                    time.sleep(tSleep_post)
                    print("kd yshlo")
                else:
                    PARAMS = {
                        "owner_id":ownerId_wallPost,
                        "from_group":from_group_wallPost,
                        "message":text,
                        "attachments":attachments_MSG,
                        "access_token": VK_API_STADALONE,
                        "v": VK_API_V
                        }
                    wallGet = requests.get(url="https://api.vk.com/method/wall.post", params=PARAMS)
                    print("kd poshlo")
                    time.sleep(tSleep_post)
                    print("kd yshlo")
        time.sleep(tSleep_for)
    time.sleep(tSleep)
 
def photos_save(file_name):
    #try:
    upload_url = get_upload_server()
    file = {'file1':open(file_name, 'rb')}
    ur = requests.post(upload_url, files=file).json()

    r = requests.get('https://api.vk.com/method/photos.saveWallPhoto?', params={'group_id': ownerId_wallPost[1::],
                                                                      'server': ur['server'],
                                                                      'photo': ur['photo'],
                                                                      'hash': ur['hash'],
                                                                      'access_token': VK_API_STADALONE,
                                                                      'v': VK_API_V}).json()

    os.remove(file_name)
    owner_id = r['response'][0]['owner_id']
    photo_id = r['response'][0]['id']
    temp = 'photo' + str(owner_id) + '_' + str(photo_id) + ','
    return(temp)
    
def get_upload_server():
    #try:
    r = requests.get('https://api.vk.com/method/photos.getWallUploadServer', params={'group_id': ownerId_wallPost[1::],
                                                                                    'access_token': VK_API_STADALONE,
                                                                                    'v': VK_API_V}).json()
    return r['response']['upload_url']
    #except:
    #    pass

def download_img(url):
    #try:
    p = requests.get(url)
    rnd = str(random.randint(1, 999999999999))
    file_name = 'temp_img/' + rnd + '.jpg'
    out = open(file_name, "wb")
    out.write(p.content)
    out.close()
    file_edit = Image.open(file_name)
    watermark = Image.open('watermark.png')
    (width, height) = file_edit.size
    (width2, height2) = watermark.size

    water_widht = width - width2 - 15
    water_height = height - height2 - 15

    paste_mask = watermark.split()[3].point(lambda i: i * TRANSPARENCY / 100.)

    file_edit.paste(watermark, (water_widht, water_height), mask=paste_mask)
    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(im=file_edit, box=None)
    rndd = str(random.randint(1, 999999999999))
    file_name2 = 'temp_img/' + rndd + '.jpg'
    file_edit.save(file_name2, quality=95)
    file_edit.close()
    os.remove('temp_img/' + rnd + '.jpg')
    watermark.close()

    return(file_name2)
    #except:
    #    pass

if __name__ == '__main__':
    main()