from flask import Flask, request, jsonify, render_template
from config import AUTH_TOKEN, API_URL
from schema import create_schema, get_schema
from connections import create_invitation, query_active_connections
from credential import (
    get_credential_definition,
    create_credential_definition,
    issue_credential,
    send_proposal,
    fetch_credential_records,
)
from messages import send_message, query_messages
from server import check_status
import json
import random
import hashlib

app = Flask(__name__)


@app.route("/")
def index():
    """Render the index page."""
    return render_template("index.html")


@app.route("/create-schema", methods=["GET", "POST"])
def api_create_schema():
    """
    Create a new schema.

    If the request method is POST, it processes the form data to create a schema
    and returns the result as JSON. If the request method is GET, it renders
    the create schema page.

    Returns:
        JSON response with the result of schema creation or renders the create schema page.
    """
    if request.method == "POST":
        data = request.form
        result = create_schema(
            data["schema_name"],
            data["schema_version"],
            data.getlist("attributes"),
            auth_token=AUTH_TOKEN,
            url=API_URL,
        )
        return jsonify(result)
    return render_template("create_schema.html")


@app.route("/get-schema", methods=["GET", "POST"])
def api_get_schema():
    """
    Retrieve a schema by its ID.

    If the request method is GET, it fetches the schema using the provided schema ID
    and returns the result as JSON. If the request method is POST, it renders the
    get schema page.

    Returns:
        JSON response with the schema details or renders the get schema page.
    """
    if request.method == "GET" and request.args.get("schema_id"):
        schema_id = request.args.get("schema_id")
        result = get_schema(schema_id, auth_token=AUTH_TOKEN, url=API_URL)
        return jsonify(result)
    return render_template("get_schema.html")


@app.route("/get-cred-def", methods=["GET", "POST"])
def api_get_cred_def():
    """
    Retrieve a credential definition by its ID.

    If the request method is GET, it fetches the credential definition using the provided
    credential definition ID and returns the result as JSON. If the request method is POST,
    it renders the get credential definition page.

    Returns:
        JSON response with the credential definition details or renders the get credential definition page.
    """
    cred_def_id = request.args.get("credential_definition_id")
    if cred_def_id:
        try:
            result = get_credential_definition(cred_def_id, auth_token=AUTH_TOKEN, url=API_URL)
            return jsonify(result)
        except Exception as e:
            return f"Error retrieving credential definition: {e}", 400
    return render_template("get_cred_def.html")


@app.route("/create-cred-def", methods=["GET", "POST"])
def api_create_cred_def():
    """
    Create a new credential definition.

    If the request method is POST, it processes the form data to create a credential
    definition and returns the result as JSON. If the request method is GET, it renders
    the create credential definition page.

    Returns:
        JSON response with the result of credential definition creation or renders the create credential definition page.
    """
    if request.method == "POST":
        data = request.form
        result = create_credential_definition(
            data["schema_id"],
            data["tag"],
            "support_revocation" in data,
            auth_token=AUTH_TOKEN,
            url=API_URL,
        )
        return jsonify(result)
    return render_template("create_cred_def.html")


@app.route("/create-invitation", methods=["GET", "POST"])
def api_create_invitation():
    """
    Create a new invitation.

    If the request method is POST, it processes the form data to create an invitation
    and returns the result as JSON. If the request method is GET, it renders the create
    invitation page.

    Returns:
        JSON response with the result of invitation creation or renders the create invitation page.
    """
    if request.method == "POST":
        data = request.form
        result = create_invitation(
            data["alias"],
            "auto_accept" in data,
            "public" in data,
            "multi_use" in data,
            auth_token=AUTH_TOKEN,
            url=API_URL,
        )
        return jsonify(result)
    return render_template("create_invitation.html")


