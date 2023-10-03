class PhoneDTO():
    def __init__(self, phone: str):
        self.phone = phone
        self.__transform__()

    def __transform__(self):
        self.phone = self.phone.replace("-", "")
        self.phone = self.phone.replace(" ", "")
        self.phone = self.phone.replace("(", "")
        self.phone = self.phone.replace(")", "")
        if self.phone[0] == "8":
            self.phone = self.phone.replace("8", "7", 1)
        self.phone = "+" + self.phone

    def get_phone(self):
        return self.phone