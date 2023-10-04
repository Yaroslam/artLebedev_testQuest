Установка

1. docker pull
2. docker run -p 8000:8000 yaroslam/artlebedev-testquest

В образе будет создана база данных lebedevart в MySQL, создана таблица certified\_specialist\_cultar\_objects\_preservation, создан пользователь user с паролем password установлен репозиторий, установлены зависимости, собраны данные из таблицы [https://opendata.mkrf.ru/opendata/7705851331-certified\_specialist](https://opendata.mkrf.ru/opendata/7705851331-certified_specialist) и записаны в таблицу lebedevart. certified\_specialist\_cultar\_objects\_preservation

Документация к api

GET /api/CertifiedSpecialistCultarPreservation/\<int:id\> - выбирает запись с id равным переданному id, возвращает данные об этой записи, в случае, если такой записи нет, вернет 404 статус код

Пример запроса

Запрос – http://localhost:8000/api/CertifiedSpecialistCultarPreservation/100

Ответ – {'id': 100,

'fio': 'Каширина Лариса Сергеевна',

'living\_place': 'Томск',

'specialization': 'архитектор (направление – проектные работы по реставрации и консервации объектов культурного наследия)',

'category': 'III категория',

'category\_order': '№241 от 4.03.2019',

'email': 'lisi4ka.tomsk@gmail.com',

'phonenumber': 'Отсутствует'

}

Запрос [http://localhost:8000/api/CertifiedSpecialistCultarPreservation/100000](http://localhost:8000/api/CertifiedSpecialistCultarPreservation/100000)

Ответ 404

GET /api/CertifiedSpecialistCultarPreservation/getMany?[filters, ordering] – выбирает множество записей согласно переданным фильтрам, возвращает массив этих записей, упорядоченный согласно переданному параметру упорядочивания

Filters

filters.category={string} – фильтрует данные согласно переданной категории, в качестве параметра возможна любая строка, фильтр осуществляет поиск этой подстроки в строке категории

filters.email={string} - фильтрует данные согласно переданной электронной почте, в качестве параметра возможна любая строка, фильтр осуществляет поиск этой подстроки в строке электронной почты

filters.fio={string} - фильтрует данные согласно переданному ФИО, в качестве параметра возможна любая строка, фильтр осуществляет поиск этой подстроки в строке ФИО

filters.living\_place={string} - фильтрует данные согласно переданному месту жительства, в качестве параметра возможна любая строка, фильтр осуществляет поиск этой подстроки в строке места жительства

filters.order={string} – фильтрует данные согласно переданному номеру приказа, в качестве параметра возможна любая строка, фильтр осуществляет поиск подстроки №{string} в строке приказа

filters.order.date.day={string} – фильтрует данные согласно переданному дню, в качестве параметра передается номер дня в месяце в формате DD

filters.order.date.mounth={string} – фильтрует данные согласно переданному номеру месяца, в качестве параметра передается номер месяца в формате MM

filters.order.date.year={string} – фильтрует данные согласно переданному года, в качестве параметра передается год в формате YYYY

filters.phone={string} – фильтрует данные согласно переданному номеру телефона, в качестве параметра передается строка цифр, в случае фильтрации по полному номеру телефона необходимо придерживаться формата +7XXXXXXXXXX

filters.specialization ={string} – фильтрует данные согласно переданной специализации, в качестве параметра передается любая строка, фильтр осуществляет поиск подстроки string в строке специализации

Ordering

sort=orderparam;orderparam2;orderparam3 – сортирует выбранные согласно переданным параметрам orderparam, сортировка осуществляется в порядке переданных параметров, для сортировки по параметру в порядке убывания параметр необходимо передать в формате -orderparam, в ином случае сортировка будет в порядке возврастания. Возможныепараметрыдлясортировки – id, fio, living\_place, specialization, category, category\_order, email, phonenumber

Пример запроса

Запрос – [http://localhost:8000/api/CertifiedSpecialistCultarPreservation/getMany?filters.email=gmail&filters.phone=980](http://localhost:8000/api/CertifiedSpecialistCultarPreservation/getMany?filters.email=gmail&filters.phone=980)

Ответ – [

{

"id": 9707,

"fio": "Смирнова Софья Юрьевна",

"living\_place": "г. НижнийНовгород",

"specialization": "архитектор",

"category": "III категория",

"category\_order": "№ 558 от 13.04.2022",

"email": "9801083723sofia@gmail.com",

"phonenumber": "+79801083723"

}

]

Запрос – [http://localhost:8000/api/CertifiedSpecialistCultarPreservation/getMany?filters.email=gmail&sort=fio;-id](http://localhost:8000/api/CertifiedSpecialistCultarPreservation/getMany?filters.email=gmail&sort=fio;-id)

Ответ – [

{

"id": 6288,

"fio": "Абраамян Фрида Вагаршаковна",

"living\_place": "г. Санкт-Петербург",

"specialization": "архитектор",

"category": "III категория",

"category\_order": "№10 от 13.01.2020",

"email": "frida.ida26@gmail.com",

"phonenumber": "+79217775989"

},

{

"id": 6452,

"fio": "Авдусина Татьяна Викторовна",

"living\_place": "Москва",

"specialization": "художник-реставратор архивных документов (направление – переплеты)",

"category": "высшаякатегория",

"category\_order": "№2184 от 12.12.2018",

"email": "avdusina.t@gmail.com",

"phonenumber": "Отсутствует"

},

{

"id": 6453,

"fio": "Аверина Татьяна Федоровна",

"living\_place": "Москва",

"specialization": "архитектор (направление – проектные работы по реставрации и консервации объектов культурного наследия)",

"category": "высшаякатегория",

"category\_order": "№2184 от 12.12.2018",

"email": "tata7741411@gmail.com",

"phonenumber": "Отсутствует"

},

…

]