from selenium import webdriver
from bs4 import BeautifulSoup
import os
from selenium.webdriver.support.ui import WebDriverWait

def fetch_chapter(driver, url):
    driver.get(url)
    WebDriverWait(driver, 10)  # 等待页面加载
    html_content = driver.page_source  # 获取页面源码
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text(separator="\n")  # 将 HTML 转为纯文本
    return text

def clean_text(text):
    text = text.split("发帖时间")[1]
    text = text.split("跳转至")[0]
    # 移除空行
    lines = [line for line in text.strip().split("\n") if line.strip()]
    # 移除最后五行
    if len(lines) > 5:
        text = "\n".join(lines[:-5])
    else:
        text = "\n".join(lines)
    return text

def main():

    for filename in os.listdir("data01"):
        if filename.endswith('.csv'):
            code = filename.split(".")[0]
            if os.path.exists(f'guba/{code}.txt'):
                print(f"{code} 已经存在。")
                continue
            driver = webdriver.Chrome()
            pageId = 1
            
            while pageId <= 40:
                try:
                    url = f'https://guba.eastmoney.com/list,{code},f_{pageId}.html'
                    text = fetch_chapter(driver, url)
                    cleaned_text = clean_text(text)
                    if cleaned_text:
                        with open(f'guba/{code}.txt', 'a', encoding='utf-8') as file:
                            file.write(cleaned_text)
                        print(f"第 {pageId} 页文本已成功写入文件。")
                        pageId += 1
                    else:
                        print("未找到第 {pageId} 文本内容。")
                except Exception as e:
                    print(f"第 {pageId} 页文本写入失败。")
                    print(e)
                    break
            
            # 关闭浏览器
            driver.quit()

if __name__ == "__main__":
    main()