@app.route("/send-proposal", methods=["GET", "POST"])
def api_send_proposal():
    """
    Send a proposal.

    If the request method is POST, it processes the form data to send a proposal
    and returns the result as JSON. If the request method is GET, it renders the
    send proposal page.

    Returns:
        JSON response with the result of the proposal sending or renders the send proposal page.
    """
    if request.method == "POST":
        data = request.form
        result = send_proposal(
            "auto_remove" in data,
            data["comment"],
            data["connection_id"],
            data["credential_preview"],
            data["filter"],
            data["replacement_id"],
            "trace" in data,
            data["verification_method"],
            auth_token=AUTH_TOKEN,
            url=API_URL,
        )
        return jsonify(result)
    return render_template("send_proposal.html")


@app.route("/issue-credential", methods=["GET", "POST"])
def api_issue_credential():
    """
    Issue a new credential.

    If the request method is POST, it processes the form data to issue a credential
    and returns the result as JSON. If the request method is GET, it renders the
    issue credential page.

    Returns:
        JSON response with the result of credential issuance or renders the issue credential page.
    """
    if request.method == "POST":
        data = request.form
        result = issue_credential(
            data["credential_data"], auth_token=AUTH_TOKEN, url=API_URL
        )
        return jsonify(result)
    return render_template("issue_credential.html")


@app.route("/new-user", methods=["GET", "POST"])
def api_new_user():
    """
    Create a new user credential.

    If the request method is POST, it processes the form data to create a new user
    credential and returns the result as JSON. If the request method is GET, it renders
    the new user page.

    Returns:
        JSON response with the result of user credential creation or renders the new user page.
    """
    if request.method == "POST":
        data = request.form
        credential_data = {
            "connection_id": data["connection_id"],
            "credential_preview": {
                "@type": "issue-credential/2.0/credential-preview",
                "attributes": [
                    {
                        "name": "user_id",
                        "value": str(
                            hashlib.sha256(data["email"].encode()).hexdigest()
                        )[:6],
                    },
                    {"name": "name", "value": data["name"]},
                    {"name": "email", "value": data["email"]},
                ],
            },
            "filter": {
                "indy": {
                    "cred_def_id": "13ZM7KEfAzLC12q1R1SiTS:3:CL:2308153:User",
                    "issuer_did": "13ZM7KEfAzLC12q1R1SiTS",
                    "schema_id": "13ZM7KEfAzLC12q1R1SiTS:2:AATP_UserSchema:1.0",
                    "schema_name": "AATP_UserSchema",
                    "schema_version": "1.0",
                }
            },
            "trace": True,
        }
        # Convert credential_data to JSON string
        credential_data_json = json.dumps(credential_data)
        result = issue_credential(
            credential_data_json, auth_token=AUTH_TOKEN, url=API_URL
        )
        return jsonify(result)
    return render_template("new_user.html")


@app.route("/new-producer", methods=["GET", "POST"])
def api_new_producer():
    """
    Create a new producer credential.

    If the request method is POST, it processes the form data to create a new producer
    credential and returns the result as JSON. If the request method is GET, it renders
    the new producer page.

    Returns:
        JSON response with the result of producer credential creation or renders the new producer page.
    """
    if request.method == "POST":
        data = request.form
        credential_data = {
            "connection_id": data["connection_id"],
            "credential_preview": {
                "@type": "issue-credential/2.0/credential-preview",
                "attributes": [
                    {
                        "name": "producer_id",
                        "value": str(
                            hashlib.sha256(data["user_id"].encode()).hexdigest()
                        )[:6],
                    },
                    {"name": "user_id", "value": data["user_id"]},
                    {"name": "organization_type", "value": data["organization_type"]},
                ],
            },
            "filter": {
                "indy": {
                    "cred_def_id": "13ZM7KEfAzLC12q1R1SiTS:3:CL:2308155:Producer",
                    "issuer_did": "13ZM7KEfAzLC12q1R1SiTS",
                    "schema_id": "13ZM7KEfAzLC12q1R1SiTS:2:AATP_ProducerSchema:1.1",
                    "schema_name": "AATP_ProducerSchema",
                    "schema_version": "1.1",
                }
            },
            "trace": True,
        }
        # Convert credential_data to JSON string
        credential_data_json = json.dumps(credential_data)
        result = issue_credential(
            credential_data_json, auth_token=AUTH_TOKEN, url=API_URL
        )
        return jsonify(result)
    return render_template("new_producer.html")


