"""
Unit tests for the HousingPriorityCalculator class.
"""

import unittest
from src.priority_calculator import HousingPriorityCalculator


class TestHousingPriorityCalculator(unittest.TestCase):
    """Unit tests for the HousingPriorityCalculator class."""

    def setUp(self) -> None:
        """Set up test fixtures before each test method."""
        self.priority_calculator = HousingPriorityCalculator()

    def test_points_for_class_year_freshman(self) -> None:
        """Test points_for_class_year for freshman (year 1)."""
        # Based on YOUR scoring system, what should freshman get?
        # If your system gives freshman 10 points, then:
        # expected_points = 10

        # WRITE YOUR TEST HERE FIRST, THEN IMPLEMENT THE METHOD
        result = self.priority_calculator.points_for_class_year(1)
        self.assertEqual(10, result)

    def test_points_for_class_year_sophomore(self) -> None:
        """Test points_for_class_year for sophomore (year 2)."""
        # Based on YOUR scoring system, what should sophomores get?
        # WRITE YOUR TEST HERE FIRST, THEN IMPLEMENT THE METHOD
        result = self.priority_calculator.points_for_class_year(2)
        self.assertEqual(20, result)
        

    def test_points_for_class_year_junior(self) -> None:
        """Test points_for_class_year for junior (year 3)."""
        # Based on YOUR scoring system, what should juniors get?
        # WRITE YOUR TEST HERE FIRST, THEN IMPLEMENT THE METHOD
        result = self.priority_calculator.points_for_class_year(3)
        self.assertEqual(30, result)

    def test_points_for_class_year_senior(self) -> None:
        """Test points_for_class_year for senior (year 4)."""
        # Based on YOUR scoring system, what should seniors get?
        # WRITE YOUR TEST HERE FIRST, THEN IMPLEMENT THE METHOD
        result = self.priority_calculator.points_for_class_year(4)
        self.assertEqual(40, result)

    def test_points_for_graduation_true(self) -> None:
        """Test points_for_graduation when graduating."""
        # How many points should graduating students get?
        result = self.priority_calculator.points_for_graduation(True)
        self.assertEqual(20, result)

    def test_points_for_graduation_false(self) -> None:
        """Test points_for_graduation when not graduating."""
        # How many points should non-graduating students get?
        result = self.priority_calculator.points_for_graduation(False)
        self.assertEqual(10, result)

    def test_points_for_credits_zero(self) -> None:
        """Test points_for_credits with 0 credits."""
        # What should 0 credits give?
        # result = self.priority_calculator.points_for_credits(0)
        # self.assertEqual(result, 0)
        result = self.priority_calculator.points_for_credits(0)
        self.assertEqual(0, result)

    def test_points_for_credits_low(self) -> None:
        """Test points_for_credits with low credit count (e.g., 7)."""
        result = self.priority_calculator.points_for_credits(7)
        self.assertEqual(7, result)

    def test_points_for_credits_medium(self) -> None:
        """Test points_for_credits with medium credit count (e.g., 15)."""
        # Test your scoring system with 15 credits
        result = self.priority_calculator.points_for_credits(15)
        self.assertEqual(15, result)

    def test_points_for_credits_high(self) -> None:
        """Test points_for_credits with high credit count (e.g., 30)."""
        # Test your scoring system with 30 credits
        result = self.priority_calculator.points_for_credits(30)
        self.assertEqual(30, result)

    def test_points_for_additional_questions_all_true(self) -> None:
        """Test points_for_additional_questions with all True responses."""
        # Based on YOUR additional questions and scoring:
        # If you ask 'old23' (2 pts) and 'honors' (3 pts):
        # responses = {'old23': True, 'honors': True}
        result = self.priority_calculator.points_for_additional_questions({'old23':True, 'honors': True})
        self.assertEqual(60, result)

    def test_points_for_additional_questions_all_false(self) -> None:
        """Test points_for_additional_questions with all False responses."""
        # Usually all False should give 0 points:
        # responses = {'old23': False, 'honors': False}
        result = self.priority_calculator.points_for_additional_questions({'old23':False, 'honors': False})
        self.assertEqual(20, result)

    def test_points_for_additional_questions_mixed(self) -> None:
        """Test points_for_additional_questions with mixed responses."""
        # Test partial points:
        # responses = {'old23': True, 'honors': False}
        result = self.priority_calculator.points_for_additional_questions({'old23':True, 'honors': False})
        self.assertEqual(40, result)

    def test_calculate_total_score_freshman_scenario(self) -> None:
        """Test calculate_total_score for a freshman scenario."""
        # Calculate expected total based on YOUR scoring system
        # Example scenario: year=1, is_graduating=False, credits=8,
        #  additional_responses={'old23': False, 'honors': True}
        # If your system: freshman=10pts, not_graduating=0pts, credits=8pts, honors_only=3pts
        # expected_total = 10 + 0 + 8 + 3 = 21
        
        year = self.priority_calculator.points_for_class_year(1)
        is_graduating = self.priority_calculator.points_for_graduation(False)
        credit = self.priority_calculator.points_for_credits(55)
        additional_responses = self.priority_calculator.points_for_additional_questions({'old23': False, 'honors': True})
        expected_total = year+is_graduating+credit+additional_responses
        self.assertEqual(expected_total, 115)


    def test_calculate_total_score_senior_graduating_scenario(self) -> None:
        """Test calculate_total_score for a graduating senior scenario."""
        # Calculate expected total for: year=4, is_graduating=True, credits=16,
        #  additional_responses={'old23': True, 'honors': True}
        # Work out the math based on YOUR scoring system first!
        year = self.priority_calculator.points_for_class_year(4)
        is_graduating = self.priority_calculator.points_for_graduation(True)
        credit = self.priority_calculator.points_for_credits(16)
        additional_responses = self.priority_calculator.points_for_additional_questions({'old23': True, 'honors': True})
        expected_total = year+is_graduating+credit+additional_responses
        self.assertEqual(expected_total, 106)

    def test_calculate_total_score_senior_non_graduating_scenario(self) -> None:
        """Test calculate_total_score for a non-graduating senior scenario."""
        # Calculate expected total for: year=4, is_graduating=False, credits=20,
        #  additional_responses={'old23': False, 'honors': False}
        # Work out the math based on YOUR scoring system first!
        year = self.priority_calculator.points_for_class_year(4)
        is_graduating = self.priority_calculator.points_for_graduation(False)
        credit = self.priority_calculator.points_for_credits(15)
        additional_responses = self.priority_calculator.points_for_additional_questions({'old23': False, 'honors': False})
        expected_total = year+is_graduating+credit+additional_responses
        self.assertEqual(expected_total, 75)

    def test_calculate_total_score_edge_cases(self) -> None:
        """Test calculate_total_score with edge cases."""
        # Test edge cases as needed based on your priority scoring system.

        # Note: you don't need to test for negative credits or invalid years,
        # since your question asker should be disallowing negative inputs anyway.


        pass
