import unittest
from unittest.mock import patch, MagicMock
from api.credential import get_credential_definition, create_credential_definition, issue_credential

class TestCredential(unittest.TestCase):

    @patch('api.credential.send_api_call')
    def test_get_credential_definition(self, mock_send_api_call):
        # Arrange
        mock_response = {"cred_def_id": "test_cred_def_id"}
        mock_send_api_call.return_value = mock_response

        # Act
        result = get_credential_definition("test_cred_def_id")

        # Assert
        self.assertEqual(result, mock_response)
        mock_send_api_call.assert_called_once()

    @patch('api.credential.send_api_call')
    def test_create_credential_definition(self, mock_send_api_call):
        # Arrange
        mock_response = {"cred_def_id": "new_cred_def_id"}
        mock_send_api_call.return_value = mock_response

        # Act
        result = create_credential_definition("schema_id", "tag", False)

        # Assert
        self.assertEqual(result, mock_response)
        mock_send_api_call.assert_called_once()

    @patch('api.credential.send_api_call')
    def test_issue_credential(self, mock_send_api_call):
        # Arrange
        mock_response = {"credential_id": "new_credential_id"}
        mock_send_api_call.return_value = mock_response
        credential_data = '{"connection_id": "conn_id", "credential_preview": {}}'

        # Act
        result = issue_credential(credential_data)

        # Assert
        self.assertEqual(result, mock_response)
        mock_send_api_call.assert_called_once()