@app.route("/new-certification", methods=["GET", "POST"])
def api_new_certification():
    """
    Create a new certification credential.

    If the request method is POST, it processes the form data to create a new certification
    credential and returns the result as JSON. If the request method is GET, it renders
    the new certification page.

    Returns:
        JSON response with the result of certification credential creation or renders the new certification page.
    """
    if request.method == "POST":
        data = request.form
        credential_data = {
            "connection_id": data["connection_id"],
            "credential_preview": {
                "@type": "issue-credential/2.0/credential-preview",
                "attributes": [
                    {
                        "name": "certification_id",
                        "value": str(
                            hashlib.sha256(
                                (
                                    data["producer_id"]
                                    + data["certification_date"]
                                    + data["certification_authority_id"]
                                    + str(random.randint(0, 1000000))
                                ).encode()
                            ).hexdigest()
                        )[:6],
                    },
                    {"name": "producer_id", "value": data["producer_id"]},
                    {"name": "certification_date", "value": data["certification_date"]},
                    {
                        "name": "certification_authority_id",
                        "value": data["certification_authority_id"],
                    },
                    {"name": "certification_status", "value": "Active"},
                ],
            },
            "filter": {
                "indy": {
                    "cred_def_id": "13ZM7KEfAzLC12q1R1SiTS:3:CL:2308259:Certification",
                    "issuer_did": "13ZM7KEfAzLC12q1R1SiTS",
                    "schema_id": "13ZM7KEfAzLC12q1R1SiTS:2:AATP_CertificationSchema:1.0",
                    "schema_name": "AATP_CertificationSchema",
                    "schema_version": "1.0",
                }
            },
            "trace": True,
        }
        # Convert credential_data to JSON string
        credential_data_json = json.dumps(credential_data)
        result = issue_credential(
            credential_data_json, auth_token=AUTH_TOKEN, url=API_URL
        )
        return jsonify(result)
    return render_template("new_certification.html")


@app.route("/new-product", methods=["GET", "POST"])
def api_new_product():
    """
    Create a new product credential.

    If the request method is POST, it processes the form data to create a new product
    credential and returns the result as JSON. If the request method is GET, it renders
    the new product page.

    Returns:
        JSON response with the result of product credential creation or renders the new product page.
    """
    if request.method == "POST":
        data = request.form
        credential_data = {
            "connection_id": data["connection_id"],
            "credential_preview": {
                "@type": "issue-credential/2.0/credential-preview",
                "attributes": [
                    {
                        "name": "product_id",
                        "value": str(
                            hashlib.sha256(
                                (
                                    data["producer_id"]
                                    + str(random.randint(0, 1000000))
                                ).encode()
                            ).hexdigest()
                        )[:6],
                    },
                    {"name": "product_name", "value": data["product_name"]},
                    {"name": "producer_id", "value": data["producer_id"]},
                    {"name": "production_date", "value": data["production_date"]},
                    {"name": "expiration_date", "value": data["expiration_date"]},
                ],
            },
            "filter": {
                "indy": {
                    "cred_def_id": "13ZM7KEfAzLC12q1R1SiTS:3:CL:2308157:Product",
                    "issuer_did": "13ZM7KEfAzLC12q1R1SiTS",
                    "schema_id": "13ZM7KEfAzLC12q1R1SiTS:2:AATP_ProductSchema:1.0",
                    "schema_name": "AATP_ProductSchema",
                    "schema_version": "1.0",
                }
            },
            "trace": True,
        }
        # Convert credential_data to JSON string
        credential_data_json = json.dumps(credential_data)
        result = issue_credential(
            credential_data_json, auth_token=AUTH_TOKEN, url=API_URL
        )
        return jsonify(result)
    return render_template("new_product.html")


