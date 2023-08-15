#!/usr/bin/python

__author__ = "HPInc."

#
# DELETE ME!
# Import parent directory to the sys.path to be able to load OneflowSDK
#

import sys, os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

#
# Order submission logic
#

import json, string, random, os
from OneflowSDK import OneflowSDK

# oneflow acccess credentials
token = os.environ["ONEFLOW_TOKEN"]
secret = os.environ["ONEFLOW_SECRET"]
siteflowEndpoint = "https://pro-api.oneflowcloud.com"
submissionEndpoint = "https://orders.oneflow.io"

# OneflowSDK instances
siteflowClient = OneflowSDK(siteflowEndpoint, token, secret)
submisionClient = OneflowSDK(submissionEndpoint, token, secret)


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def validate_order(order):
    print("Validating Order")
    return siteflowClient.request("POST", "/api/order/validate", order)


def submit_order(order):
    print("Submitting Order")
    return submisionClient.request("POST", "/api/order", order)


# Here are the variables required for a single item order
# this is not a full set of fields available
destination = "oneflow"
orderId = id_generator()
itemId = id_generator()
sku = "card"
quantity = 1
fetchPath = "https://files-static.hpsiteflow.com/samples/CardSample.pdf"
componentCode = "Card"
shipTo = {
    "name": "John Doe",
    "address1": "1 Primrose Street",
    "town": "London",
    "postcode": "12345",
    "isoCountry": "GB",
    "email": "info@domain.com",
    "phone": "01234567890",
}
carrier = {"code": "royalmail", "service": "firstclass"}

# nothing to change below here

# create an item - this goes into the order below
item = {
    "sourceItemId": itemId,
    "sku": sku,
    "quantity": quantity,
    "components": [{"code": componentCode, "path": fetchPath, "fetch": True}],
}

# create a shipment - this goes into the order below
shipment = {"shipTo": shipTo, "carrier": carrier}

# put together the complete order
order = {
    "destination": {"name": destination},
    "orderData": {"sourceOrderId": orderId, "items": [item], "shipments": [shipment]},
}

# validate the order
print(validate_order(json.dumps(order)))

# finally, submit the order
print(submit_order(json.dumps(order)))
