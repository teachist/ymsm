import sys
import json
import os
import re
from urllib import request
from bs4 import BeautifulSoup
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/'
header = {
    'Cookie': 'AD_RS_COOKIE=20080917',
    'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \ AppleWeb\Kit/537.36 (KHTML, like Gecko)\ '
                  'Chrome/58.0.3029.110 Safari/537.36'}
# header = {}


class GetHttp:
    def __init__(self, url, headers=None, charset='gbk'):
        if headers is None:
            headers = {}
        self._response = ''
        try:
            print(url)
            self._response = request.urlopen(
                request.Request(url=url, headers=headers))
        except Exception as e:
            print(e)
        self._c = charset

    @property
    def text(self):
        try:
            return self._response.read().decode(self._c)
        except Exception as e:
            print(e)
            return ''



def write_to_file(dicts):
    filename = 'areas.json'
    with open(filename, 'a', encoding='gbk') as f:
        json.dump(dicts, f, ensure_ascii=False)

results = dict(
    {
        'provinces': [],
        'cities': [],
        'towns': [],
        'contries': [],
        'villages': [],
    }
)


def provincetr(u, he, lists):
    # 获取全国省份和直辖市
    t = GetHttp(u, he, 'gbk').text

    if t:
        soup = BeautifulSoup(t, 'html.parser')
        for i in soup.find_all(attrs={'class': 'provincetr'}):
            for a in i.find_all('a'):
                id = re.sub(r"\D", "", a.get('href'))
                lists[id] = {'id': id, 'name': a.text, 'pid': '0', 'code': id}
                results['provinces'].append(
                    {'id': id, 'name': a.text, 'pid': '0', 'code': id})
    write_to_file(results['provinces'])
    return lists


def citytr(u, he, lists):
    # 获取省下级市
    l = lists.copy()
    o = {}
    for i in l:
        t = GetHttp(u + i + '.html', he, 'gbk').text
        if not t:
            continue
        soup = BeautifulSoup(t, 'html.parser')
        for v in soup.find_all(attrs={'class': 'citytr'}):
            id = str(v.find_all('td')[0].text)
            if id[0:4] not in lists.keys():
                o[id[0:4]] = {'id': id[0:4], 'name': str(
                    v.find_all('td')[1].text), 'pid': i, 'code': id}
                results['cities'].append({'id': id[0:4], 'name': str(
                    v.find_all('td')[1].text), 'pid': i, 'code': id})
    write_to_file(results['cities'])

    return o


def countytr(u, he, lists):
    # 获取市下级县
    l = lists.copy()
    o = {}
    for i in l:
        t = GetHttp(u + i[0:2] + '/' + i + '.html', he, 'gbk').text
        if not t:
            continue
        soup = BeautifulSoup(t, 'html.parser')
        for v in soup.find_all(attrs={'class': 'countytr'}):
            id = str(v.find_all('td')[0].text)
            if id[0:6] not in lists.keys():
                o[id[0:6]] = {'id': id[0:6], 'name': str(
                    v.find_all('td')[1].text), 'pid': i, 'code': id}
                results['contries'].append({'id': id[0:6], 'name': str(
                    v.find_all('td')[1].text), 'pid': i, 'code': id})
    write_to_file(results['contries'])
    return o


def towntr(u, he, lists):
    # 县下级镇
    l = lists.copy()
    o = {}
    for i in l:
        t = GetHttp(u + i[0:2] + '/' + i[2:4] +
                    '/' + i + '.html', he, 'gbk').text
        if not t:
            continue
        soup = BeautifulSoup(t, 'html.parser')
        for v in soup.find_all(attrs={'class': 'towntr'}):
            id = str(v.find_all('td')[0].text)
            if id[0:9] not in lists.keys():
                o[id[0:9]] = {'id': id[0:9], 'name': str(
                    v.find_all('td')[1].text), 'pid': i, 'code': id}
                results['towns'].append({'id': id[0:9], 'name': str(
                    v.find_all('td')[1].text), 'pid': i, 'code': id})
    write_to_file(results['towns'])

    return o


def villagetr(u, he, lists):
    # 镇下级村
    l = lists.copy()
    o = {}
    for i in l:
        t = GetHttp(u + i[0:2] + '/' + i[2:4] + '/' +
                    i[4:6] + '/' + i + '.html', he, 'gbk').text
        if not t:
            continue
        soup = BeautifulSoup(t, 'html.parser')
        for v in soup.find_all(attrs={'class': 'villagetr'}):
            id = str(v.find_all('td')[0].text)
            if id[0:12] not in lists.keys():
                o[id[0:12]] = {'id': id[0:12], 'name': str(
                    v.find_all('td')[2].text), 'pid': i, 'code': id}
                results['villages'].append({'id': id[0:12], 'name': str(
                    v.find_all('td')[2].text), 'pid': i, 'code': id})
    write_to_file(results['villages'])

    return o


p = provincetr(u=url, he=header, lists={})
print('省', p)
c = citytr(u=url, he=header, lists=p)
# print('市', c)
o = countytr(u=url, he=header, lists=c)
# print('县', o)
t = towntr(u=url, he=header, lists=o)
# print('镇', t)
v = villagetr(u=url, he=header, lists=t)
# print('村', v)



# sqlfile = 'areas.sql'
# with open(sqlfile, 'w') as f:
