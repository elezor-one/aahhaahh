from datetime import datetime as date
from time import sleep
from os import system as terminal
from pyrogram import Client as session
from time import perf_counter as perf 
import os, sys

def poll(num):
	if num == 0:
		terminal('printf "\e[0;0m"')
	else:
		terminal('printf "\e[1;91m"')	
	return True
	
def printf(text):
	terminal(f'printf """{text}"""')
	return True
	
app = {
1: session('1'),
}

poll(0)
dead = 0 ; accounts = 0
for _ in app:
	try:
		app[_].start()
		me = app[_].get_me()
		accounts += 1
		print(f'[√] {me.first_name}({me.id}) launched')
	except Exception as exc:
		dead += 1
		print(f'[x] failed to launched\n{exc}')
		
while True:
	run = 0
	while run != 1:
		terminal('clear')
		poll(0)
		print(
f'[*] total accounts> {accounts}\n'
f'[1] flood to pm\n'
f'[2] join to chat\n'
f'[3] flood to chat\n'
f'[4] leave to chat\n'
f'[5] change bio\n'
f'[6] check ping\n'
f'[7] restart botnet\n'
f'[8] report to user'
			)			
		action = input('>> ')
		if action == "1" or action == "2" or action == "3" or action == "4" or action == "5" or action == "6" or action == "7" or action == "8":
			run = 1
		else:
			poll(1)
			print('[x] invalid option...')
			poll(0)
			sleep(2)

	# flood to pm
	if action == '1':
		poll(1)
		printf('username> ')
		poll(0)
		username = input()
		poll(1)
		printf('text> ')
		poll(0)
		text = input()
		poll(1)
		printf('gif(y/n)> ')
		poll(0)
		gif = input()
		if gif == 'y':
			poll(1)
			printf('link> ')
			poll(0)
			link = input()
		poll(1)
		printf('msgs> ')
		poll(0)
		msgs = int(input())
		poll(0)
		sms = 0
		ping = perf()
		for z in range(msgs):
			for _ in app:
				try:
					if gif == 'y':
						app[_].send_video(username, link, caption=text)
						sms += 1
						print(f'[v] send {sms} message(gif)')
					else:
						app[_].send_message(username, text)
						sms += 1
						print(f'[v] send {sms} message(text)')
				except:
						print(f'[x] failed to send message')
		ping = perf() - ping
		ping = round(ping, 1)
		print(f'[√] all msgs send in {ping}s')
		input('[*] click enter to continue')
	
	# join to chat
	if action == '2':
		poll(1)
		printf('group> ')
		poll(0)
		group = input()
		poll(0)
		ping = perf()
		for _ in app:
			try:
				app[_].join_chat(group)
				print(f'[v] account {_} joined to chat')
			except:
				print(f'[x] failed to join to chat')
		ping = perf() - ping
		ping = round(ping, 1)
		print(f'[√] all accounts joined in {ping}s')
		input('[*] click enter to continue')	

	# flood to chat
	if action == '3':
		poll(1)
		printf('group> ')
		poll(0)
		group = input()
		poll(1)
		printf('text> ')
		poll(0)
		text = input()
		poll(1)
		printf('gif(y/n)> ')
		poll(0)
		gif = input()
		if gif == 'y':
			poll(1)
			printf('link> ')
			poll(0)
			link = input()
		poll(1)
		printf('msgs> ')
		poll(0)
		msgs = int(input())
		poll(0)
		sms = 0
		ping = perf()
		for z in range(msgs):
			for _ in app:
				try:
					if gif == 'y':
						app[_].send_video(group, link, caption=text)
						sms += 1
						print(f'[v] send {sms} message(gif)')
					else:
						app[_].send_message(group, text)
						sms += 1
						print(f'[v] send {sms} message(text)')
				except:
						print(f'[x] failed to send message')
		ping = perf() - ping
		ping = round(ping, 1)
		print(f'[√] all msgs send in {ping}s')
		input('[*] click enter to continue')	

	# leave to chat
	if action == '4':
		poll(1)
		printf('group> ')
		poll(0)
		group = input()
		poll(0)
		ping = perf()
		for _ in app:
			try:
				app[_].leave_chat(group)
				print(f'[v] account {_} leaved to chat')
			except:
				print(f'[x] failed to leave to chat')
		ping = perf() - ping
		ping = round(ping, 1)
		print(f'[√] all accounts leaved in {ping}s')
		input('[*] click enter to continue')

	# change bio
	if action == '5':
		poll(1)
		printf('bio> ')
		poll(0)
		new = input()
		poll(0)
		ping = perf()
		for _ in app:
			try:
				app[_].update_profile(bio=new)
				print(f'[v] account {_} change bio')
			except:
				print(f'[x] failed to change bio')
		ping = perf() - ping
		ping = round(ping, 1)
		print(f'[√] all accounts change bio in {ping}s')
		input('[*] click enter to continue')
		
	# check ping
	if action == '6':
		poll(0)
		ping = perf()
		for _ in app:
			msg = app[_].send_message('me', 'Я люблю Телеграм ;)')
			msg.delete()
		ping = (perf() - ping) * 1000
		print(f'[v] ping smooth to {ping}ms')
		input('[*] click enter to continue')
	
	# restart botnet
	if action == '7':
		poll(0)
		print('[√] restarting botnet')
		os.execl(sys.executable, sys.executable, *sys.argv) 
		quit() 
			
	# report to user
	if action == '8':
		poll(1)
		printf('group> ')
		poll(0)
		group = input()
		poll(1)
		printf('id> ')
		poll(0)
		id = int(input())
		poll(0)
		ping = perf()
		for _ in app:
			try:
				app[_].forward_messages('notoscam', group, [id])
				print(f'[v] account {_} send report')
			except:
				print('[x] failed to send report')
		ping = perf() - ping
		ping = round(ping, 1)
		print(f'[√] all accounts reported in {ping}s')
		input('[*] click enter to continue')
		
		
idle()	