from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    username = 'Test hero'
    level = 5
    health = 25.6
    damage = 10.2

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_attributes_types(self):
        self.assertIsInstance(self.username, str)
        self.assertIsInstance(self.level, int)
        self.assertIsInstance(self.health, float)
        self.assertIsInstance(self.damage, float)

    def test_enemy_same_username(self):
        enemy = Hero(self.username, self.level, self.health, self.damage)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_health_not_enough(self):
        self.hero.health = 0

        enemy = Hero("Some enemy", self.level, self.health, self.damage)

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

        self.hero.health -= 1
        with self.assertRaises(ValueError) as ve2:
            self.hero.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve2.exception))

    def test_enemy_health_not_enough(self):
        enemy = Hero("Some enemy", self.level, 0, self.damage)
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy)

        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(ve.exception))

        enemy.health -= 1
        with self.assertRaises(ValueError) as ve2:
            self.hero.battle(enemy)

        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(ve2.exception))

    def test_draw(self):
        enemy = Hero("Some enemy", self.level, self.health, self.damage)

        result = self.hero.battle(enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(-25.4, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_hero_wins(self):
        enemy = Hero("Some enemy", 1, 1, 1)

        result = self.hero.battle(enemy)
        self.assertEqual("You win", result)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(29.6, self.hero.health)
        self.assertEqual(15.2, self.hero.damage)

    def test_hero_loses(self):
        self.hero.health = 10
        self.hero.damage = 10
        enemy = Hero("Some enemy", 100, 100, 100)

        result = self.hero.battle(enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(101, enemy.level)
        self.assertEqual(55, enemy.health)
        self.assertEqual(105, enemy.damage)

    def test_str(self):
        expected = f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"

        self.assertEqual(expected, str(self.hero))


if __name__ == '__main__':
    main()
