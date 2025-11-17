import json

from requests import Session

data = '{"tests": [{"name":"Login","status":"PASS"},{"name":"API","status":"FAIL"}]}'

parsed = json.loads(data)

fails = list(filter(lambda t: t['status'] == "FAIL", parsed['tests']))

print(fails[0]['name'])
# what
# ll
# be
# the
# output


def fun(x, lst=[]):
    lst.append(x ** 2)
    print(len(lst))
    return sum(lst) / len(lst)

print(fun(2))
#print(fun("3"))

# JSON data
data = {
  "name": "John Doe",
  "job": "QA Engineer",
  "email": "john.doe@example.com",
  "id": "101",
  "createdAt": "2025-11-05T08:20:43.511Z",
  "skills": ["Java", "Selenium", "API Testing"]
}

print(data['skills'][1])

import  requests

s = Session()

r_post = requests.post("https://www.example.com",data= data)
requests.post(url="https://www.amazon.in",json=data)
print(r_post.text)
#assert  r_post.status_code == 201


#
# with open("",r) as f:
#     f.read()
#
# import pandas as pd
# data = pd.read_excel("Sheetname",)
#
# import json
#
# data = '{"tests": [{"name":"Login","status":"PASS"},{"name":"API","status":"FAIL"}]}'
#
# parsed = json.loads(data)
#
# fails = list(filter(lambda t: t['status'] == "FAIL", parsed['tests']))
#
# print(fails[0]['name'])
# what
# ll
# be
# the
# output


def fun(x, lst=[]):
    lst.append(x ** 2)
    print(len(lst))
    return sum(lst) / len(lst)


print(fun(2))
#print(fun("3"))

# {
#
#     "name": "John Doe",
#
#     "job": "QA Engineer",
#
#     "email": "john.doe@example.com",
#
#     "id": "101",
#
#     "createdAt": "2025-11-05T08:20:43.511Z"
#                  "skills": ["Java", "Selenium", "API Testing"]
#
# }
#file path = C:\Users\ravig\OneDrive\Documents

import pandas as pd
# df = pd.read_excel("C:\\Users\\ravig\\OneDrive\\Documents\\CustomerData.xlsx",engine="openpyxl")
# print(df.head(5))
# print(df['LastName'])
# print(df['Address'])

def read_data_excel(filepath: str, sheet_name : str = "Sheet1"):
    try:
        df = pd.read_excel(filepath, sheet_name=sheet_name)
        print(f"Successfully read Excel file: {filepath}")
        return  df
    except FileNotFoundError:
        print("Please check the Filepath")
    except PermissionError:
        print("File is Open or Locked, close it and retry")
    except Exception as e:
        print(f"Excel reading error {e}")

print(read_data_excel("C:\\Users\\ravig\\OneDrive\\Documents\\CustomerData.xlsx",sheet_name="Sheet1"))

from re import  sub
sentence = 'hello#$%world welcome@!#$%to python*&^%'
result = sub(r"[a-zA-Z0-9\s]",'*',sentence)
print(result)

def fibo_check(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        series = fibo_check(n-1)
        series.append((series[-1] + series[-2]))
    return series

print(fibo_check(5))



