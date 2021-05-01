import pymysql
import redis
from collections.abc import Iterable
from bson import ObjectId
from pymongo import MongoClient


def mysql_connect() -> None:
    """

    fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    fetchall(): 接收全部的返回结果行.
    rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
    """
    conn = pymysql.connect(host="127.0.0.1", user="root", password="mysql", database='test', port=3306)
    # 创建游标对象cursor
    cursor = conn.cursor()
    cursor.execute("select * from emp")
    print("返回的结果条数", cursor.rowcount)
    print(cursor.fetchall())  # cursor.fetchall()返回全部结果

    # 插入操作
    sql = r"INSERT INTO `test`.`emp`(`EMPNO`, `ENAME`, `JOB`, `MGR`, `HIREDATE`, `SAL`, `COMM`, `DEPTNO`) VALUES (7934, 'MILLER', 'CLERK', 7782, '1982-01-23', 1300, NULL, 10);"

    try:
        cursor.execute(sql)
        conn.commit()
        print("影响的行数", cursor.rowcount)
    except Exception as e:
        print(e)
        conn.rollback()

    # 插入语句执行fetchall 是不会返回影响的行数的
    print(cursor.fetchall())

    cursor.close()
    conn.close()
    return None


def redis_connect() -> None:
    conn = redis.StrictRedis(host="127.0.0.1", port=6379)
    conn.set("key", 666)
    print(bytes(conn.get("key")).decode(encoding="UTF-8"))
    conn.close()
    return None


def mongo_connect() -> None:
    conn = MongoClient(host="127.0.0.1", port=27017)
    # 连接数据库a
    db = conn.a
    res = db.tb1.find({})
    for i in res:
        print(i)
    db.tb1.insert({"_id":ObjectId("5e64dc95741f5c0fa88ba603"),"name":4545})
    conn.close()
    return None


# mysql_connect()
# redis_connect()
# mongo_connect()
