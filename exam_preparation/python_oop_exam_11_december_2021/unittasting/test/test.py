from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self):
        self.team1 = Team("Gosho")
        self.team2 = Team("Pesho")

    def test_init_team(self):
        self.assertEqual("Gosho", self.team1.name)
        self.assertEqual("Pesho", self.team2.name)
        self.assertEqual({}, self.team1.members)

    def test_name_property(self):
        with self.assertRaises(ValueError) as ex:
            self.team1.name = "Gosho56"
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member(self):
        self.team1.members = {"Gosho": 20, "Jon": 30}
        self.team1.add_member(Joro=35)
        self.assertEqual({"Gosho": 20, "Jon": 30, "Joro": 35}, self.team1.members)
        self.team1.add_member(Gosho=20)
        self.assertEqual({"Gosho": 20, "Jon": 30, "Joro": 35}, self.team1.members)
        self.assertEqual("Successfully added: Betty", self.team1.add_member(Betty=35))
        self.assertEqual({"Gosho": 20, "Jon": 30, "Joro": 35, "Betty": 35}, self.team1.members)

    def test_remove_member(self):
        self.team1.members = {"Gosho": 20, "Jon": 30, "Joro": 35}
        self.team1.remove_member("Gosho")
        self.assertEqual({"Jon": 30, "Joro": 35}, self.team1.members)
        self.assertEqual("Member Jon removed", self.team1.remove_member("Jon"))
        self.assertEqual({"Joro": 35}, self.team1.members)
        self.assertEqual("Member with name Jordan does not exist", self.team1.remove_member("Jordan"))
        self.assertEqual({"Joro": 35}, self.team1.members)

    def test___gt__(self):
        self.team1.members = {"Jon": 30, "Joro": 35}
        self.team2.members = {"Gosho": 20, "Jon": 30, "Joro": 35}
        self.assertFalse(self.team1.__gt__(self.team2))
        self.team2.members = {"Jon": 30, "Joro": 35}
        self.team1.members = {"Gosho": 20, "Jon": 30, "Joro": 35}
        self.assertTrue(self.team1.__gt__(self.team2))

    def test___len__(self):
        self.team1.members = {"Gosho": 20, "Jon": 25}
        self.assertEqual(2, self.team1.__len__())

    def test___add__(self):
        self.team1.new_team = Team("Asan")

        self.assertEqual(self.team1.new_team, self.team1.__add__(self.team2))


    def test___str__(self):
        pass



if __name__ == "__main__":
    main()

