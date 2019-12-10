import json

fn = 'areas.json'
with open(fn, 'r', encoding='gbk') as f:
    jsonobj = json.load(f)

with open('provincesql.sql', 'r', encoding='gbk') as f:
    before = f.read()

    # for item in jsonobj['sources']:
    #     for item_i in item:
    #         for itme_j in item[item_i]:
    #             code = itme_j["id"]
    #             name = itme_j['name']
    #             pid = itme_j["pid"]
    #
    #             if pid == '0':
    #                 pid = 'NULL'
    #             sqlstring = f"INSERT INTO student_management_area VALUES('{code}','{name}','{pid}');\n"
    #             # print(sqlstring)
    #             f.write(sqlstring)
print(before.encode('iso-8859-1').decode('gbk'))