import unittest
from unittest.mock import patch, MagicMock
from api.server import check_status

class TestServer(unittest.TestCase):

    @patch('api.server.send_api_call')
    def test_check_status(self, mock_send_api_call):
        # Arrange
        mock_response = {"status": "ready"}
        mock_send_api_call.return_value = mock_response

        # Act
        result = check_status()

        # Assert
        self.assertEqual(result, mock_response)
        mock_send_api_call.assert_called_once()
