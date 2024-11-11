import requests
import re
import json
from news_utils import store_data
import os

def crawl(brand):
    pageIndex = 1

    try:
        while pageIndex <= 50:
            url = "https://search-api-web.eastmoney.com/search/jsonp"
            params = {
                "cb": "jQuery351010870239735990794_1728918106327",
                "param": f'{{"uid":"","keyword":"{brand}","type":["cmsArticleWebOld"],"client":"web","clientType":"web","clientVersion":"curr","param":{{"cmsArticleWebOld":{{"searchScope":"default","sort":"default","pageIndex":{pageIndex},"pageSize":10,"preTag":"<em>","postTag":"</em>"}}}}}}',
                "_": "1728918106345"
            }

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }
            response = requests.get(url, params=params, headers=headers)

            # 去掉JSONP回调，提取纯JSON数据
            jsonp_data = response.text
            json_str = re.sub(r'jQuery[0-9_]+\(', '', jsonp_data)[:-1]

            # 解析JSON数据
            data = json.loads(json_str)['result']['cmsArticleWebOld']

            store_data(data, f'news/{brand}.txt')

            pageIndex += 1
    except Exception as e:
        print(e)
        print("未找到匹配的文本。")
        print("爬取结束。")

with open('brands.txt', 'r', encoding='utf-8') as file:
    brands = [brand.strip() for brand in file.readlines()]
    for brand in brands:
        file_path = f'news/{brand}.txt'
        if os.path.exists(file_path):
            print(f"{brand} 已经存在。")
            continue
        crawl(brand)