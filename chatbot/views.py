
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json, requests,re,requests
from pprint import pprint
from random import shuffle
from api import shortUrl,analytics

VERIFY_TOKEN = 'shubhamjain7&'
PAGE_ACCESS_TOKEN = 'EAACV0IwqWyQBAOitzLccXMY0xrQbFykN3McdB4TyVewF9oNEwa76eCxBcXoOZB4l20Er3u9oyfQMULT5bzEQycHqslzL18NTqLelLrqgcoGmwmItPccG5cGnGGMgUL8LSZBxYE3M2dfsc6ZBfDFe9cuVKMywbfeQyUn7tDvtgZDZD'


def logg(mess,meta='log',symbol='#'):

	print '%s\n%s\n%s'%(symbol*20,mess,symbol*20)


def index(request):
	# giphysearch()
	# set_menu()
	# set_get_started()
	post_facebook_message('asd','assd')
	handle_quickreply('assd','sss')
	
	render_postback("assd","nfu") 
	output_text="stock_search "
	
	return HttpResponse(output_text, content_type='application/json')

def set_get_started():

	post_message_url="https://graph.facebook.com/v2.6/me/thread_settings?access_token=%s"%(PAGE_ACCESS_TOKEN)
	response_msg={
	"setting_type":"call_to_actions",
		"thread_state":"new_thread",
		"call_to_actions":[
		{
			"payload":"Get_started"
		}
		]
	}
	menu_object = json.dumps(response_msg)
	status = requests.post(post_message_url,
			headers = {"Content-Type": "application/json"},
			data = menu_object)

	logg(status.text,'-GET-OBJECT-')
	return

def set_menu():
	post_message_url = 'https://graph.facebook.com/v2.6/me/thread_settings?access_token=%s'%PAGE_ACCESS_TOKEN
	
	response_object =   {
							"setting_type" : "call_to_actions",
							"thread_state" : "existing_thread",
							"call_to_actions":[
							{
								"type":"postback",
								"title":"HELP",
								"payload":"MENU_HELP"
							},
							
							
							]
						}

	menu_object = json.dumps(response_object)
	status = requests.post(post_message_url,
			headers = {"Content-Type": "application/json"},
			data = menu_object)

	logg(status.text,'-MENU-OBJECT-')
	return

def set_greeting_text():
	post_message_url = "https://graph.facebook.com/v2.6/me/thread_settings?access_token=%s"%PAGE_ACCESS_TOKEN
	greeting_text = "Url-shortner-bot: Type something like this 'Hey bot"
	greeting_object = json.dumps({"setting_type":"greeting", "greeting":{"text":greeting_text}})
	status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=greeting_object)
	pprint(status.json())
	return

def handle_quickreply(fbid,payload):
	if not payload:
		return

	post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
	logg(payload,symbol='-QR-')
	payload=str(payload)
	try:

		response,clicks,browser,countries,platform,referrers=payload.split("@")
		if response=="true":

			response_msg = {"recipient":{"id":fbid}, "message":{"text":clicks}}
			response_msg = json.dumps(response_msg)
			requests.post(post_message_url,headers={"Content-Type": "application/json"},data=response_msg)

			browser="Browsers clicks\n"+browser
			response_msg1 = {"recipient":{"id":fbid}, "message":{"text":browser}}
			response_msg1= json.dumps(response_msg1)
			requests.post(post_message_url,headers={"Content-Type": "application/json"},data=response_msg1)

			countries="Countries clicks\n"+countries
			response_msg2 = {"recipient":{"id":fbid}, "message":{"text":countries}}
			response_msg2= json.dumps(response_msg2)
			requests.post(post_message_url,headers={"Content-Type": "application/json"},data=response_msg2)

			platform="Platforms\n"+platform
			response_msg3 = {"recipient":{"id":fbid}, "message":{"text":platform}}
			response_msg3= json.dumps(response_msg3)
			requests.post(post_message_url,headers={"Content-Type": "application/json"},data=response_msg3)

			referrers="Referrerss\n"+referrers
			response_msg4 = {"recipient":{"id":fbid}, "message":{"text":referrers}}
			response_msg4= json.dumps(response_msg4)
			requests.post(post_message_url,headers={"Content-Type": "application/json"},data=response_msg4)

	except:
		pass
	return


def render_postback(fbid,payload):
	if not payload:
		return

	post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
	logg(payload,symbol='-RP-')
	response_msg = {"recipient":{"id":fbid}, "message":{"text":payload}}
	
	if payload=="MENU_HELP":
		output_text="Type your url(starting with https or www) to get it shortened or type your \"https://goo.gl/\" ie shortened url to know your url stats"
		response_msg = {"recipient":{"id":fbid}, "message":{"text":output_text}}

	if payload=="Get_started":
		output_text="Hello there, I am a Url-shortner-bot. Type your url(starting with https or www) to get it shortened or type your \"https://goo.gl/\" ie shortened url to know your url stats"
		response_msg = {"recipient":{"id":fbid}, "message":{"text":output_text}}

	

	response_msg = json.dumps(response_msg)
	requests.post(post_message_url,headers={"Content-Type": "application/json"},data=response_msg)
	return

