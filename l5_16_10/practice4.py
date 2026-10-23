import random


class SpaceShip:
    def __init__(self, fuel: float, speed: float, condition_level: int = 10):
        self.max_fuel = fuel
        self.fuel = fuel
        self.speed = speed
        self.condition_level = condition_level
        self.condition = self.ship_condition()

        self.mission = Mission()

    def ship_condition(self):
        if 1 <= self.condition_level <= 2:
            return "Корабль не в состоянии лететь"
        elif 3 <= self.condition_level <= 4:
            return "Корабль в критическом состоянии"
        elif 5 <= self.condition_level <= 6:
            return "На корабле есть большие неполадки"
        elif 7 <= self.condition_level <= 8:
            return "На корабле есть небольшие неполадки"
        elif 9 <= self.condition_level <= 10:
            return "С кораблем все в порядке"
        else:
            return "Корабля больше нет"

    def condition_level_control(self, increase: int):
        self.condition_level += increase

    def fuel_control(self, increase: float):
        if self.fuel + increase <= self.max_fuel:
            self.fuel += increase

    def speed_control(self, increase: float):
        self.speed += increase


class CrewMember:
    __skills = {
        "Пилот": ("Экономия топлива", 1),
        "Инженер": ("Астероидный щит", 1),
        "Мусорщик": ("Чистый рай", 1)
    }

    def __init__(self, role: str, health: int) -> None:
        self.role = role
        self.skill = self.__skills[self.role][0]
        self.skill_level = self.__skills[self.role][1]
        self.health = health

    def health_control(self, increase):
        self.health += increase

    def skills_control(self, increase):
        self.skill_level += increase


class Mission:
    __goals = [{"goal": "Долететь до планеты B", "fuel": 100},
             {"goal": "Доставка корабля", "condition": 8},]
    __events = [{"event": "Метеорит", "place": "Топливный бак", "fuel": -30},
              {"event": "Пожар", "place": "Хранилище", "condition": -2},]

    def __init__(self) -> None:
        self.goal = random.choice(self.__goals)

    def get_goal(self) -> dict:
        return self.goal

    def get_event(self) -> dict:
        return random.choice(self.__events)


ship = SpaceShip(1000, 1300)
print(ship.ship_condition())

bob1 = CrewMember("Пилот", 100)
bob2 = CrewMember("Инженер", 100)
bob3 = CrewMember("Мусорщик", 100)

print(bob1.role, bob1.skill)
print(bob2.role, bob2.skill)
print(bob3.role, bob3.skill)

bob1.skills_control(1)

mission = Mission()
print(mission.get_goal())

event = mission.get_event()
print(event)
if "fuel" in event:
    ship.fuel_control(event["fuel"] + bob1.skill_level * 20)
if "condition" in event:
    ship.condition_level_control(event["condition"] + bob3.skill_level * 1.25)

print(ship.fuel)
print(ship.ship_condition(), ship.condition_level)

