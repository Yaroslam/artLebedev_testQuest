from peewee import Model, PostgresqlDatabase

connection = PostgresqlDatabase("lebedevart", user="user", password="password",
                           port=5432, host="app_postgres")


class BaseModel(Model):

    class Meta:
        database = connection
        table_settings = ['DEFAULT CHARSET=utf8', 'ENGINE=innoDB']
