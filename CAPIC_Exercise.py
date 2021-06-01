import json
with open("CAPIC_RESPONSE") as capic_response_json:
    capic_response = json.load(capic_response_json)

hcloudCtx_attributes = capic_response["imdata"][0]["hcloudCtx"]["attributes"]
health_attributes = capic_response["imdata"][0]["hcloudCtx"]["children"][0]["healthInst"]["attributes"]



class JsonManipulator:
    def get_name(self, hcloudCtx_attributes):
        name = hcloudCtx_attributes["name"]
        if name == "":
            name = "-"
        return name


    def get_tenant_name(self, hcloudCtx_attributes):
        tenant_name = hcloudCtx_attributes["tenantName"]
        if tenant_name == "":
            tenant_name = "-"
        return tenant_name


    def get_description(self, hcloudCtx_attributes):
        description = hcloudCtx_attributes["description"]
        if description == "":
            description = "-"
        return description


    def get_name_alias(self, hcloudCtx_attributes):
        name_alias = hcloudCtx_attributes["nameAlias"]
        if name_alias == "":
            name_alias = "-"
        return name_alias


    def get_ctx_profile_name(self, hcloudCtx_attributes):
        ctx_profile_name = hcloudCtx_attributes["ctxProfileName"]
        if ctx_profile_name == "":
            ctx_profile_name = "-"
        return ctx_profile_name


    def get_current_health(self, health_attributes):
        current_health = health_attributes["cur"]
        return current_health


    def get_maxsev(self, health_attrbutes):
        max_sev = health_attrbutes["maxSev"]
        return max_sev


class CloudCtx(JsonManipulator):
    def __init__(self):
        self.name = self.get_name(hcloudCtx_attributes)
        self.tenant_name = self.get_tenant_name(hcloudCtx_attributes)
        self.description = self.get_description(hcloudCtx_attributes)
        self.name_alias = self.get_name_alias(hcloudCtx_attributes)
        self.ctx_profile_name = self.get_ctx_profile_name(hcloudCtx_attributes)


    def display_information(self):
        print(f"Name: {self.name}\nTenant name: {self.tenant_name}\nDescription: {self.description}\nName alias: {self.name_alias}\nCtx profile name: {self.ctx_profile_name}")


class HealthInst(CloudCtx):
    def __init__(self):
        self.current_health = self.get_current_health(health_attributes)
        self.max_sev = self.get_maxsev(health_attributes)


    def display_health(self):
        if int(self.current_health) < 100:
            print("Unhealthy")
        else:
            print("Healthy")




a = CloudCtx()
# a.display_information()
b = HealthInst()
b.display_health()
