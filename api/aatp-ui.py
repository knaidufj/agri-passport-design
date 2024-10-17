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
    return render_template("index.html")


@app.route("/create-schema", methods=["GET", "POST"])
def api_create_schema():
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
    if request.method == "GET":
        schema_id = request.args.get("schema_id")
        result = get_schema(schema_id, auth_token=AUTH_TOKEN, url=API_URL)
        return jsonify(result)
    return render_template("get_schema.html")


@app.route("/get-cred-def", methods=["GET", "POST"])
def api_get_cred_def():
    if request.method == "GET":
        cred_def_id = request.args.get("credential_definition_id")
        result = get_credential_definition(
            cred_def_id, auth_token=AUTH_TOKEN, url=API_URL
        )
        return jsonify(result)
    return render_template("get_cred_def.html")


@app.route("/create-cred-def", methods=["GET", "POST"])
def api_create_cred_def():
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
    if request.method == "POST":
        data = request.form
        result = issue_credential(
            data["credential_data"], auth_token=AUTH_TOKEN, url=API_URL
        )
        return jsonify(result)
    return render_template("issue_credential.html")


@app.route("/new-user", methods=["GET", "POST"])
def api_new_user():
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
                            hashlib.sha256((data["producer_id"] + data["certification_date"] + data["certification_authority_id"] + str(random.randint(0, 1000000))).encode()).hexdigest()
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
                            hashlib.sha256((data["producer_id"] + str(random.randint(0, 1000000))).encode()).hexdigest()
                        )[:6],
                    },
                    {"name": "product_name", "value": data["product_name"]},
                    {"name": "producer_id", "value": data["producer_id"]},
                    {"name": "production_date", "value": data["production_date"]},
                    {"name": "expiration_date", "value": data["expiration_date"]}
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
                            hashlib.sha256((data["producer_id"] + str(random.randint(0, 1000000))).encode()).hexdigest()
                        )[:6],
                    },
                    {"name": "product_id", "value": data["product_id"]},
                    {"name": "packaging_date", "value": data["packaging_date"]},
                    {"name": "packaging_facility_id", "value": data["packaging_facility_id"]},
                    {"name": "packaging_conditions", "value": data["packaging_conditions"]},
                    {"name": "batch_number", "value": data["batch_number"]}
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
    if request.method == "POST":
        data = request.form
        credential_data = {
            "connection_id": data["connection_id"],
            "credential_preview": {
                "@type": "issue-credential/2.0/credential-preview",
                "attributes": [
                    {
                        "name": "shipment_id",
                        "value": str(
                            hashlib.sha256((data["product_id"] + str(random.randint(0, 1000000))).encode()).hexdigest()
                        )[:6],
                    },
                    {"name": "product_id", "value": data["product_id"]},
                    {"name": "origin_location", "value": data["origin_location"]},
                    {"name": "destination_location", "value": data["destination_location"]},
                    {"name": "shipment_date", "value": data["shipment_date"]},
                    {"name": "transport_conditions", "value": data["transport_conditions"]}
                ],
            },
            "filter": {
                "indy": {
                    "cred_def_id": "13ZM7KEfAzLC12q1R1SiTS:3:CL:2308438:Transportation",
                    "issuer_did": "13ZM7KEfAzLC12q1R1SiTS",
                    "schema_id": "13ZM7KEfAzLC12q1R1SiTS:2:AATP_TransportationSchema:1.1",
                    "schema_name": "AATP_TransportationSchema",
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
    return render_template("new_transportation.html")

@app.route("/query-connections", methods=["GET"])
def api_query_connections():
    result = query_active_connections(auth_token=AUTH_TOKEN, url=API_URL)
    return jsonify(result)


@app.route("/query-messages", methods=["GET"])
def api_query_messages():
    connection_id = request.args.get("connection_id")
    state = request.args.get("state", "sent")
    result = query_messages(connection_id, state, auth_token=AUTH_TOKEN, url=API_URL)
    return jsonify(result)


@app.route("/send-message", methods=["GET", "POST"])
def api_send_message():
    if request.method == "POST":
        data = request.form
        result = send_message(
            data["connection_id"], data["content"], auth_token=AUTH_TOKEN, url=API_URL
        )
        return jsonify(result)
    return render_template("send_message.html")


@app.route("/check-status", methods=["GET"])
def api_check_status():
    result = check_status(auth_token=AUTH_TOKEN, url=API_URL)
    return jsonify(result)


@app.route("/fetch-credential-records", methods=["GET", "POST"])
def api_fetch_credential_records():
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


if __name__ == "__main__":
    app.run(debug=True)
