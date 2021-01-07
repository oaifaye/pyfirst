# coding=utf-8
#================================================================
#
#   File name   : post_img.py
#   Author      : Faye
#   Created date: 2021/1/2 8:44 
#   Description :
#
#================================================================
import base64
import urllib.request
import urllib.parse
import json

def dopost(img_path):
    base_url = "https://ai.baidu.com/aidemo"
    data={
        "image": img2base64(img_path),
        "type": "https://aip.baidubce.com/rest/2.0/image-process/v1/image_definition_enhance"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "cookie": "BIDUPSID=A957C5ADEF41906FAAAB020CCCD0A132; PSTM=1586942357; BAIDUID=6A53E44135D683ABF5823C0B512010BE:SL=0:NR=50:FG=1; BDUSS=29Zc3V4bVpSbG9uWldhTTRvelJZUWloNEF3a35vZm9qeDY3S0k2R3lteUFLZVJmRVFBQUFBJCQAAAAAAAAAAAEAAAApT9Mgb2FpZmF5ZQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAICcvF-AnLxfM; BDUSS_BFESS=29Zc3V4bVpSbG9uWldhTTRvelJZUWloNEF3a35vZm9qeDY3S0k2R3lteUFLZVJmRVFBQUFBJCQAAAAAAAAAAAEAAAApT9Mgb2FpZmF5ZQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAICcvF-AnLxfM; __yjs_duid=1_6b3953b0f206b34dd8b7dd45def5197b1609286743900; MCITY=-332%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=6A53E44135D683ABF5823C0B512010BE:SL=0:NR=50:FG=1; BCLID=9322585924033595462; BDSFRCVID=pe_OJexroG3VSgJrNFwUKmu2SwH-P33TDYLEptww7unQ1ttVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR3KB6rtKRTffjrnhPF3K-LmXP6-hnjy3b7pbb3F-qrPfU5ohJ_K0n-nqJ0eJh3RymJ4QPb5bK3hDxDl5bO4y4Ldj4oxJpOJ-bCL0p5aHl51fbbvbURvD--g3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIE3-oJqC-aMCtm3j; BCLID_BFESS=9322585924033595462; BDSFRCVID_BFESS=pe_OJexroG3VSgJrNFwUKmu2SwH-P33TDYLEptww7unQ1ttVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; Hm_lvt_8b973192450250dd85b9011320b455ba=1608598520,1608598651,1608798288,1609548019; CAMPAIGN_TRACK=cp%3Aaipinzhuan%7Cpf%3Apc%7Cpp%3AAIpingtai%7Cpu%3Atitle%7Cci%3A%7Ckw%3A10005792; Hm_lpvt_8b973192450250dd85b9011320b455ba=1609548038; ab_sr=1.0.0_Y2M4M2YzZWE3YmNlMmVjYjI0OGQ4NmIxZjY2NjYwMDcyMWNjNDM3NGMwZDI4M2YwODQ0N2E0ZjViMzE1M2UxMGFiNDU1NjE2NjZlZTY0NDYyNGNiZDYzMGExOTZmOGNj; __yjsv5_shitong=1.0_7_a21020bd4460cba62ab1954317512c7a561e_300_1609548038225_111.30.61.13_d19aa724; delPer=0; PSINO=1; H_PS_PSSID=33425_1469_33403_33306_32970_33284_33286_33351_33313_33312_33311_33310_33335_33309_26350_33308_33307_33268_33370; BA_HECTOR=ag248l8h808lagal991fuvgf90r"
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
        text = open('res_img.jpg', "wb")
        text.write(res_image_data)
        text.close()
    else:
        print('失败:', res)

    # html=response.read().decode('utf-8')  #这里讲解一下decode()是把bytes转化解码为了 str ,
    # 但是写入文本的话，是不需要解码的，解码了str写不进去，



def img2base64(img_path):
    with open(img_path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
        data = 'data:image/jpeg;base64,%s'%s
        print(data)
        return data

if __name__ == '__main__':
    img_path = 'img.jpg'
    dopost(img_path)