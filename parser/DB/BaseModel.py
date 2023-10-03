from peewee import Model, MySQLDatabase

connection = MySQLDatabase("lebedevart", user="user", password="password",
                           port=3306, host="localhost")


class BaseModel(Model):

    class Meta:
        database = connection
        table_settings = ['DEFAULT CHARSET=utf8', 'ENGINE=innoDB']
