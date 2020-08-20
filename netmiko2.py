#Khai báo các thư viện cần thiết để chạy code
from netmiko import ConnectHandler      #Gọi hàm ConnectHandler() từ thư viện netmiko
from getpass import getpass             #Gọi hàm getpass() để bảo mật mật khẩu ssh

#Phần truy cập, từ giao diện command của python
print("Bắt đầu phiên truy cập")
access_ip_device = input("Nhập địa chỉ IP SSH: ")            #Truy cập vào địa chỉ ip của host được nhập từ bàn phím
device_username = input("Nhập username: ")          #Lấy user được nhập từ bàn phím
ssh_password = getpass("Nhập mật khẩu: ")                #Yêu cầu nhập mật khẩu SSH để truy cập vào thiết bị

#Khai báo container lưu trữ dữ liệu ban đầu:
cisco_router = {
    'device_type': 'cisco_ios',
    'host': access_ip_device,
    'username': device_username,
    'passwordSSH': ssh_password,                                
}

#Phiên làm việc, với container net_connect đại diện cho thiết bị có cấu hình đã được khai báo trong diction cisco_router
net_connect = ConnectHandler(**cisco_router)                
net_connect.send_config_set(['int f0/1', 'ip add 192.168.10.1 255.255.255.0', 'no shutdown', 'exit'])
net_connect.send_config_set(['int loopback 0', 'ip add 192.168.20.1 255.255.255.0', 'no shutdown', 'exit'])
output = net_connect.send_command('show ip int br')

#Lưu trữ dữ liệu vào file cấu hình "txt"
with open('router_ip_int.txt', 'w+') as file_access:
    file_access.write("IP interfaces:")
    file_access.write(output)

#Vì tiến trình cấu hình và xuất cấu hình thiết bị ra file tốn một khoảng thời gian nhất định để chạy ngầm
#Nên cần chương trình xuất ra Thông báo kết thúc phiên làm việc
print('All task have been complete. Press enter to stop.')