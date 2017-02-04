from django.test import TestCase

# This test case is just to test the fact that tests are running
# and asserting correctly both in development environment and travis-ci
class TestCaseInception(TestCase):
    
    def test_test_case_inception(self):
        testVariable = 10
        self.assertEqual(testVariable, 10, "How the fuck did this fail?")