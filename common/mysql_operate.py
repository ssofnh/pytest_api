import pymysql
from common.logger import logger


class MysqlDb():

    def __init__(self, db_conf):
        if db_conf is None:
            return
        try:
            # 通过字典拆包传递配置信息，建立数据库连接
            self.conn = pymysql.connect(**db_conf, autocommit=True)
            # 通过 cursor() 创建游标对象，并让查询结果以字典格式输出
            self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        except pymysql.Error as e:
            logger.error("Failed to connect to MySQL: {}".format(e))
            raise

    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

    def select_db(self, sql, params=None):
        '''查询'''
        try:
            # 检查连接是否断开，如果断开就进行重连
            self.conn.ping(reconnect=True)
            # 使用 execute() 执行sql，并将参数值作为参数传递给 execute() 方法
            self.cur.execute(sql, params)
            # 使用 fetchall() 获取查询结果
            data = self.cur.fetchall()
            return data
        except pymysql.Error as e:
            logger.error("MySQL query error: {}".format(e))
            raise

    def execute_db(self, sql, params=None):
        """更新/新增/删除"""
        try:
            # 检查连接是否断开，如果断开就进行重连
            self.conn.ping(reconnect=True)
            # 使用 execute() 执行sql
            self.cur.execute(sql, params)
            # 提交事务
            self.conn.commit()
        except pymysql.Error as e:
            logger.info("操作MySQL出现错误，错误原因：{}".format(e))
            print("操作MySQL出现错误，错误原因：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()
            raise
