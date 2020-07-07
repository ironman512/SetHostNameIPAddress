
#!/bin/python
import os, sys

############## START Check Root Login ###################
# This script must be run as root!
if not os.geteuid()==0:
    sys.exit('This script must be run as root!')

############## END Check Root Login ######################

############ Start Set HostName Section #####################
set_host_name = input("Set Host-Name: ")
os.system("hostnamectl set-hostname " +set_host_name)
print("Host-Name Set Successfully...")
############### END Set HostName Section #####################


########### Start nmtui section  ###############
# If IP Address set By ncurses Screen then uncomment below line and comment nmcli  section
#os.system("nmtui")
################## End nmtui section ###########


######################### START nmcli section ##########################
os.system("nmcli device status | awk '{print $4}'")

interface_name = input("Select Interface which you want to set IP Address: ")
#print(interface_name)

set_ip = input("Set IP Address/Subnet in CIDR Format- XX.XX.XX.XX/XX : " )
os.system("nmcli connection modify " +interface_name +" ipv4.address " +set_ip)

set_getway = input("Set Gateway : ")
os.system("nmcli connection modify " +interface_name +" ipv4.gateway " +set_getway)

#work in progress
#set_dns1 = input("Set DNS1 : ")
#os.system("nmcli connection modify " +interface_name +" ipv4.gateway " +set_getway")

os.system("nmcli connection modify "+interface_name +" ipv4.method manual")
os.system("nmcli con up "+interface_name)

############################### END nmcli Section ################################

#nmcli con mod net-eth0 ipv4.addresses "192.168.2.10/24 192.168.2.1"


#ipv4 = os.popen('ip addr show eth0 | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\'').read().strip()
#ipv6 = os.popen('ip addr show eth0 | grep "\<inet6\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\'').read().strip()


# yum install bash-completion bash-completion-extras
#  nmcli device status
# nmcli device status | awk '{print $4}'