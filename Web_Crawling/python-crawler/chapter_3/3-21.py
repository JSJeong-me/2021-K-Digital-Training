class Shop:
    name = ""
    businessHours = ""
    def __init__(self,name,businessHours):
        self.name = name
        self.businessHours = businessHours
    def detail(self):
        print("가게 이름: " + self.name + ", 영업시간: " + self.businessHours)

shop = Shop("구름 국수", "9:00-19:00")
shop.detail() # 가게 이름: 구름 국수, 영업시간: 9:00-19:00