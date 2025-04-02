import os

path = "/sys/devices/pci0000:00/0000:00:02.4/0000:05:00.0/nvme/nvme1"

dirs = []

for root, d_names, f_names in os.walk(path):
    dirs.append(d_names)

hwmon_path = ""

if "hwmon" in dirs[0]:
    hwmon_path = path + "/hwmon"
if "hwmon1" in dirs[0]:
    hwmon_path = path + "/hwmon1"
if "hwmon2" in dirs[0]:
    hwmon_path = path + "/hwmon2"
if "hwmon3" in dirs[0]:
    hwmon_path = path + "/hwmon3"
if "hwmon4" in dirs[0]:
    hwmon_path = path + "/hwmon4"


def get_cpu_temp():

    with open(hwmon_path + "/temp2_input", "r") as file:
        data = file.read()
        return round(int(data) / 1000)


result = "  " + str(get_cpu_temp()) + "  "

print(result)
