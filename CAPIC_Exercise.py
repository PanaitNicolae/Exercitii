import json
import time
from datetime import datetime
with open("CAPIC_RESPONSE") as capic_response_json:
    capic_response = json.load(capic_response_json)

dict_list = capic_response["imdata"]


class JsonManipulator:
    pass


class CloudCtx(JsonManipulator):
    track_number = 0
    def __init__(self):
        self.name = None
        self.tenant_name = None
        self.description = None
        self.name_alias = None
        self.ctx_profile_name = None
        self.modTs = None
        self.reference = HealthInst()
        CloudCtx.track_number += 1

    def format_str(self, str, replace_with="-"):
        if str == "":
            str = replace_with
        return str

    def format_time(self,time_str, type = "%Y-%m-%dT%H:%M:%S.%f%z"):
        time_obj = datetime.strptime(time_str, type)
        time_string = datetime.strftime(time_obj, "%d-%m-%Y, %H:%M:%S %p")
        return time_string

    def retrieve_hcloudCtx_info(self, dict):
        hcloudCtx_attributes = dict["hcloudCtx"]["attributes"]
        name = self.format_str(hcloudCtx_attributes["name"])
        tenant_name = self.format_str(hcloudCtx_attributes["tenantName"])
        description = self.format_str(hcloudCtx_attributes["description"])
        name_alias = self.format_str(hcloudCtx_attributes["nameAlias"])
        ctx_profile_name = self.format_str(hcloudCtx_attributes["ctxProfileName"])
        modTs = self.format_time(hcloudCtx_attributes["modTs"])
        self.name = name
        self.tenant_name = tenant_name
        self.description = description
        self.name_alias = name_alias
        self.ctx_profile_name = ctx_profile_name
        self.modTs = modTs

    def display_information(self):
        print(f"Name: {self.name}\
                \nTenant name: {self.tenant_name}\
                \nDescription: {self.description}\
                \nName alias: {self.name_alias}\
                \nCtx profile name: {self.ctx_profile_name}\
                \nHealth: {self.reference.current_health}\
                \nTime: {self.modTs}")


class HealthInst(JsonManipulator):
    def __init__(self):
        self.current_health = None
        self.max_sev = None

    def retrieve_healthInst_info(self, dict):
        if len(dict["hcloudCtx"]["children"]) == 0:
            self.current_health = 0
            self.max_sev = "-"
        else:
            health_attributes = dict["hcloudCtx"]["children"][0]["healthInst"]["attributes"]
            self.current_health = health_attributes["cur"]
            self.max_sev = health_attributes["maxSev"]

    def display_health(self):
        if int(self.current_health) < 100:
            print("Unhealthy")
        else:
            print("Healthy")


def sort_cur_low_high(obj_list):
    return int(obj_list.reference.current_health)

def sort_time_high_low(obj_list):
    return obj_list.modTs


CloudCtx_obj_list = []
for i in dict_list:
    obj = CloudCtx()
    obj.retrieve_hcloudCtx_info(i)
    obj.reference.retrieve_healthInst_info(i)
    CloudCtx_obj_list.append(obj)

CloudCtx_obj_list.sort(key = sort_cur_low_high, reverse = False)
for i in CloudCtx_obj_list:
    i.display_information()
    print("\n")


CloudCtx_obj_list.sort(key = sort_time_high_low, reverse = True)
for i in CloudCtx_obj_list:
    i.display_information()
    print("\n")


