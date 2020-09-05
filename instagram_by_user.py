import os
import re
import sys
import json
import time
import random
import requests
from hashlib import md5
from pyquery import PyQuery as pq

url_base = 'https://www.instagram.com/'
uri = 'https://www.instagram.com/graphql/query/?query_hash=a5164aed103f24b03e7b7747a2d94e3c&variables=%7B%22id%22%3A%22{user_id}%22%2C%22first%22%3A12%2C%22after%22%3A%22{cursor}%22%7D'

headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'cookie':
    'mid=W-ucPAAEAAHfHL6krlN9h6rAeAcZ; mcd=3; ig_did=C9B84CE5-C181-4D4C-B8BC-0D5919452C1E; shbid=15506; shbts=1599292902.46192; rur=VLL; csrftoken=IGP4k5Q1zCqYZHBAxTgs9e7HPhHRzLIr; ds_user_id=41324821423; sessionid=41324821423%3AEpEY7WYAYFlQso%3A6; urlgen="{\"58.153.26.120\": 4760}:1kETVz:QvuyyX7buFvZrnDhc5OpKWO6B-M"',
    'Connection': 'close'
}

requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数


def get_html(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print('请求网页源代码错误, 错误状态码：', response.status_code)
    except Exception as e:
        print(e)
        return None


def get_json(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            print('请求网页json错误, 错误状态码：', response.status_code)
    except Exception as e:
        print(e)
        time.sleep(60 + float(random.randint(1, 4000)) / 100)
        return get_json(url)


def get_content(url):
    try:
        s = requests.session()
        s.keep_alive = False  # 关闭多余连接
        response = s.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.content
        else:
            print('请求资源二进制流错误, 错误状态码：', response.status_code)
    except Exception as e:
        print(e)
        return None


def download(url, i):
    try:
        content = get_content(url)
        endw = 'mp4' if r'mp4?_nc_ht' in url else 'jpg'
        file_path = '/Users/yida/python/result/{0}/{1}.{2}'.format(
            user_name,
            md5(content).hexdigest(), endw)
        if not os.path.exists(file_path):
            with open(file_path, 'wb') as f:
                print(f'第{i + 1}条资源下载完成\n')
                f.write(content)
                f.close()
        else:
            print('第{0}条资源已存在\n'.format(i + 1))
    except Exception as e:
        print(e)
        print('第{0}条资源下载失败\n'.format(i + 1))


def get_url_from_edge(edge):
    if edge['node']['is_video']:
        video_url = edge['node']['video_url']
        if video_url:
            return video_url
    else:
        display_url = edge['node']['display_url']
        return display_url


def get_url_from_edge_multi(edge, i, urls):
    if "edge_sidecar_to_children" in edge["node"]:
        edge_sidecar_to_children = edge["node"][
            "edge_sidecar_to_children"]
        print('----第{0}条帖子资源数{1}------'.format(
            i + 1, len(edge_sidecar_to_children["edges"])))
        for edge_children in edge_sidecar_to_children["edges"]:
            if edge_children['node']['display_url']:
                source_url = get_url_from_edge(edge_children)
                urls.append(source_url)
    else:
        print('----第{0}条帖子资源数{1}------'.format(i + 1, 1))
        source_url = get_url_from_edge(edge)
        urls.append(source_url)

def get_urls(html):
    urls = []
    user_id = re.findall('"profilePage_([0-9]+)"', html, re.S)[0]
    print('user_name: {0}, user_id: {1}\n'.format(user_name, user_id))
    doc = pq(html)
    items = doc('script[type="text/javascript"]').items()
    for item in items:
        if item.text().strip().startswith('window._sharedData'):
            js_data = json.loads(item.text()[21:-1], encoding='utf-8')
            # print(f'js_data------: {json.dumps(js_data)}')
            edges = js_data["entry_data"]["ProfilePage"][0]["graphql"]["user"][
                "edge_owner_to_timeline_media"]["edges"]
            print('======帖子数{0}======\n '.format(len(edges)))
            page_info = js_data["entry_data"]["ProfilePage"][0]["graphql"][
                "user"]["edge_owner_to_timeline_media"]['page_info']
            cursor = page_info['end_cursor']
            flag = page_info['has_next_page']
            for i in range(len(edges)):
                edge = edges[i]
                get_url_from_edge_multi(edge, i, urls)
            print(cursor, flag)
    while flag:
        url = uri.format(user_id=user_id, cursor=cursor)
        js_data = get_json(url)
        infos = js_data['data']['user']['edge_owner_to_timeline_media'][
            'edges']
        print('======帖子数{0}======\n '.format(len(infos)))
        cursor = js_data['data']['user']['edge_owner_to_timeline_media'][
            'page_info']['end_cursor']
        flag = js_data['data']['user']['edge_owner_to_timeline_media'][
            'page_info']['has_next_page']
        for j in range(len(infos)):
            info = infos[j]
            get_url_from_edge_multi(info, j, urls)
        print(cursor, flag)
        # time.sleep(4 + float(random.randint(1, 800))/200)    # if count > 2000, turn on
    print('\n======总资源数{0}======\n '.format(len(urls)))
    return urls


def main(user):
    url = url_base + user + '/'
    html = get_html(url)
    urls = get_urls(html)
    dirpath = f'/Users/yida/python/result/{user}'
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    for i in range(len(urls)):
        print('------>>>正在下载第{0}条资源： '.format(i + 1) + urls[i],
              ' 还剩{0}条'.format(len(urls) - i - 1), '\n')
        download(urls[i], i)
        time.sleep(0.1)


if __name__ == '__main__':
    user_name = sys.argv[1]
    start = time.time()
    main(user_name)
    print('Complete!!!!!!!!!!')
    end = time.time()
    spend = end - start
    hour = spend // 3600
    minu = (spend - 3600 * hour) // 60
    sec = spend - 3600 * hour - 60 * minu
    print(f'一共花费了{hour}小时{minu}分钟{sec}秒')
