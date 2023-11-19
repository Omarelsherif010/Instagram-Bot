from instagrapi import Client

username = 'omarelsherif0101'
password = 'Collegeboard@010#instagram'

cl = Client()
cl.login(username, password)
cl.dump_settings("session.json")