# coding=utf-8
#================================================================
#
#   File name   : baidu_spider.py
#   Author      : Faye
#   Created date: 2021/1/2 8:44
#   Description : 薅百度图像风格转换羊毛  https://ai.baidu.com/tech/imageprocess/style_trans
#
#================================================================
import base64
import urllib.request
import urllib.parse
import json
import os
import time
import shutil
import cv2

def task(img_dir, target_dir, sleep=5):
    for root, dirs, files in os.walk(img_dir, target_dir):
        for name in files:
            try:
                img_path = os.path.join(root, name)
                img_copy_path = os.path.join(target_dir, name)
                font = os.path.splitext(name)[0]
                ext = os.path.splitext(name)[1]
                target_path = os.path.join(target_dir, font+"_shape"+ext)
                if (not os.path.exists(target_path) or not os.path.exists(img_copy_path)) and ext != '.gif':
                    print('img_path:', img_path)
                    msg = dopost(img_path, target_path)
                    if msg == 'success':
                        shutil.copy(img_path, img_copy_path)
                    elif msg == '请求Demo过于频繁':
                        now = int(time.time())  # 1533952277
                        timeArray = time.localtime(now)
                        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                        print(otherStyleTime)
                        time.sleep(10 * 60)
                    time.sleep(sleep)
            except Exception as e:
                print(e)

def dopost(img_path, target_path):
    base_url = "https://ai.baidu.com/aidemo"
    data={
        "image": img2base64(img_path),
        "type": "https://aip.baidubce.com/rest/2.0/image-process/v1/style_trans",
        "option": "color_pencil"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "cookie": "BIDUPSID=663470C50F19B781EDB5BEF9640CBB3C; PSTM=1559714206; MCITY=-332%3A; BAIDUID=5B36ECA438924FDC64A1921F27674EB0:FG=1; BDUSS=29TeEdXQS1mTEFXdVVQV0hRVzBpVX5LZXNxazRjcEhDZmVNR25yQjhBekkzaE5nRVFBQUFBJCQAAAAAAAAAAAEAAAApT9Mgb2FpZmF5ZQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMhR7F~IUexfa; BDUSS_BFESS=29TeEdXQS1mTEFXdVVQV0hRVzBpVX5LZXNxazRjcEhDZmVNR25yQjhBekkzaE5nRVFBQUFBJCQAAAAAAAAAAAEAAAApT9Mgb2FpZmF5ZQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMhR7F~IUexfa; CAMPAIGN_TRACK=cp%3Aaipinzhuan%7Cpf%3Apc%7Cpp%3AAIpingtai%7Cpu%3Atitle%7Cci%3A%7Ckw%3A10005792; BAIDUID_BFESS=5B36ECA438924FDC64A1921F27674EB0:FG=1; delPer=0; PSINO=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BCLID=9091312826571865553; BDSFRCVID=FkKOJexroG3VC0JeD98EKmu2SwH-P33TDYLEptww7unQ1ttVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR3KB6rtKRTffjrnhPF3Q4PUXP6-hnjy3b7p5KJF5l-Bbh5ohJ_K0n-nqJ0eJh3RymJ4QPb5bK3hDxDl5bO4y4Ldj4oxJpOJ-bCL0p5aHl51fbbvbURvD--g3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIE3-oJqC8bMD-93H; BCLID_BFESS=9091312826571865553; BDSFRCVID_BFESS=FkKOJexroG3VC0JeD98EKmu2SwH-P33TDYLEptww7unQ1ttVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tR3KB6rtKRTffjrnhPF3Q4PUXP6-hnjy3b7p5KJF5l-Bbh5ohJ_K0n-nqJ0eJh3RymJ4QPb5bK3hDxDl5bO4y4Ldj4oxJpOJ-bCL0p5aHl51fbbvbURvD--g3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIE3-oJqC8bMD-93H; __yjs_duid=1_4f03ea6bea1d2a5ce02c5ebdef3c35411617095969620; Hm_lvt_8b973192450250dd85b9011320b455ba=1615851289,1616134439,1617095969; Hm_lpvt_8b973192450250dd85b9011320b455ba=1617095999; __yjsv5_shitong=1.0_7_9ffbb46bc3a58bfcd617fd7395ec82fd4a59_300_1617096001550_111.30.61.13_340e2a54; H_PS_PSSID=33802_33817_33259_33344_33778_33759_33675_33392_33713_26350_33268_33795"
    }
    postdata = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url=base_url,headers=headers,data=postdata,method='POST')
    response=urllib.request.urlopen(req)
    html=response.read()
    res = json.loads(html)
    # text = open('G:/post.html', "wb")
    # text.write(html)
    # text.close()
    print('图像请求结果：', res['msg'])
    if res['msg'] == 'success':
        base64_data = res['data']['image'].replace("data:audio/x-mpeg;base64,", "")
        res_image_data = base64.b64decode(base64_data)
        text = open(target_path, "wb")
        text.write(res_image_data)
        text.close()
    else:
        if res['msg'] == 'image size error' or res['msg'] == 'image format error' or res['msg'] == '文件超过大小限制':
            shutil.move(img_path, '/data/baidu/remove/'+os.path.split(img_path)[1])
        print('失败:', res)
    return res['msg']

    # html=response.read().decode('utf-8')  #这里讲解一下decode()是把bytes转化解码为了 str ,
    # 但是写入文本的话，是不需要解码的，解码了str写不进去，

def img2base64(img_path):
    with open(img_path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
        data = 'data:image/jpeg;base64,%s'%s
        # print(data)
        return data

# 看文件是否成对
def check(target_dir, del_small=False):
    for f in os.listdir(target_dir):
        try:
            if f.find('_shape') != -1:
                blur_name = f.replace('_shape', '')
                if del_small:
                    img = cv2.imread(os.path.join(target_dir, blur_name))
                    if img.shape[0] < 256 or img.shape[1] < 256:
                        os.remove(os.path.join(target_dir, f))
                        os.remove(os.path.join(target_dir, blur_name))
                        print('del:', os.path.join(target_dir, f))
                        print('del:', os.path.join(target_dir, blur_name))
                        continue
                if not os.path.exists(os.path.join(target_dir, blur_name)):
                    print("no file:", blur_name)
                    os.remove(os.path.join(target_dir, f))
        except Exception as e:
            print(e)

if __name__ == '__main__':
    # img_path = 'img.jpg'
    # dopost(img_path)
    # img_dir = r'/data/baidu/004/'
    # target_dir = '/data/baidu/004_shape/'

    img_dir = r'F:/datasets/tiananmen/01'
    target_dir = 'F:/datasets/tiananmen/01_target'
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    task(img_dir, target_dir, sleep=1)

    # target_dir = '/data/baidu/baidu/'
    # check(target_dir, del_small=True)