from flask import Flask, render_template, request, redirect
from threading import Thread
#this is the link: https://testtesttes.notkar1myt.repl.co
#for invite: https://testtesttes.notkar1myt.repl.co/invite

app = Flask('')

@app.route('/')
def home():
	return f"The Kid Laroi Is Online ✔"



def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()


@app.route('/invite')
def inv():
  	return redirect("https://discord.com/api/oauth2/authorize?client_id=770665928500969502&permissions=0&redirect_uri=https%3A%2F%2Fdiscord.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D770665928500969502%26permissions%3D8%26scope%3Dbot&scope=bot")