@app.route("/new-packaging", methods=["GET", "POST"])
def api_new_packaging():
    """
    Create a new packaging credential.

    If the request method is POST, it processes the form data to create a new packaging
    credential and returns the result as JSON. If the request method is GET, it renders
    the new packaging page.

    Returns:
        JSON response with the result of packaging credential creation or renders the new packaging page.
    """
    if request.method == "POST":
        data = request.form
        credential_data = {
            "connection_id": data["connection_id"],
            "credential_preview": {
                "@type": "issue-credential/2.0/credential-preview",
                "attributes": [
                    {
                        "name": "packaging_id",
                        "value": str(
                            hashlib.sha256(
                                (
                                    data["producer_id"]
                                    + str(random.randint(0, 1000000))
                                ).encode()
                            ).hexdigest()
                        )[:6],
                    },
                    {"name": "product_id", "value": data["product_id"]},
                    {"name": "packaging_date", "value": data["packaging_date"]},
                    {
                        "name": "packaging_facility_id",
                        "value": data["packaging_facility_id"],
                    },
                    {
                        "name": "packaging_conditions",
                        "value": data["packaging_conditions"],
                    },
                    {"name": "batch_number", "value": data["batch_number"]},
                ],
            },
            "filter": {
                "indy": {
                    "cred_def_id": "13ZM7KEfAzLC12q1R1SiTS:3:CL:2308160:Packaging",
                    "issuer_did": "13ZM7KEfAzLC12q1R1SiTS",
                    "schema_id": "13ZM7KEfAzLC12q1R1SiTS:2:AATP_PackagingSchema:1.0",
                    "schema_name": "AATP_PackagingSchema",
                    "schema_version": "1.0",
                }
            },
            "trace": True,
        }
        # Convert credential_data to JSON string
        credential_data_json = json.dumps(credential_data)
        result = issue_credential(
            credential_data_json, auth_token=AUTH_TOKEN, url=API_URL
        )
        return jsonify(result)
    return render_template("new_packaging.html")


@app.route("/new-transportation", methods=["GET", "POST"])
def api_new_transportation():
    """
    Create a new transportation credential.

    If the request method is POST, it processes the form data to create a new transportation
    credential and returns the result as JSON. If the request method is GET, it renders
    the new transportation page.

    Returns:
        JSON response with the result of transportation credential creation or renders the new transportation page.
    """
    if request.method == "POST":
        data = request.form
        credential_data = {
            "connection_id": data["connection_id"],
            "credential_preview": {
                "@type": "issue-credential/2.0/credential-preview",
                "attributes": [
                    {"name": "product_id", "value": data["product_id"]},
                    {"name": "origin_location", "value": data["origin_location"]},
                    {
                        "name": "destination_location",
                        "value": data["destination_location"],
                    },
                    {"name": "shipment_date", "value": data["shipment_date"]},
                    {
                        "name": "transport_conditions",
                        "value": data["transport_conditions"],
                    },
                ],
            },
            "filter": {
                "indy": {
                    "cred_def_id": "13ZM7KEfAzLC12q1R1SiTS:3:CL:2308438:Transportation",
                    "issuer_did": "13ZM7KEfAzLC12q1R1SiTS",
                    "schema_id": "13ZM7KEfAzLC12q1R1SiTS:2:AATP_TransportationSchema:1.1",
                    "schema_name": "AATP_TransportationSchema",
                    "schema_version": "1.1",
                }
            },
            "trace": True,
        }
        # Convert credential_data to JSON string
        credential_data_json = json.dumps(credential_data)
        result = issue_credential(
            credential_data_json, auth_token=AUTH_TOKEN, url=API_URL
        )
        return jsonify(result)
    return render_template("new_transportation.html")


@app.route("/query-connections", methods=["GET"])
def api_query_connections():
    """
    Query active connections.

    This endpoint retrieves the active connections and returns the result as JSON.

    Returns:
        JSON response with the list of active connections.
    """
    result = query_active_connections(auth_token=AUTH_TOKEN, url=API_URL)
    return jsonify(result)


@app.route("/query-messages", methods=["GET"])
def api_query_messages():
    """
    Query messages for a specific connection.

    This endpoint retrieves messages based on the connection ID and state (sent or received)
    and returns the result as JSON.

    Returns:
        JSON response with the list of messages for the specified connection.
    """
    connection_id = request.args.get("connection_id")
    state = request.args.get("state", "sent")
    result = query_messages(connection_id, state, auth_token=AUTH_TOKEN, url=API_URL)
    return jsonify(result)


