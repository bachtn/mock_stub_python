from unittest.mock import patch

import numpy

from image_tools import convert_to_jpeg


@patch('cv2.imencode')
def test_convert_to_jpeg_calls_cv2_imencode_method_with_jpeg_extension(imencode_mock):
    fake_image = numpy.ones(shape=(1000, 2000, 3))

    convert_to_jpeg(fake_image)

    imencode_mock.assert_called_once_with('.jpeg', fake_image)
