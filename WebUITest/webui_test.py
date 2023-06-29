import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import itertools

class SpiralMatrixSolverTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000")

    def tearDown(self):
        self.driver.quit()

    def test_solve_spiral_matrix(self):
        # EP test cases
        ep_test_cases = [
            {
                "input": "1,2,3\n4,5,6\n7,8,9",
                "expected_output": ["1", "2", "3", "6", "9", "8", "7", "4", "5"]
            },
            {
                "input": "1,2\n3,4",
                "expected_output": ["1", "2", "4", "3"]
            },
            {
                "input": "1",
                "expected_output": ["1"]
            },
        ]

        # BVA test cases
        bva_test_cases = [
            {
                "input": "",
                "expected_output": []
            },
            {
                "input": "1,2,3\n4,5\n6,7,8,9",
                "expected_output": ["1", "2", "3", "5", "9", "8", "7", "6", "4"]
            },
        ]

        # EP test cases
        for test_case in ep_test_cases:
            with self.subTest(test_case=test_case):
                matrix_input = self.driver.find_element(By.ID, "matrix")
                matrix_input.clear()
                matrix_input.send_keys(test_case["input"])

                submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
                submit_button.click()

                result_list = self.driver.find_element(By.ID, "result")
                result_items = result_list.find_elements(By.TAG_NAME, "li")

                self.assertEqual(len(result_items), len(test_case["expected_output"]))

                for expected, actual in zip(test_case["expected_output"], result_items):
                    self.assertEqual(expected, actual.text)
                print("Passed EP for UI test case")

        # BVA test cases
        for test_case in bva_test_cases:
            with self.subTest(test_case=test_case):
                matrix_input = self.driver.find_element(By.ID, "matrix")
                matrix_input.clear()
                matrix_input.send_keys(test_case["input"])

                submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
                submit_button.click()

                result_list = self.driver.find_element(By.ID, "result")
                result_items = result_list.find_elements(By.TAG_NAME, "li")

                self.assertEqual(len(result_items), len(test_case["expected_output"]))

                for expected, actual in zip(test_case["expected_output"], result_items):
                    self.assertEqual(expected, actual.text)

                print("Passed BVA for UI test case")

if __name__ == '__main__':
    unittest.main()