@app.route("/send-message", methods=["GET", "POST"])
def api_send_message():
    """
    Send a message to a specific connection.

    If the request method is POST, it processes the form data to send a message
    and returns the result as JSON. If the request method is GET, it renders the
    send message page.

    Returns:
        JSON response with the result of the message sending or renders the send message page.
    """
    if request.method == "POST":
        data = request.form
        result = send_message(
            data["connection_id"], data["content"], auth_token=AUTH_TOKEN, url=API_URL
        )
        return jsonify(result)
    return render_template("send_message.html")


@app.route("/check-status", methods=["GET"])
def api_check_status():
    """
    Check the status of the server.

    This endpoint retrieves the current status of the server and returns the result as JSON.

    Returns:
        JSON response with the server status.
    """
    result = check_status(auth_token=AUTH_TOKEN, url=API_URL)
    return jsonify(result)


@app.route("/fetch-credential-records", methods=["GET", "POST"])
def api_fetch_credential_records():
    """
    Fetch credential records for a specific connection.

    If the request method is POST, it retrieves the credential records for the specified
    connection ID and formats them for rendering. If the request method is GET, it renders
    the fetch credential records page.

    Returns:
        JSON response with the formatted credential records or renders the fetch credential records page.
    """
    credentials = []  # Initialize an empty list to avoid 'NoneType' errors
    if request.method == "POST":
        data = request.form
        credentials = fetch_credential_records(
            data["connection_id"], auth_token=AUTH_TOKEN, url=API_URL
        )

        # Format credentials as needed for rendering
        credentials = credentials["results"]
        result = []
        if credentials:
            for credential in credentials:
                cred_ex_record = credential["cred_ex_record"]
                result.append(
                    {
                        "cred_ex_id": cred_ex_record["cred_ex_id"],
                        "created_at": cred_ex_record["created_at"],
                        "cred_preview": cred_ex_record["cred_preview"]["attributes"],
                        "cred_name": cred_ex_record["by_format"]["cred_offer"]["indy"][
                            "cred_def_id"
                        ].split(":")[-1],
                    }
                )

        return render_template("fetch_credential_records.html", credentials=result)

    return render_template("fetch_credential_records.html", credentials=credentials)


@app.route("/product-trace", methods=["GET", "POST"])
def api_product_trace():
    """
    Trace a product based on its ID.

    If the request method is POST, it retrieves the credential records for the specified
    connection ID, filters them by product ID, and returns the result as JSON. If the
    request method is GET, it renders the product trace page.

    Returns:
        JSON response with the filtered product trace results or renders the product trace page.
    """
    credentials = []  # Initialize an empty list to avoid 'NoneType' errors
    if request.method == "POST":
        data = request.form
        credentials = fetch_credential_records(
            data["connection_id"], auth_token=AUTH_TOKEN, url=API_URL
        )

        # Format credentials as needed for rendering
        credentials = credentials.get("results", [])
        result = []
        for credential in credentials:
            cred_ex_record = credential["cred_ex_record"]
            cred_preview = cred_ex_record["cred_preview"]["attributes"]
            product_info = {attr["name"]: attr["value"] for attr in cred_preview}
            result.append(
                {
                    "cred_ex_id": cred_ex_record["cred_ex_id"],
                    "created_at": cred_ex_record["created_at"],
                    "cred_preview": product_info,
                    "cred_name": cred_ex_record["by_format"]["cred_offer"]["indy"][
                        "cred_def_id"
                    ].split(":")[-1],
                }
            )

        # Only filter the entries which contain the product_id
        product_id = data.get("product_id", "").strip()

        # Let's filter the result to only include the product_id. Use direct access instead of json.dumps
        result_json = [
            credential
            for credential in result
            if "product_id" in credential["cred_preview"]
            and credential["cred_preview"]["product_id"] == product_id
        ]

        return render_template("product_trace.html", credentials=result_json)

    return render_template("product_trace.html", credentials=credentials)


if __name__ == "__main__":
    app.run(debug=True)