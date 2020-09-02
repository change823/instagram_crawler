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
    'ig_did=57ABBED0-CAA3-4D0C-A7F6-EB57CD0BAA72; mid=XvMi7QAEAAG76kCJAwavAxdX56l4; fbm_124024574287414=base_domain=.instagram.com; csrftoken=jCZ7idsf8yTPZuZELA1dUa0xgQF00sdR; ds_user_id=3602874642; sessionid=3602874642%3AampqMh97bmiE6E%3A29; shbid=15506; shbts=1598520402.4904773; rur=VLL; urlgen="{\"35.236.132.111\": 15169}:1kBZwc:jtBaFKo-I96omKsCbITDklKlEuU"',
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
        file_path = '/Users/yida/Crawler/result/{0}/{1}.{2}'.format(
            'by_url',
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
        edge_sidecar_to_children = edge["node"]["edge_sidecar_to_children"]
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
    doc = pq(html)
    items = doc('script[type="text/javascript"]').items()
    for item in items:
        if item.text().strip().startswith('window.__additionalDataLoaded'):
            js_data = json.loads(item.text()[48:-2], encoding='utf-8')
            print(f'js_data------: {json.dumps(js_data)}')
            edges = js_data["graphql"]["shortcode_media"][
                "edge_sidecar_to_children"]["edges"]
            print('======帖子数{0}======\n '.format(len(edges)))

            for i in range(len(edges)):
                edge = edges[i]
                get_url_from_edge_multi(edge, i, urls)

    print('\n======总资源数{0}======\n '.format(len(urls)))
    return urls


def main(url):
    html = get_html(url)
    urls = get_urls(html)
    dirpath = f'/Users/yida/Crawler/result/by_url'
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    for i in range(len(urls)):
        print('------>>>正在下载第{0}条资源： '.format(i + 1) + urls[i],
              ' 还剩{0}条'.format(len(urls) - i - 1), '\n')
        download(urls[i], i)
        time.sleep(0.1)


if __name__ == '__main__':
    url = sys.argv[1]
    if not url.endswith('/'):
        url = url + '/'
    start = time.time()
    main(url)
    print('Complete!!!!!!!!!!')
    end = time.time()
    spend = end - start
    hour = spend // 3600
    minu = (spend - 3600 * hour) // 60
    sec = spend - 3600 * hour - 60 * minu
    print(f'一共花费了{hour}小时{minu}分钟{sec}秒')