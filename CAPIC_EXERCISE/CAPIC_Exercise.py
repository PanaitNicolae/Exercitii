import json
from CloudCtx_File import *
import argparse

parser = argparse.ArgumentParser(description="CAPIC EXERCISE")
parser.add_argument("json_file",help="File name where is the CAPIC response.")
arg = parser.parse_args()

with open("CAPIC_RESPONSE") as capic_response_json:
    capic_response = json.load(capic_response_json)

dict_list = capic_response["imdata"]

CloudCtx_obj_list = []
for i in dict_list:
    obj = CloudCtx()
    obj.retrieve_hcloudCtx_info(i)
    CloudCtx_obj_list.append(obj)

list_sorted_by_health = CloudCtx.sort_by_health(CloudCtx_obj_list)
for i in list_sorted_by_health:
    i.display_information()
    print("\n")

list_sorted_by_time = CloudCtx.sort_by_time(CloudCtx_obj_list)
for i in list_sorted_by_time:
    i.display_information()
    print("\n")
