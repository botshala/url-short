import requests
from pprint import pprint
import json
def shortUrl(url="http://www.google.com/"):
	headers = {
	    'Content-Type': 'application/json',
	}

	data = '{"longUrl": "%s"}'%(url)

	result= requests.post('https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyBVL2rPsRdrWSn35Y3Ru4qf3U6x8EeX6H4', headers=headers, data=data)
	result=result.json()
	return result['id']



def longUrl(url='http://goo.gl/fbsS'):
	result=requests.get('https://www.googleapis.com/urlshortener/v1/url?shortUrl=%s&key=AIzaSyBVL2rPsRdrWSn35Y3Ru4qf3U6x8EeX6H4'%(url))
	result=result.json()
	return result['id'],result['status'] 


def analytics(url='http://goo.gl/fbsS'):
	
	result=requests.get('https://www.googleapis.com/urlshortener/v1/url?shortUrl=%s&projection=FULL&key=AIzaSyBVL2rPsRdrWSn35Y3Ru4qf3U6x8EeX6H4'%(url))
	result=result.json( )

	pprint (result)
	#pprint (result)
	if result['status']=="OK":
		try:
			longUrl=result['longUrl']
		except:
			longUrl="No data found"
		status=result['status']
			#alltime
		alltime_short=result['analytics']['allTime']['shortUrlClicks']

		try:
			alltime_browsers=check(result['analytics']['allTime']['browsers'])
		except:
			alltime_browsers="No data found"


		try:
			alltime_countries=check(result['analytics']['allTime']['countries'])
		except:
			alltime_countries="No data found"


		try:
			alltime_platforms=check(result['analytics']['allTime']['platforms'])
		except:
			alltime_platforms="No data found"


		try:
			alltime_referrers=check(result['analytics']['allTime']['referrers'])
		except:
			alltime_referrers="No data found"




		month_short=result['analytics']['month']['shortUrlClicks']

		try:
			month_browsers=check(result['analytics']['month']['browsers'])
		except:
			month_browsers="No data found"


		try:
			month_countries=check(result['analytics']['month']['countries'])
		except:
			month_countries="No data found"


		try:
			month_platforms=check(result['analytics']['month']['platforms'])
		except:
			month_platforms="No data found"


		try:
			month_referrers=check(result['analytics']['month']['referrers'])
		except:
			month_referrers="No data found"


		week_short=result['analytics']['week']['shortUrlClicks']
		try:
			week_browsers=check(result['analytics']['week']['browsers'])
		except:
			week_browsers="No data found"


		try:
			week_countries=check(result['analytics']['week']['countries'])
		except:
			week_countries="No data found"


		try:
			week_platforms=check(result['analytics']['week']['platforms'])
		except:
			week_platforms="No data found"


		try:
			week_referrers=check(result['analytics']['week']['referrers'])
		except:
			week_referrers="No data found"

		day_short=result['analytics']['day']['shortUrlClicks']
		try:
			day_browsers=check(result['analytics']['day']['browsers'])
		except:
			day_browsers="No data found"

		try:
			day_countries=check(result['analytics']['day']['countries'])
		except:
			day_countries="No data found"

		try:
			day_platforms=check(result['analytics']['day']['platforms'])
		except:
			day_platforms="No data found"

		try:
			day_referrers=check(result['analytics']['day']['referrers'])
		except:
			day_referrers="No data found"

		created=result['created']
		
	else:
		status=result['status']
		created=alltime_short=alltime_browsers=alltime_countries=alltime_platforms=alltime_referrers=month_short=month_browsers=month_countries=month_platforms=month_referrers=week_short=week_browsers=week_countries=week_platforms=week_referrers=day_short=day_browsers=day_countries=day_platforms=day_referrers=status


	return status,created,alltime_short,alltime_browsers,alltime_countries,alltime_platforms,alltime_referrers,month_short,month_browsers,month_countries,month_platforms,month_referrers,week_short,week_browsers,week_countries,week_platforms,week_referrers,day_short,day_browsers,day_countries,day_platforms,day_referrers





def check(item):
	
	try:
		item
		string=''
		for b in item:
			if len(string)<300:
				a=b.values()
				string= string+ a[1]+": "+a[0]+"\n"
		string=str(string)
	except:
		string="No data found"
	return string

print analytics()