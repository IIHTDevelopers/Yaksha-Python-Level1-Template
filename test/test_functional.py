import unittest
import numpy as np
import pandas as pd
import sys
import os
from test.TestUtils import TestUtils
from ecommerce import *
from StudentGrade import GradeManager
from pythonbasics import *

class TestShoppingCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_obj = TestUtils()
        cls.cart_items = [
            {"Item": "webcam", "Price": 800, "Quantity": 1},
            {"Item": "printer ink", "Price": 700, "Quantity": 2},
            {"Item": "Headphones", "Price": 300, "Quantity": 3},
            {"Item": "Keyboard", "Price": 500, "Quantity": 1},
            {"Item": "Mouse", "Price": 400, "Quantity": 1},
            {"Item": "Cleaning kit", "Price": 200, "Quantity": 1},
            {"Item": "USB Drive", "Price": 30, "Quantity": 2},
        ]

    def test_display_cart(self):
        """Test if the display_cart function correctly returns a DataFrame with expected columns."""
        try:
            df = display_cart(self.cart_items)
            expected_columns = ["Item", "Price", "Quantity", "Total Price"]
            self.assertTrue(all(col in df.columns for col in expected_columns))
            self.test_obj.yakshaAssert("test_display_cart", True, "functional")
            print("test_display_cart = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_display_cart", False, "exception")
            print("test_display_cart = Failed ")

    def test_price_analysis(self):
        """Test if the price analysis returns correct statistical values."""
        try:
            result = price_analysis(self.cart_items)
            self.assertEqual(result["min"], 30)
            self.assertEqual(result["max"], 800)
            self.assertAlmostEqual(result["mean"], 418.57, places=2)
            self.assertAlmostEqual(result["std"], 251.99, places=2)
            self.test_obj.yakshaAssert("test_price_analysis", True, "functional")
            print("test_price_analysis = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_price_analysis", False, "exception")
            print("test_price_analysis = Failed ")


class TestGradeManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_filename = "grades.txt"
        cls.manager = GradeManager(cls.test_filename)
        cls.test_obj = TestUtils()

    def setUp(self):
        """Setup before each test case"""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def tearDown(self):
        """Cleanup after each test case"""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_add_default_students(self):
        """Test if default student records are added correctly"""
        try:
            self.manager.add_default_students()
            with open(self.test_filename, "r") as file:
                lines = file.readlines()
            self.assertEqual(len(lines), 5)
            self.test_obj.yakshaAssert("test_add_default_students", True, "functional")
            print("test_add_default_students = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_add_default_students", False, "exception")
            print("test_add_default_students = Failed ")

    def test_view_grades(self):
        """Test if student grades are read correctly"""
        try:
            self.manager.add_default_students()
            grades = self.manager.view_grades()
            self.assertIsNotNone(grades)
            self.assertGreater(len(grades), 0)
            self.test_obj.yakshaAssert("test_view_grades", True, "functional")
            print("test_view_grades = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_view_grades", False, "exception")
            print("test_view_grades = Failed ")


class TestHospitalManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_obj = TestUtils()

    def test_display_hospital_info(self):
        """Test if hospital information is displayed correctly."""
        try:
            result = display_hospital_info()
            self.assertIsNotNone(result)
            self.assertIn(hospital_name, result)
            self.assertIn(str(total_doctors), result)
            self.test_obj.yakshaAssert("test_display_hospital_info", True, "functional")
            print("test_display_hospital_info = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_display_hospital_info", False, "exception")
            print("test_display_hospital_info = Failed ")

    def test_display_patients(self):
        """Test if patient records are displayed correctly."""
        try:
            result = display_patients()
            self.assertIsNotNone(result)
            for patient in patients:
                self.assertIn(patient, result)
            self.test_obj.yakshaAssert("test_display_patients", True, "functional")
            print("test_display_patients = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_display_patients", False, "exception")
            print("test_display_patients = Failed ")

    def test_check_emergency(self):
        """Test emergency patient detection."""
        try:
            result = check_emergency("Bob")
            self.assertTrue(result)  # Should return True for emergency patient
            result = check_emergency("Alice")
            self.assertFalse(result)  # Should return False for non-emergency patient
            self.test_obj.yakshaAssert("test_check_emergency", True, "functional")
            print("test_check_emergency = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("test_check_emergency", False, "exception")
            print("test_check_emergency = Failed ")



if __name__ == "__main__":
    unittest.main()
