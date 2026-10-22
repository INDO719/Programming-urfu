import random


class SpaceShip:
    def __init__(self, fuel: float, speed: float, condition_level: int):
        self.fuel = fuel
        self.speed = speed
        self.condition_level = condition_level
        self.condition = self.ship_condition(self.condition_level)

        self.mission = Mission()

    @staticmethod
    def ship_condition(level: int):
        if 1 <= level <= 2:
            return "Корабль не в состоянии лететь"
        elif 3 <= level <= 4:
            return "Корабль в критическом состоянии"
        elif 5 <= level <= 6:
            return "На корабле есть большие неполадки"
        elif 7 <= level <= 8:
            return "На корабле есть небольшие неполадки"
        elif 9 <= level <= 10:
            return "С кораблем все в порядке"
        else:
            return "Корабля больше нет"

    def condition_level_control(self, increase: int):
        self.condition_level += increase

    def fuel_control(self, increase: float):
        self.fuel += increase

    def speed_control(self, increase: float):
        self.speed += increase




class CrewMember:
    __skills = [
        {"Пилот": "Экономия топлива"},
        {"Инженер": "Астероидный щит"},
        {"Мусорщик": "Чистый рай"}
    ]

    def __init__(self, role: str, health: int) -> None:
        self.role = role
        self.skills = [self.__skills[self.role]]
        self.health = health

    def health_control(self, increase):
        self.health += increase

    def skills_control(self, skill):
        self.skills.append(skill)



class Mission:
    __goals = [{"goal": "Долететь до планеты B", "fuel": 100},
             {"goal": "Доставка корабля", "condition": 8},]
    __events = [{"event": "Метеорит", "place": "Топливный бак", "fuel": 30},
              {"event": "Пожар", "place": "Хранилище", "condition": 1},]

    def __init__(self) -> None:
        self.goal = random.choice(self.__goals)

    def get_goal(self) -> dict:
        return self.goal

    def get_event(self) -> dict:
        return random.choice(self.__events)


