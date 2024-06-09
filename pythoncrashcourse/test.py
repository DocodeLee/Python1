def format_name(first, last, middle = ''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name =f"{first} {last}"
    return full_name.title()

def city_info(name, country, population = ''):
    if population:
        info = f"{name}, {country} - population : {population}"
    else:
        info = f"{name}, {country}"
    return info.title()

class AnonymousSurvey:
    """Collect anonymous answers to a survey question"""
    def __init__(self,question):
        """store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
    def show_question(self):
        """Show the survey question"""
        print(self.question)
    def store_response(self,new_response):
        """store a single response to the survey"""
        self.responses.append(new_response)
    def show_results(self):
        """Show all the response that have been given"""
        print("Survey Results: ")
        for response in self.responses:
            print(f"- {response}")
            
class Employee:
    """Collect information of employee firstname lastname annual salary"""
    def __init__(self, first, last, salary):
        """store name and salary"""
        self.first = first
        self.last = last
        self.salary = salary
    def give_raise(self, raise_amount = 50000):
        self.salary += raise_amount
        