import json
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
        self.reference = HealthInst()
        CloudCtx.track_number += 1

    def retrieve(self, dict):
        hcloudCtx_attributes = dict["hcloudCtx"]["attributes"]
        self.name = hcloudCtx_attributes["name"] if hcloudCtx_attributes["name"] != "" else "-"
        self.tenant_name = hcloudCtx_attributes["tenantName"] if hcloudCtx_attributes["tenantName"] !="" else "-"
        self.description = hcloudCtx_attributes["description"] if hcloudCtx_attributes["description"] != "" else "-"
        self.name_alias = hcloudCtx_attributes["nameAlias"] if hcloudCtx_attributes["nameAlias"] !="" else "-"
        self.ctx_profile_name = hcloudCtx_attributes["ctxProfileName"] if hcloudCtx_attributes["ctxProfileName"] != "" else "-"

    def display_information(self):
        print(f"Name: {self.name}\nTenant name: {self.tenant_name}\nDescription: {self.description}\nName alias: {self.name_alias}\nCtx profile name: {self.ctx_profile_name} \nHealth: {self.reference.current_health} ")



class HealthInst(JsonManipulator):
    def __init__(self):
        self.current_health = None
        self.max_sev = None


    def retrieve(self, dict):
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


def sort_func(obj_list):
    return int(obj_list.reference.current_health)



CloudCtx_obj_list = []
for i in dict_list:
    obj = CloudCtx()
    obj.retrieve(i)
    obj.reference.retrieve(i)
    CloudCtx_obj_list.append(obj)

CloudCtx_obj_list.sort(key = sort_func, reverse = False)
for i in CloudCtx_obj_list:
    i.display_information()
    print("\n")

print(CloudCtx.track_number)
# a.display_information()

