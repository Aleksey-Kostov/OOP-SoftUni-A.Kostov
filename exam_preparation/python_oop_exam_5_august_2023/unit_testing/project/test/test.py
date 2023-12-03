from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar("Seat", "Sedan", 100000, 20000.00)

    def test_init(self):
        self.assertEqual("Seat", self.car.model)
        self.assertEqual("Sedan", self.car.car_type)
        self.assertEqual(100000, self.car.mileage)
        self.assertEqual(20000, self.car.price)

    def test_init_type(self):
        self.assertIsInstance(self.car.model, str)
        self.assertIsInstance(self.car.car_type, str)
        self.assertIsInstance(self.car.mileage, int)
        self.assertIsInstance(self.car.price, float)

    def test_getter_price(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0
        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_getter_mileage(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 99
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    def test_set_promotional_price_with_exception_higher(self):
        with self.assertRaises(ValueError) as ve1:
            self.car.set_promotional_price(21000)
        self.assertEqual("You are supposed to decrease the price!", str(ve1.exception))

    def test_set_promotional_price_with_exception_equal(self):
        with self.assertRaises(ValueError) as ve1:
            self.car.set_promotional_price(20000)
        self.assertEqual("You are supposed to decrease the price!", str(ve1.exception))

    def test_set_promotional_price_with_not_exception(self):
        new_price = self.car.set_promotional_price(10000)
        self.assertEqual(10000, self.car.price)
        self.assertEqual("The promotional price has been successfully set.", new_price)

    def test_need_repair_with_repair_impossible(self):
        self.car.repair_price = 15000
        self.assertEqual('Repair is impossible!', self.car.need_repair(self.car.repair_price, "test"))

    def test_need_repair_with_repair(self):
        self.car.repair_price = 5000
        self.car.need_repair(self.car.repair_price, "test")
        self.assertEqual(25000, self.car.price)
        self.assertEqual(['test'], self.car.repairs)
        self.assertEqual("Price has been increased due to repair charges.",
                         self.car.need_repair(self.car.repair_price, "test"))

    def test_diff_car_type(self):
        self.car2 = SecondHandCar("BMW", "Test", 100000, 20000.00)
        self.assertEqual('Cars cannot be compared. Type mismatch!', self.car.__gt__(self.car2))

    def test_same_car_type(self):
        self.car2 = SecondHandCar("BMW", "Sedan", 100000, 20000.00)
        self.assertEqual(self.car.price > self.car2.price, self.car.__gt__(self.car2))

    def test_string(self):
        self.assertEqual(f"""Model {self.car.model} | Type {self.car.car_type} | Milage {self.car.mileage}km
Current price: {self.car.price:.2f} | Number of Repairs: {len(self.car.repairs)}""", str(self.car))


if __name__ == '__main__':
    main()
