from unittest.mock import patch

from src.stub_mock import filter_my_data, display, MyClass

"""
Mock
"""


# Mock a function
def test_display_calls_print_message():
    # Given
    x = 'yolo'

    # When
    with patch('test_mocks_stubs_examples.print_message') as print_message_mock:
        display(x)
        # Then
        assert print_message_mock.called


# Mock an object function
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
# FIXME : if not working remove it
def test_display_calls_print_message_when_condition_is_true():
    # Given
    myObj = MyClass()
    condition = True

    # When
    with patch.object(myObj, 'print_message') as myObj_print_message_mock:
        # Then
        myObj.display(condition)
        myObj_print_message_mock.assert_called()


def test_my_static_method_does_not_call_print_message_when_condition_is_false():
    # When
    with patch.object(MyClass, 'print_message') as myObj_print_message_mock:
        # Then
        MyClass.my_static_method(condition=False)
        assert not myObj_print_message_mock.called


"""
Stub
"""


def test_filter_should_call_get_data():
    # When
    with patch('stub_example.get_data') as get_data_mock:
        filter_my_data("in stock")
        # Then
        get_data_mock.assert_called()


def test_filter_should_filter_data_properly():
    # Given
    expected_filtered_data = [("in stock", "Iphone 8", 30), ("in stock", "Samsung 8", 5)]

    # When
    with patch('stub_example.get_data') as get_data_stub:
        get_data_stub.return_value = [("in stock", "Iphone 8", 30), ("in stock", "Samsung 8", 5),
                                      ("not in stock", "Iphone X", 0), ("not in stock", "Samsung 6", 0)]
        filtered_data_result = filter_my_data("in stock")

    # Then
    assert filtered_data_result == expected_filtered_data


def test_filter_should_return_empty_list_when_get_data_raises_exception():
    # Given
    expected_filtered_data = []

    # When
    with patch('stub_example.get_data') as get_data_stub:
        get_data_stub.side_effect = Exception('Could not connect to the CRM')
        filtered_data_result = filter_my_data("in stock")

    # Then
    assert filtered_data_result == expected_filtered_data
