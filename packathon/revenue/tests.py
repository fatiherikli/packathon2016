from django.test import TestCase

class QuestionViewTests(TestCase):
    def test_revenue(self):
        try:
            from revenue.models import Revenue
        except ImportError:
            self.fail('No such revenue model')
