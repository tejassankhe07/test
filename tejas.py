from netmiko import ConnectHandler

abc = {
    'device_type': 'cisco_ios',
    'ip': '192.168.252.150',
    'username': 'tejas',
    'password': 'dcne123',
}

abc_session = ConnectHandler(**abc)
print(abc_session.send_command('show interfaces description'))
