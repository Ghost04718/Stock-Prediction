from datetime import datetime

def store_data(data, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        for item in data:
            publication_date = datetime.strptime(item['date'], "%Y-%m-%d %H:%M:%S")
            if (publication_date.month == 10 and publication_date.day >= 28) or publication_date.month == 11:
                file.write(item['date'] + '\n')
                file.write(item['title'] + '\n')
                file.write(item['content'] + '\n')
                file.write(item['mediaName'] + ' ' + item['url'] + '\n\n')
                print(f"{publication_date}已成功写入{filename}。")