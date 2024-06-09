import unittest
from test import format_name, city_info, AnonymousSurvey, Employee

# class NameTest(unittest.TestCase):
#     """Do names like 'Sooyong park' work?"""
#     def test_first_last_name(self):
#         formatted = format_name("hyunil","lee")
#         self.assertEqual(formatted,"Hyunil Lee")
#     ## under here is for first middle last name
#     def test_first_last_middle(self):
#         """ Do name like benzamin frankling gorden work?"""
#         formatted = format_name("wolfgang","mozart","amadeus")
#         self.assertEqual(formatted,"Wolfgang Amadeus Mozart")
# if __name__ == '__main__':
#     unittest.main()


## Practice

# class CityTest(unittest.TestCase):
#     """Check Santiago Chile work?"""
#     def test_city_country_population(self):
#         information = city_info("santiago", "chile", "500000")
#         self.assertEqual(information,"Santiago, Chile - Population : 500000")
#     def test_city_country(self):
#         information = city_info("santiago","chile")
#         self.assertEqual(information,"Santiago, Chile")
# if __name__ == '__main__':
#     unittest.main()


##Testing the clas

##Define the question first
# question = "What language did you learn first"
# my_survey = AnonymousSurvey(question)

##show the question and save the response
# my_survey.show_question()
# print("Enter q anytimg to quit \n")
# while True:
#     response = input("Language : ")
#     if response == "q":
#         break
#     my_survey.store_response(response)
## TO show the result
# print("\n Thank you to everyone who participated")
# my_survey.show_results()

## Test the class

# class TestAnonymousSurvey(unittest.TestCase):
#     """Test for the class AnonymousSurvey"""
#     def test_store_single_response(self):
#         """Test the single response"""
#         question = "what language did you learn"
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_response('English')
#         self.assertIn("English",my_survey.responses)
#     def test_store_several_response(self):
#         """Test the several responses"""
#         question = "What langauge did you learn"
#         my_survey = AnonymousSurvey(question)
#         responses = ["English","Japanese","Korean"]
#         for response in responses:
#             my_survey.store_response(response)
#         for response in responses:
#             self.assertIn(response,my_survey.responses)
# if __name__ =='__main__':
#     unittest.main()


## Simplified with setUp()

# class TestAnonymousSurvey(unittest.TestCase):
#     """Test for the class AnonymousSurvey"""
#     def setUp(self):
#         """Create a survey and a set of response"""
#         question = "what language did you first learn"
#         self.my_survey = AnonymousSurvey(question)
#         self.responses = ["English","Japanese","Korean"]
#     def test_store_single_response(self):
#         # """Test the single response"""
#         # question = "what language did you learn"
#         # my_survey = AnonymousSurvey(question)
#         # my_survey.store_response('English')
#         # self.assertIn("English",my_survey.responses)
#         self.my_survey.store_response(self.responses[0])
#         self.assertIn(self.responses[0],self.my_survey.responses)
#     def test_store_several_response(self):
#         """Test the several responses"""
#         # question = "What langauge did you learn"
#         # my_survey = AnonymousSurvey(question)
#         # responses = ["English","Japanese","Korean"]
#         # for response in responses:
#         #     my_survey.store_response(response)
#         # for response in responses:
#         #     self.assertIn(response,my_survey.responses)
#         for response in self.responses:
#             self.my_survey.store_response(response)
#         for response in self.responses:
#             self.assertIn(response,self.my_survey.responses)
# if __name__ =='__main__':
#     unittest.main()


# ## Practice
# justin = Employee("matin","justin", 40_000)
# print(f"{justin.first}, {justin.last}, {justin.salary}")
# justin.give_raise(2000)
# print(f"{justin.salary}")

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.justin = Employee("justin","max", 50000)
    
    def test_give_default_raise(self):
        self.justin.give_raise()
        self.assertEqual(self.justin.salary, 50000 + 50000)
    
    def test_give_custom_raise(self):
        self.justin.give_raise(3000)
        self.assertEqual(self.justin.salary, 50000 + 3000)

if __name__ == "__main__":
    unittest.main()