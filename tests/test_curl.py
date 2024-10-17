import unittest
from unittest.mock import patch, MagicMock
from api.curl import send_api_call
import requests

class TestCurl(unittest.TestCase):

    @patch('api.curl.requests.request')
    def test_send_api_call_get(self, mock_request):
        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = {'key': 'value'}
        mock_request.return_value = mock_response

        # Act
        result = send_api_call('http://test.url', method='GET')

        # Assert
        self.assertEqual(result, {'key': 'value'})
        mock_request.assert_called_once_with('GET', 'http://test.url', headers=None, json=None)

    @patch('api.curl.requests.request')
    def test_send_api_call_post(self, mock_request):
        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = {'id': 'new_id'}
        mock_request.return_value = mock_response
        headers = {'Content-Type': 'application/json'}
        data = {'name': 'test'}

        # Act
        result = send_api_call('http://test.url', method='POST', headers=headers, data=data)

        # Assert
        self.assertEqual(result, {'id': 'new_id'})
        mock_request.assert_called_once_with('POST', 'http://test.url', headers=headers, json=data)

    @patch('api.curl.requests.request')
    def test_send_api_call_error(self, mock_request):
        # Arrange
        mock_request.side_effect = requests.exceptions.HTTPError('404 Client Error')

        # Act & Assert
        with self.assertRaises(requests.exceptions.HTTPError):
            send_api_call('http://test.url')
