from HealthInst_File import *
from JsonManipulator import *
from datetime import datetime


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

    @staticmethod
    def format_str(str, replace_with="-"):
        if str == "":
            str = replace_with
        return str

    @staticmethod
    def format_time(time_str, format_type = "%Y-%m-%dT%H:%M:%S.%f%z"):
        time_obj = datetime.strptime(time_str, format_type)
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
        self.reference.retrieve_healthInst_info(dict)

    def display_information(self):
        print(f"Name: {self.name}\
                \nTenant name: {self.tenant_name}\
                \nDescription: {self.description}\
                \nName alias: {self.name_alias}\
                \nCtx profile name: {self.ctx_profile_name}\
                \nHealth: {self.reference.current_health}\
                \nTime: {self.modTs}")