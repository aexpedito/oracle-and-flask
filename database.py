import cx_Oracle
from sqlalchemy import create_engine

class OracleDB:
    def __init__(self):
        self.username='SANDBOX'
        self.password='pirad2'
        self.hostname='localhost'
        self.port='1521'
        self.sid='XE'
        self.engine=None
        self.conn=None
        self.rconn=None

    def connect(self):
        try:
            self.engine = create_engine('oracle://SANDBOX:pirad2@127.0.0.1:1521/XE')
            self.conn = self.engine.connect()
            self.rconn = self.engine.raw_connection()
        except cx_Oracle.DatabaseError as e:
            self.engine=None
            print(e)
            exit(1)

    def select(self):
        res = self.conn.execute("select * from tb_user")
        payload = []
        content = {}
        for result in res:
            content = {'id': result[0], 'username':result[1]}
            payload.append(content)
            content = {}
        return payload
