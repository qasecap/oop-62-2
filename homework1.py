class Hero:
    def __init__(self, nick, hp, lvl):
        self.nick = nick
        self.hp = hp
        self.lvl = lvl

    def action(self):
        return f"{self.nick} вызов священного орудия!"

    def level_up(self):
        self.lvl += 1
        return f"{self.nick} повысил уровень до {self.lvl}!"

yato = Hero(nick="Yato", hp=500, lvl=5)
yukine = Hero(nick="Yukine", hp=300, lvl=5)

print(yato.action())
print(yukine.action())

print(yato.level_up())

print(type(yato))