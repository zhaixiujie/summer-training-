import pymysql.cursors

# Connect to the database
# ahulock2018@47.96.175.196:3307
connection = pymysql.connect(host='47.96.175.196',
                             port= 3307,
                             user='root',
                             password='ahulock2018',
                             db='learning',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `xiuxiu`(`id`,`fullname`, `age`,`card`,`school`) VALUES (%s, %s,%s, %s, %s)"
        cursor.execute(sql, ('3', '李四','11',"90","安徽大学"))


    # connection is not autocommit by default. So you must commit to save
    # your changes.
        connection.commit()
    # with connection.cursor() as cursor:
    #     #Read a single record
    #     sql = "SELECT `chengji`, `name`,`xuehao` FROM `xj` WHERE `id`=%s"%(2)
    #     cursor.execute(sql)
    #     result = cursor.fetchone()
    #     print(result)

    # with connection.cursor() as cursor:
    #     sql="UPDATE xj SET  chengji=chengji+20 WHERE id = %s" % (2)
    #     cursor.execute(sql)
    #     connection.commit()
    # with connection.cursor() as cursor:
    #     sql = "DELETE FROM xj WHERE id = %s" % (5)
    #     cursor.execute(sql)
    #     connection.commit()



finally:
    connection.close()
