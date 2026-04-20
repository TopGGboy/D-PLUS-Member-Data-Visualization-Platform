from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
import pymysql


# Create your views here.
def plushome(request):
    return render(request, "plushome.html")


def plus_useredu(request):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         database='jdplus')
    cursor = db.cursor()
    cursor.execute("select edu,count(*) as num from plus_user group by edu;")
    data = cursor.fetchall()
    user_edu = []
    for i in data:
        user_edu.append({'edu': i[0], 'num': i[1]})

    cursor.close()
    db.close()
    return HttpResponse(json.dumps(user_edu))


# 用户城市
def plus_usercity(request):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         database='jdplus')
    cursor = db.cursor()
    cursor.execute("select city,count(*) as num from plus_user group by city;")
    data = cursor.fetchall()
    user_edu = []
    for i in data:
        print(i[0], '  ', i[1])
        user_edu.append({'city': i[0], 'num': i[1]})

    cursor.close()
    db.close()
    return HttpResponse(json.dumps(user_edu))


# 用户性别
def plus_usersex(request):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         database='jdplus')
    cursor = db.cursor()
    cursor.execute("select sex,count(*) as num from plus_user group by sex;")
    data = cursor.fetchall()
    user_edu = []
    for i in data:
        print(i[0], '  ', i[1])
        user_edu.append({'sex': i[0], 'num': i[1]})

    cursor.close()
    db.close()
    return HttpResponse(json.dumps(user_edu))


# PLUS累计在籍会员数趋势分析
def plus_acc(request):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         database='jdplus')
    cursor = db.cursor()
    cursor.execute("select date,forming_cnt as num from M3 limit 10;")
    data = cursor.fetchall()
    user_edu = []
    for i in data:
        user_edu.append({'date': i[0].strip()[5:], 'forming_cnt': i[1][3:]})

    cursor.close()
    db.close()
    return HttpResponse(json.dumps(user_edu))


# PLUS在籍会员中新会员VS老会员比例
def plus_old_new_plus(request):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         database='jdplus')
    cursor = db.cursor()
    cursor.execute("select is_1st,count(is_1st) as num from M1 group by is_1st ;")
    data = cursor.fetchall()
    user_edu = []
    for i in data:
        print(i[0], '  ', i[1])
        if i[0] == 0:
            user_edu.append({'is_1st': '老会员', 'num': i[1]})
        else:
            user_edu.append({'is_1st': '新会员', 'num': i[1]})
    cursor.close()
    db.close()
    return HttpResponse(json.dumps(user_edu))


# PLUS累计在籍会员数趋势分析
def plus_user_times(request):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         database='jdplus')
    cursor = db.cursor()
    cursor.execute("select times,count(times) as num from M1 group by times;")
    data = cursor.fetchall()
    user_edu = []
    for i in data:
        user_edu.append({'times': i[0], 'num': i[1]})

    cursor.close()
    db.close()
    return HttpResponse(json.dumps(user_edu))


# PLUS会员每日各状态（拉新、续费、召回）开通会员数分析
def plus_uds(request):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         database='jdplus')
    cursor = db.cursor()
    cursor.execute("select date,add_1st_form_cnt,renew_form_cnt,Loss_renew_form_cnt as num from M3 limit 20;")
    data = cursor.fetchall()
    user_edu = []
    for i in data:
        user_edu.append({
            'date': i[0],
            'add_1st_form_cnt': i[1],
            'renew_form_cnt': i[2],
            'Loss_renew_form_cnt': i[3]
        })

    cursor.close()
    db.close()
    return HttpResponse(json.dumps(user_edu))
