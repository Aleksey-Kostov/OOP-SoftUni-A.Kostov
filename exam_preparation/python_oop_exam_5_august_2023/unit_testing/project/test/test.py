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

    def test_getter_price_more_less_than_one(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0
        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_getter_price_equal_to_one(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1
        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_getter_happy_price(self):
        self.assertEqual(20000, self.car.price)

    def test_getter_mileage_more_less_than_100(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 99
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    def test_getter_mileage_equal_to_100(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    def test_getter_happy_mileage(self):
        self.assertEqual(100000, self.car.mileage)

    def test_set_promotional_price_with_exception_more_less_than_price(self):
        with self.assertRaises(ValueError) as ve1:
            self.car.set_promotional_price(21000)
        self.assertEqual("You are supposed to decrease the price!", str(ve1.exception))
        self.assertEqual(20000, self.car.price)

    def test_set_promotional_price_with_exception_equal_to_price(self):
        with self.assertRaises(ValueError) as ve1:
            self.car.set_promotional_price(20000)
        self.assertEqual("You are supposed to decrease the price!", str(ve1.exception))
        self.assertEqual(20000, self.car.price)

    def test_set_promotional_price_with_not_exception(self):
        new_price = self.car.set_promotional_price(10000)
        self.assertEqual(10000, self.car.price)
        self.assertEqual("The promotional price has been successfully set.", new_price)

    def test_need_repair_with_repair_impossible(self):
        self.car.repair_price = 15000
        self.assertEqual('Repair is impossible!', self.car.need_repair(self.car.repair_price, "test"))
        self.assertEqual([], self.car.repairs)
        self.assertEqual(20000, self.car.price)

    def test_need_repair_with_repair(self):
        self.car.repair_price = 5000
        self.car.need_repair(self.car.repair_price, "test")
        self.assertEqual(25000, self.car.price)
        self.assertEqual(['test'], self.car.repairs)
        self.assertEqual("Price has been increased due to repair charges.",
                         self.car.need_repair(self.car.repair_price, "test"))

        self.car.need_repair(self.car.repair_price, "test")
        self.assertEqual(35000, self.car.price)
        self.assertEqual(['test', 'test', 'test'], self.car.repairs)
        self.assertEqual("Price has been increased due to repair charges.",
                         self.car.need_repair(self.car.repair_price, "test"))

    def test_need_repair_with_repair_equal(self):
        self.car.repair_price = 10000
        self.car.need_repair(self.car.repair_price, "test")
        self.assertEqual(30000, self.car.price)
        self.assertEqual(['test'], self.car.repairs)
        self.assertEqual("Price has been increased due to repair charges.",
                         self.car.need_repair(self.car.repair_price, "test"))

    def test_diff_car_type(self):
        self.car2 = SecondHandCar("BMW", "Test", 100000, 20000.00)
        self.assertEqual('Cars cannot be compared. Type mismatch!', self.car > self.car2)

    def test_same_car_type(self):
        self.car2 = SecondHandCar("BMW", "Sedan", 100000, 10000.00)
        self.assertTrue(self.car.price > self.car2.price)
        self.assertFalse(self.car.price < self.car2.price)

    def test_string_no_repairs(self):
        self.assertEqual(f"""Model Seat | Type Sedan | Milage 100000km
Current price: 20000.00 | Number of Repairs: 0""", str(self.car))

    def test_string_1_repairs(self):
        self.car.need_repair(8000, "test")
        self.assertEqual(f"""Model Seat | Type Sedan | Milage 100000km
Current price: 28000.00 | Number of Repairs: 1""", str(self.car))

    def test_string_2_repairs(self):
        self.car.need_repair(5000, "test")
        self.car.need_repair(5000, "test")
        self.assertEqual(f"""Model Seat | Type Sedan | Milage 100000km
Current price: 30000.00 | Number of Repairs: 2""", str(self.car))


if __name__ == '__main__':
    main()
