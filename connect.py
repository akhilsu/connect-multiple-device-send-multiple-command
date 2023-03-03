from netmiko import ConnectHandler

devices = ["10.10.10.10","10.10.10.20","10.10.10.30","10.10.10.40","10.10.10.50"]
commands = ["show version","show platform","show processes cpu","show memory summary","show bgp scale"]

for i in devices:
    device = {
        "device_type" : "cisco_xr",
        "ip" : i,
        "username" : "root",
        "password" : "root@123",
        "port" : 22
    }

    connectdevice = ConnectHandler(**device)
    for j in commands:
        fetch = connectdevice.send_command(j,read_timeout=300)
        print(fetch)
    connectdevice.disconnect()
