import unittest
from unittest.mock import patch, MagicMock
from api.connections import create_invitation, query_active_connections

class TestConnections(unittest.TestCase):

    @patch('api.connections.send_api_call')
    @patch('api.connections.qrcode.QRCode')
    def test_create_invitation(self, mock_qrcode, mock_send_api_call):
        # Arrange
        mock_response = {"invitation_url": "http://test.url"}
        mock_send_api_call.return_value = mock_response
        mock_qr = MagicMock()
        mock_qrcode.return_value = mock_qr

        # Act
        result = create_invitation("test_alias")

        # Assert
        self.assertEqual(result, mock_response)
        mock_send_api_call.assert_called_once()
        mock_qr.make_image.assert_called_once()

    @patch('api.connections.send_api_call')
    def test_query_active_connections(self, mock_send_api_call):
        # Arrange
        mock_response = {"connections": [{"id": "conn1"}, {"id": "conn2"}]}
        mock_send_api_call.return_value = mock_response

        # Act
        result = query_active_connections()

        # Assert
        self.assertEqual(result, mock_response)
        mock_send_api_call.assert_called_once()
