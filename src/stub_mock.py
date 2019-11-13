
from unittest.mock import patch


"""
* When I mock or stub something (function, object, class, etc), unittest with just create a wrapper around it
by creating a MagicMock object.
* This object have my attribute that help us when testing.
For example, it has a 'called' attribute that will be true if the function is called & false otherwise.
* When we are mocking / stubing a function, we should give the full path to the function.
For example if the function is located in 'my_module1.my_module2', when mocking the function we should specify the full
path
with patch(''my_module1.my_module2.my_function') as mock:
    # do something
    pass
"""

#################################################
#                       MOCK
#################################################
"""
* Mock is just testing behaviour, making sure certain methods are called.
* For example, I want to test that my function :
- was called
- was not called
- was called once (or multiple times)
- was called with certain arguments
- ...
"""


############# Mock a function
def print_message(message):
    print(message)


def display(x):
    print_message('yolo')
    print("hello")

# Mock an object function
class MyClass:
    def display(self, condition):
        if condition:
            self.print_message()

    def print_message(self):
        print("You called me")

    @staticmethod
    def my_static_method(self, condition):
        self.print_message()


def test_display_calls_print_message_when_condition_is_true():
    # Given
    myObj = MyClass()

    # When
    with patch.object(myObj, 'print_message') as myObj_print_message_mock:
        # Then
        myObj.display(condition=False)
        myObj_print_message_mock.assert_called()


def test_display_does_not_call_print_message_when_condition_is_false():
    # Given
    myObj = MyClass()

    # When
    with patch.object(myObj, 'print_message') as myObj_print_message_mock:
        # Then
        myObj.display(condition=False)
        assert not myObj_print_message_mock.called

# Mock a class function
### Class with static methods


#################################################
#                       Stub
#################################################
def get_data():
    """
    Gets the information from CRM
    1 - Should connect to the database
    2 - Should execute a query with the correct parameters
    3 - Should return the result of the query
    :return List[("Status", "Phone model", "number of products")]
    ("In stock", "Iphone 8", 30), ("Out of stock", "Samsung 10", 0)
    """
    pass


def filter_my_data(stock_status):
    """
    - Get data
    - Filter data
    """
    try:
        data = get_data()
        filtered_data = [item for item in data if item[0] == stock_status]
        return filtered_data
    except Exception:
        return []