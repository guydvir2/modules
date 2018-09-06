import json
import os


class JSONconfig:

    def __init__(self, filename, default_values=None):
        self.filename = filename
        self.def_values = {}
        self.data_from_file = None
        self.create_default_file()

    def read_file(self, file=None):
        if file != None:
            self.filename = file

        if os.path.isfile(self.filename) is True:
            with open(self.filename, 'r') as f:
                self.data_from_file = json.load(f)

            print(self.data_from_file)
        else:
            self.create_default_file()

    def create_def_vals(self):
        self.def_values = {"client_ID": 'ESP32_1',
                           "client_topic": 'HomePi/Dvir/my_device',
                           "out_topic": 'HomePi/Dvir/Messages',
                           "listen_topics": 'HomePi/Dvir/Windows/All',
                           "pin_in1": 22, "pin_in2": 19, "pin_out1": 23, "pin_out2": 18,
                           "static_ip": 'None',
                           "SERVER": '192.168.2.113'}

    def create_default_file(self):
        self.create_def_vals()
        self.write2file(self.def_values)

    def write2file(self, dict):
        with open(self.filename, 'w') as f:
            json.dump(dict, f, indent=4, sort_keys=False)
        print("done")

    def update_value(self, key, value):
        self.read_file()
        self.data_from_file[key] = value
        self.write2file(self.data_from_file)


class SchedReader:

    def __init__(self, filename=None, default_values=None, file_type='json'):
        self.def_values = {}
        self.data_from_file = None
        self.filename = filename

        self.read_file()

    def read_file(self, file=None):
        if file != None:
            self.filename = file

        if os.path.isfile(self.filename) is True:
            with open(self.filename, 'r') as f:
                self.data_from_file = json.load(f)
        else:
            self.create_default_file()
            self.data_from_file = self.def_values

        return self.data_from_file

    def create_default_file(self):
        self.def_values = {"topic": 'HomePi/Dvir/Windows/Win1',
                           "schedule_up": [
                               {"start_days": [1, 2, 3, 4, 5], "end_days": [1, 2, 3, 4, 5], "start_time": "06:45:00",
                                "end_time": "06:45:05"},
                               {"start_days": [1, 2, 3, 4, 5, 6, 7], "end_days": [1, 2, 3, 4, 5, 6, 7],
                                "start_time": "02:01:10",
                                "end_time": "02:01:15"}],
                           "schedule_down": [{"start_days": [1, 2, 3, 4, 5, 6, 7], "end_days": [1, 2, 3, 4, 5, 6, 7],
                                              "start_time": "02:00:00",
                                              "end_time": "02:01:00"},
                                             {"start_days": [1, 2, 3, 4, 5], "end_days": [1, 2, 3, 4, 5],
                                              "start_time": "08:00:00",
                                              "end_time": "08:01:00"}],
                           "enable": True}
        self.write2file(self.def_values)

    def write2file(self, dict):
        with open(self.filename, 'w') as f:
            json.dump(dict, f, indent=4, sort_keys=False)

    def update_value(self, key, value):
        self.read_file()
        self.data_from_file[key] = value
        self.write2file(self.data_from_file)

    def get_file_list(self, file_type, path=None):
        file_list = os.listdir(path=path)
        sched_files = []

        for file in file_list:
            try:
                if file.split('.')[1] == file_type:
                    sched_files.append(file)
            except IndexError:
                pass

        return sched_files

    def print_found_files(self):
        files = self.get_file_list(file_type='json')
        for file in files:
            self.read_file(file)


if __name__ == "__main__":
    a = JSONconfig('/home/guy/github/modules/test1.json')
    # a.update_value('client_ID', "ESP8266")
