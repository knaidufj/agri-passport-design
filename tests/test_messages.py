import unittest
from unittest.mock import patch, MagicMock
from api.messages import send_message, query_messages

class TestMessages(unittest.TestCase):

    @patch('api.messages.send_api_call')
    def test_send_message(self, mock_send_api_call):
        # Arrange
        mock_response = {"message_id": "test_message_id"}
        mock_send_api_call.return_value = mock_response

        # Act
        result = send_message("conn_id", "Hello, World!")

        # Assert
        self.assertEqual(result, mock_response)
        mock_send_api_call.assert_called_once()

    @patch('api.messages.send_api_call')
    def test_query_messages(self, mock_send_api_call):
        # Arrange
        mock_response = {"messages": [{"id": "msg1"}, {"id": "msg2"}]}
        mock_send_api_call.return_value = mock_response

        # Act
        result = query_messages("conn_id", "sent")

        # Assert
        self.assertEqual(result, mock_response)
        mock_send_api_call.assert_called_once()
