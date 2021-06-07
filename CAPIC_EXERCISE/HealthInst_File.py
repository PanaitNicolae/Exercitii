from JsonManipulator import*


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