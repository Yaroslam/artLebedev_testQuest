import asyncio
import aiofiles
from aiocsv import AsyncReader
import re
from DTOs.PhoneDTO import PhoneDTO
from DB.CertifiedSpecialistModel import CertifiedSpecialistModel


def fillRow(row: list, needLen: int) -> list:
    if len(row) < needLen:
        while len(row) != needLen:
            row.append('')
    return row


def groupEmail(emailGroups: list[list]) -> str:
    res = ''
    for group in emailGroups:
        for match in group:
            res += match
        if len(emailGroups) > 1:
            res += " "
    return res.strip()


def getEmail(row: list) -> str | None:
    emailRegExp = r"((?!\.)[\w\-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])"
    email = "Отсутствует"
    emailMathes = re.findall(emailRegExp, row[5])
    if len(emailMathes) > 0:
        email = groupEmail(emailMathes)
    return email

def groupPhone(phoneGroup: list[str]) -> str:
    res = ''
    for number in phoneGroup:
        phone = PhoneDTO(number)
        clear_number = phone.get_phone()
        res+=clear_number + " "
    return res.strip()

def getPhoneNumber(row: list) -> str | None:
    # [0-9]{11}  +79529920647 89159815399
    # [0-9]{4}\s[0-9]{3}\s[0-9]{2}\s[0-9]{2} 8922 209 29 67
    # [0-9]-[0-9]{3}-[0-9]{3}-[0-9]{4} 8-931-314-0447
    # [0-9]{4}-[0-9]{3}-[0-9]{2}-[0-9]{2} 8905-548-75-29
    phone = "Отсутствует"
    phoneRes = ''
    phoneRegExp = [r"[0-9]{11}", r"[0-9]{4}\s[0-9]{3}\s[0-9]{2}\s[0-9]{2}", r"[0-9]-[0-9]{3}-[0-9]{3}-[0-9]{4}",
                   r"[0-9]{4}-[0-9]{3}-[0-9]{2}-[0-9]{2}", r"[0-9]\([0-9]{3}\)[0-9]{7}",
                   r"[0-9]-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}"]
    for regExp in phoneRegExp:
        phoneMathes = re.findall(regExp, row[5])
        if len(phoneMathes) > 0:
            phoneRes += groupPhone(phoneMathes)
    if phoneRes != '':
        phone = phoneRes
    return phone

async def main():
    async with aiofiles.open("./table.csv", mode="r", encoding="utf-8", newline="") as afp:
        async for row in AsyncReader(afp):
            if row[0] != 'Фамилия, имя, отчество аттестованного специалиста':
                row = fillRow(row, 6)
                email = getEmail(row)
                phone = getPhoneNumber(row)
                fio = row[0].strip()
                living_place = row[1].strip() if row[1] != '' else "Отсутствует"
                specialization = row[2].strip()
                category = row[3].strip() if row[3] != '' else "Отсутствует"
                category_order = row[4].strip() if row[4] != '' else "Отсутствует"
                CertifiedSpecialistModel.create(
                    fio=fio,
                    living_place=living_place,
                    specialization=specialization,
                    email=email,
                    phonenumber=phone,
                    category=category,
                    category_order=category_order
                )

asyncio.run(main())