def post_facebook_message(fbid, recevied_message):
	if  recevied_message:
		post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
		response=''
		joke_text="Hello there, I am a Url-shortner-bot. Type your url(starting with https or www) to get it shortened or type your \"https://goo.gl/\" ie shortened url to know your url stats"
		flag1=0
		tokens = re.sub(r"[^a-zA-Z0-9\s]",' ',recevied_message).lower().split()
		for token in tokens:
			if token=="hello" or token=="hi" or token=="hey" or token=="yo" or token=="hii" or token=="hiii" or token=="heya" or token=="hola" or token=="hai" or token=="hie" or token=="hye":
				response = json.dumps({"recipient":{"id":fbid}, "message":{"text":joke_text}})
			
				status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response)
				pprint(status.json())
				flag1=1
				break 

		if flag1==0:
			flag2=0
			flag3=0
			if recevied_message.startswith("https://goo.gl"):
				flag2=1
				try:
					status,created,alltime_short,alltime_browsers,alltime_countries,alltime_platforms,alltime_referrers,month_short,month_browsers,month_countries,month_platforms,month_referrers,week_short,week_browsers,week_countries,week_platforms,week_referrers,day_short,day_browsers,day_countries,day_platforms,day_referrers=analytics(recevied_message)
					if status=="OK":
						All_time="Number of all time clicks: "+alltime_short
						Month="Number of Month clicks: "+month_short
						Week="Number of Week clicks: "+week_short
						Day="Number of Day clicks: "+day_short

						response =json.dumps(   {

						"recipient":{
							"id":fbid
							},
							"message":{
							"text":"The link was created on : \""+created+"\"\nOver what time period do you want to find the stats of clicks??",
							"quick_replies":[
							 
								{
								"content_type":"text",
								"title":"All time clicks ",
								"payload":"true"+"@"+All_time+"@"+alltime_browsers+"@"+alltime_countries+"@"+alltime_platforms+"@"+alltime_referrers
								},
								{
								"content_type":"text",
								"title":"Month clicks",
								"payload":"true"+"@"+Month+"@"+month_browsers+"@"+month_countries+"@"+month_platforms+"@"+month_referrers
								},
								{
								"content_type":"text",
								"title":"Week clicks",
								"payload":"true"+"@"+Week+"@"+week_browsers+"@"+week_countries+"@"+week_platforms+"@"+week_referrers
								},
								{
								"content_type":"text",
								"title":"Day Clicks",
								"payload":"true"+"@"+Day+"@"+day_browsers+"@"+day_countries+"@"+day_platforms+"@"+day_referrers
								},
								
							]
							}

							})
						status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response)
						

					else:
						text="The status of the link is :" +status
						response = json.dumps({"recipient":{"id":fbid}, "message":{"text":text}})
						status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response)
					

				
				except:
					text="No such generated link found.Please check your link"
					response = json.dumps({"recipient":{"id":fbid}, "message":{"text":text}})
					status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response)
					

			if flag2==0:
		
				if "https" in recevied_message or "www" in recevied_message or "http" in recevied_message:
					flag3=1
					recevied_message=shortUrl(recevied_message)
					text="Here is your shortened url: " +recevied_message+"\n\n You can message me the generated url anytime to know it's stats "
					response = json.dumps({"recipient":{"id":fbid}, "message":{"text":text}})
						
					status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response)

				if flag3==0 and "https" not in recevied_message:
					text="I only accept the link with https and www in the beginning"
					response = json.dumps({"recipient":{"id":fbid}, "message":{"text":text}})
					status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response)
			
				


	

class MyChatBotView(generic.View):
  def get (self, request, *args, **kwargs):
    if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
      return HttpResponse(self.request.GET['hub.challenge'])
    else:
      return HttpResponse('Oops invalid token')

  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return generic.View.dispatch(self, request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    incoming_message= json.loads(self.request.body.decode('utf-8'))
    
    logg(incoming_message)

    for entry in incoming_message['entry']:
      for message in entry['messaging']:

        try:
          if 'postback' in message:
            render_postback(message['sender']['id'],message['postback']['payload'])
            return HttpResponse()
          else: 
            pass
        except Exception as e:
          logg(e,symbol='-140-')

        try:
          if 'quick_reply' in message['message']:
            handle_quickreply(message['sender']['id'],
              message['message']['quick_reply']['payload'])
            return HttpResponse()
          else:
            pass
        except Exception as e:
          logg(e,symbol='-140-')
        
        try:
          sender_id = message['sender']['id']
          message_text = message['message']['text']
          post_facebook_message(sender_id,message_text) 
        except Exception as e:
          logg(e,symbol='-147-')

    return HttpResponse()
