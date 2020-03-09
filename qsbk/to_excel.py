
import pandas as pd
import json


def json_to():
    lists = []
    with open('duanzi.json', 'r', encoding="utf-8") as f:
        for i in f.readlines():
            lists.append(json.loads(i))

        pf = pd.DataFrame(list(lists))
        columns = {
                        'title': '名称',
                        'content': '段子'
            }
        pf.rename(columns=columns, inplace=True)
        pf.to_excel('D:/段子.xlsx', encoding='utf-8', index=False)


if __name__ == '__main__':
    json_to()
