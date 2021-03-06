import os
import json
from rich.console import Console
from rich.text import Text
console = Console()

def main_menu():    
	console.print('\t1.Status of containers',style="bold cyan")
	console.print('\t2.Download new Image',style="bold cyan")
	console.print('\t3.Run container',style="bold cyan")
	console.print('\t4.Delete Container',style="bold cyan")
	console.print('\t5.Network details of container',style="bold cyan")
	console.print('\t6.Modify Network details of contaniner',style="bold cyan")
	console.print('\t7.Exit',style="bold red")
	
def rich_func(res):

	console.print(Text(res,style="bold blue"))
	
def Status_of_container():

	print(os.popen("docker ps -a").read())
	#os.system("sudo docker container stats")

def Downld_img():

	image = input("Enter the image name :")
	print(f"docker pull {image}")
	res = os.popen(f"docker pull {image}").read()
	rich_func(res)

def Run_container():

	image = input("Enter the image name :")
	container = input("Enter the container name :")
	cmd = f"docker run --name {container} {image}"
	res = os.popen(cmd).read()
	rich_func(res)
	console.print(f"{container} is created successfully",style="bold red")

def Del_Container():

	container_name = input("Enter the container name to delete :")
	cmd = f"docker rm {container_name}"
	res = os.popen(cmd).read()
	#rich_func(res)
	console.print(f"{container_name} is removed successfully",style="bold red")

def Network_detail_container():

	cmd = f"docker network inspect bridge"
	res = os.popen(cmd).read()
	rich_func(res)
	l = json.loads(res)[0]
	for i in l["Containers"].values():
		console.print(f'{i["Name"]} | {i["MacAddress"]} | {i["IPv4Address"]}',style="bold magenta" )

def Modify_Network_detail_contaniner(): 
   
	res = os.popen("docker network ls").read()
	rich_func(res)
	
	network = input("Enter the network name : ")
	container_image = input("Enter the container name to disconnect from network :")
	print(f"Disconnecting {container_image} from {network}")
	cmd =f"docker network disconnect bridge {container_image}"
	print(os.popen(cmd).read())
	console.print("Disconnected network",style="bold blue")
	
	console.print("Creating Network", style="bold cyan")
	ip = input('enter ip for network/cidr :')
	cmd1=f"sudo docker network create -d bridge --subnet={ip}  {network}"
	print(os.popen(cmd1).read())
	print(f"Connecting {container_image} to  {network}")
	
	cmd2 = f"docker network connect {network} {container_image}"
	print(os.popen(cmd2).read())
	console.print("Connected to network",style="bold blue")

def Exit():
	console.print("Successfully Exited",style="bold green")
	exit()	
	
operations = {
	"1":Status_of_container,
	"2":Downld_img,
	"3":Run_container,
	"4":Del_Container,
	"5":Network_detail_container,
	"6":Modify_Network_detail_contaniner,
	"7":Exit
	
}

while True:

	main_menu()
	ch = input("Enter Choice: ")
	operations[ch]()
