import requests
import re
import json
import os
'''
headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Origin': 'https://y.qq.com',
    'Referer': 'https://y.qq.com/n/yqq/playsquare/6555387822.html',
    #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    
    }
    param={
       "g_tk": "5381",
       "loginUin": "0",
       "hostUin": "0"
       "format": "json"
       "inCharset": "utf8"
       "outCharset": "utf-8"
       "notice": "0"
       "platform": "yqq.json"
       "needNewCode": "0"
       "data": {"req":{"module":"CDN.SrfCdnDispatchServer",
                     "method":"GetCdnDispatch","param":
                     {"guid":"6346363002","calltype":0,"userip":""}},
              "req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey",
                       "param":{"guid":"6346363002","songmid":
                                ["004F6Mxm4XvTgI"],"songtype":[0],
                                "uin":"0","loginflag":1,"platform":"20"}},
              "comm":{"uin":0,"format":"json","ct":24,"cv":0}}
       }
       param={
    "g_tk": "5381",
    "loginUin": "0",
    "hostUin": "0",
    "format": "json",
    "inCharset": "utf8",
    "outCharset": "utf-8",
    "notice": "0",
    "platform": "yqq.json",
    "needNewCode": "0",
    
    "data": "{"+"req"+":"+"{"+"module"+":"+"CDN.SrfCdnDispatchServer"+","+"method"+":"+"GetCdnDispatch"+","+"param"+":"+"{"+"guid"+":"+"6346363002"+","+"calltype"+":"+"0"+","+"userip"+":"+"}}"+","+"req_0"+":"+"{"+"module"+":"+"vkey.GetVkeyServer"+","+"method"+":"+"CgiGetVkey"+","+"param"+":"+"{"+"guid"+":"+"6346363002"+","+"songmid"+":"+"["+"004F6Mxm4XvTgI"+"]"+","+"songtype"+":"+"["+"0"+"]"+","+"uin"+":"+"0"+","+"loginflag"+":"+"1"+","+"platform"+":"+"20"+"}},"+"comm"+":"+"{"+"uin"+":"+"0"+","+"format"+":"+"json"+","+"ct"+":"+"24,"+"cv"+":"+"0}}",
    }
    '''

#获取歌曲列表

def get_list():
    headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Origin': 'https://y.qq.com',
    'Referer': 'https://y.qq.com/n/yqq/playsquare/6555387822.html',
    #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    
    }
    url="https://c.y.qq.com/qzone/fcg-bin/fcg_ucc_getcdinfo_byids_cp.fcg?type=1&json=1&utf8=1&onlysong=0&disstid=6555387822&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0"
    response=requests.get(url,headers=headers)
    data=response.text
    jd=json.loads(data)
    #print('INDENT',json.dumps(jd,sort_keys=True,indent=2))
    list=jd["cdlist"][0]["songlist"]
    #print(list)
    print(len(list))
    print(type(list))
    return list
   
def download(url,filename):
    headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Origin': 'https://y.qq.com',
    'Referer': 'https://y.qq.com/n/yqq/playsquare/6555387822.html',
    #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    
    }
    current_path=os.path.abspath('.')
    response=requests.get(url,headers=headers).content
    #print(current_path)
    with open(filename+".mp3","wb") as f:
        f.write(response)

def get_vkey(songmid):
    headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Origin': 'https://y.qq.com',
    'Referer': 'https://y.qq.com/n/yqq/playsquare/6555387822.html',
    #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    
    }
    #request=requests.get("https://u.y.qq.com/cgi-bin/musicu.fcg?",headers=headers,params=param)
    request=requests.get("https://u.y.qq.com/cgi-bin/musicu.fcg?g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22req%22%3A%7B%22module%22%3A%22CDN.SrfCdnDispatchServer%22%2C%22method%22%3A%22GetCdnDispatch%22%2C%22param%22%3A%7B%22guid%22%3A%226346363002%22%2C%22calltype%22%3A0%2C%22userip%22%3A%22%22%7D%7D%2C%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%226346363002%22%2C%22songmid%22%3A%5B%22"+songmid+"%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%220%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A0%2C%22format%22%3A%22json%22%2C%22ct%22%3A24%2C%22cv%22%3A0%7D%7D",headers=headers)
    data=request.text
    jd=json.loads(data)
    vkey=jd["req_0"]["data"]["midurlinfo"][0]["vkey"]
    return vkey

def get_m4a(vkey,songmid):
    url="http://isure.stream.qqmusic.qq.com/C400"+songmid+".m4a?guid=6346363002&vkey="+vkey+"&uin=0&fromtag=66"
    return url
def run():
    list=get_list()
    i=0
    n=len(list)
    while i < n:
        songmid=list[i]["songmid"]
        filename=list[i]["songname"]
        vkey=get_vkey(songmid)
        url=get_m4a(vkey,songmid)
        
        print(i,url)
        download(url,filename)
        i=i+1

def main():
    run()
if __name__=='__main__':
    main()
    

    

    




    

    









    




