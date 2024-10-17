from flask import Flask, request, jsonify, render_template
from config import AUTH_TOKEN, API_URL
from schema import create_schema, get_schema
from connections import create_invitation, query_active_connections
from credential import get_credential_definition, create_credential_definition, issue_credential, send_proposal
from messages import send_message, query_messages
from server import check_status
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-schema', methods=['GET', 'POST'])
def api_create_schema():
    if request.method == 'POST':
        data = request.form
        result = create_schema(
            data['schema_name'],
            data['schema_version'],
            data.getlist('attributes'),
            auth_token=AUTH_TOKEN,
            url=API_URL
        )
        return jsonify(result)
    return render_template('create_schema.html')

@app.route('/get-schema', methods=['GET'])
def api_get_schema():
    if request.method == 'GET':
        schema_id = request.args.get('schema_id')
        result = get_schema(schema_id, auth_token=AUTH_TOKEN, url=API_URL)
        return jsonify(result)
    return render_template('get_schema.html')

@app.route('/get-cred-def', methods=['GET'])
def api_get_cred_def():
    if request.method == 'GET':
        cred_def_id = request.args.get('credential_definition_id')
        result = get_credential_definition(cred_def_id, auth_token=AUTH_TOKEN, url=API_URL)
        return jsonify(result)
    return render_template('get_cred_def.html')

@app.route('/create-cred-def', methods=['GET', 'POST'])
def api_create_cred_def():
    if request.method == 'POST':
        data = request.form
        result = create_credential_definition(
            data['schema_id'],
            data['tag'],
            'support_revocation' in data,
            auth_token=AUTH_TOKEN,
            url=API_URL
        )
        return jsonify(result)
    return render_template('create_cred_def.html')

@app.route('/create-invitation', methods=['GET', 'POST'])
def api_create_invitation():
    if request.method == 'POST':
        data = request.form
        result = create_invitation(
            data['alias'],
            'auto_accept' in data,
            'public' in data,
            'multi_use' in data,
            auth_token=AUTH_TOKEN,
            url=API_URL
        )
        return jsonify(result)
    return render_template('create_invitation.html')

@app.route('/send-proposal', methods=['GET', 'POST'])
def api_send_proposal():
    if request.method == 'POST':
        data = request.form
        result = send_proposal(
            'auto_remove' in data,
            data['comment'],
            data['connection_id'],
            data['credential_preview'],
            data['filter'],
            data['replacement_id'],
            'trace' in data,
            data['verification_method'],
            auth_token=AUTH_TOKEN,
            url=API_URL
        )
        return jsonify(result)
    return render_template('send_proposal.html')

@app.route('/issue-credential', methods=['GET', 'POST'])
def api_issue_credential():
    if request.method == 'POST':
        data = request.form
        result = issue_credential(data['credential_data'], auth_token=AUTH_TOKEN, url=API_URL)
        return jsonify(result)
    return render_template('issue_credential.html')

@app.route('/query-connections', methods=['GET'])
def api_query_connections():
    result = query_active_connections(auth_token=AUTH_TOKEN, url=API_URL)
    return jsonify(result)

@app.route('/query-messages', methods=['GET'])
def api_query_messages():
    connection_id = request.args.get('connection_id')
    state = request.args.get('state', 'sent')
    result = query_messages(connection_id, state, auth_token=AUTH_TOKEN, url=API_URL)
    return jsonify(result)

@app.route('/send-message', methods=['GET', 'POST'])
def api_send_message():
    if request.method == 'POST':
        data = request.form
        result = send_message(
            data['connection_id'],
            data['content'],
            auth_token=AUTH_TOKEN,
            url=API_URL
        )
        return jsonify(result)
    return render_template('send_message.html')

@app.route('/check-status', methods=['GET'])
def api_check_status():
    result = check_status(auth_token=AUTH_TOKEN, url=API_URL)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
