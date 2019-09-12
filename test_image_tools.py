from unittest.mock import patch

import pytest

from image_tools import load_images, save_images, convert_to_jpeg, save_binary_file


@pytest.fixture()
def image_list_and_names():
    image_list, image_name_list = load_images('images')
    return image_list, image_name_list


@patch('image_tools.save_binary_file')
@patch('image_tools.cv2.imwrite')
def test_save_images_should_not_call_cv2_imwrite_function(imwrite_mock, save_binary_file_mock,
                                                          image_list_and_names):
    # Given
    image_list, image_name_list = image_list_and_names

    # When
    save_images(image_list, image_name_list, 'images')

    # Then
    assert not imwrite_mock.called


@patch('image_tools.cv2.imencode')
def test_convert_to_jpeg_calls_cv2_imencode_method(imencode_mock, image_list_and_names):
    # Given
    image_list, image_name_list = image_list_and_names
    target_image = image_list[0]
    imencode_mock.return_value = (True, target_image)

    # When
    convert_to_jpeg(target_image)

    # Then
    imencode_mock.assert_called_once_with('.jpeg', target_image)


@patch('image_tools.cv2.imencode')
def test_convert_to_jpeg_raises_an_exception_if_the_conversion_fails(imencode_mock, image_list_and_names):
    # Given
    image_list, image_name_list = image_list_and_names
    target_image = image_list[0]
    imencode_mock.return_value = (False, target_image)

    # Then
    with pytest.raises(Exception, match='Error encountered while converting image to JPG'):
        # When
        convert_to_jpeg(target_image)


@patch('image_tools.save_binary_file')
@patch('image_tools.convert_to_jpeg')
def test_save_images_should_call_convert_to_jpeg_function(convert_to_jpeg_mock, save_binary_file_mock,
                                                          image_list_and_names):
    # Given
    image_list, image_name_list = image_list_and_names

    # When
    save_images(image_list, image_name_list, 'images')

    # Then
    convert_to_jpeg_mock.assert_called()


@patch('builtins.open')
def test_save_binary_path_uses_open_builtin_to_save_images(open_builtin_mock, image_list_and_names):
    # Given
    image_list, image_name_list = image_list_and_names

    # When
    save_binary_file('fake_path', image_list[0])

    # Then
    open_builtin_mock.assert_called()


@patch('image_tools.convert_to_jpeg')
@patch('image_tools.save_binary_file')
def test_save_images_calls_save_binary_file_function(save_binary_file_mock, convert_to_jpeg_mock, image_list_and_names):
    # Given
    image_list, image_name_list = image_list_and_names

    # When
    save_images(image_list, image_name_list, 'images')

    # Then
    save_binary_file_mock.assert_called()
