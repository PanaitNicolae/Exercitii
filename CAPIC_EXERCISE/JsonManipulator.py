from datetime import datetime


def sort_cur_low_high(obj_list):
    return int(obj_list.reference.current_health)


def sort_time_high_low(obj_list):
    return datetime.strptime(obj_list.modTs, "%d-%m-%Y, %H:%M:%S %p")


class JsonManipulator:
    @staticmethod
    def sort_by_health(obj_list):
        obj_list.sort(key = sort_cur_low_high, reverse = False)
        return obj_list

    @staticmethod
    def sort_by_time(obj_list):
        obj_list.sort(key=sort_time_high_low, reverse=True)
        return obj_list