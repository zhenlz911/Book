import pymysql
#创建数据库
class PymysqlDb():
    def __init__(self):
        self.db = pymysql.connect(host = 'localhost',
                                  port = 3306,
                                  user = 'root',
                                  password = '123456',
                                  db = 'LibraryManagement',
                                  charset = 'utf8')
        self.cursor = self.db.cursor()

    #创建数据库
    def create_db(self):
        self.cursor.execute('create database LibraryManagement')
        self.cursor.close()
        self.db.close()

    #创建数据表
    def create_table(self):

        #创建user表，studentid学号，password密码，isadmin是否为管理员，timesborrowed借阅次数，numborrowed已借书数量
        self.cursor.execute('create table User (StudentId char(10) unique not null,Name varchar(20),'
                            'PassWord char(32) not null,IsAdmin bit default 0,TimesBorrowed int default 0,'
                            'NumBorrowed int default 0)')
        #创建book，bookname书名，auth作者，category分类，bookid图书id，publisher出版社，publishertime出版时间，
        #numstorage库存量，numcanborrow可借量，numborrowed被借阅次数
        self.cursor.execute('create table Book (BookName varchar(30) not null,BookId char(6) not null,'
                            'Auth varchar(20) not null,Category varchar(10) default null,Publisher date,'
                            'PublisherTime date,Numstorage int default 0,NumCanBorrow int default 0,'
                            'NumBorrowed int default 0)')

        self.cursor.execute('create table User_Book(StudentId char(10) unique not null,BookId char(6) not null,'
                            'BorrowTime  DATE,ReturnTime DATE,BorrowState BIT DEFAULT 0)')

        self.cursor.execute('create table BuyOrDrop(BookId CHAR(6) NOT NULL,Time DATE,BuyOrDrop BIT DEFAULT 0,'
                            'Number INT DEFAULT 0)')
        #self.db.commit()
        self.cursor.close()
        self.db.close()

    def query(self,sql):
        self.cursor.execute(sql)
        row = self.cursor.fetchall()
        return row
        self.cursor.close()
        self.db.close()

    def insert_db(self,sql):
        self.cursor.execute(sql)
        self.db.commit()
        self.cursor.close()
        self.db.close()

    def deleteDb(self,sql):
        self.cursor.execute(sql)
        self.db.commit()
        self.cursor.close()
        self.db.close()

    def updateDb(self,sql):
        self.cursor.execute(sql)
        self.db.commit()
        self.cursor.close()
        self.db.close()










