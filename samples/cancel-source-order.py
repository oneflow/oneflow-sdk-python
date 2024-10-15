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
# Cancel source order request logic
#

import json, os
from OneflowSDK import OneflowSDK

# credentials and endpoint
token = os.environ["ONEFLOW_TOKEN"]
secret = os.environ["ONEFLOW_SECRET"]
endpoint = "https://pro-api.oneflowcloud.com"

# OneflowSDK instance
client = OneflowSDK(endpoint, token, secret)

# specific api call
source_name = "CHANGE_ME_YOUR_SOURCE_NAME"
source_order_id = "CHANGE_ME_YOUR_SOURCE_ORDER_ID"

api_path = "/api/order/{source_name}/{source_order_id}/cancel".format(source_name=source_name, source_order_id=source_order_id)

# make the PUT request to the endpoint
r = client.request("PUT", api_path)

# output the results
print("result", r)
