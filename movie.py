import telebot
from telebot import types

names = {
	
	'master': ['BQACAgQAAxkBAAITdmAXl1HOMtXIrC1FQ_q4nsfDKI7yAAJCCgACVmaZUDE6GNbE8hVDHgQ',
			   'BQACAgQAAxkBAAITd2AXl1HFxsUx-BPNVbC0gnavv_qVAAK1BwACOG2YUFy83wknBEkIHgQ',
			   'BQACAgQAAxkBAAITeGAXl1GAV9hXu60h6ohWlzQ6fMkuAAK2BwACOG2YUH-FZjU-UjwKHgQ',
			   'BQACAgQAAxkBAAITeWAXl1HPVIL5SgErAkxyHH4bJMOzAAIgCQACVzGgUPpuO70aTP5zHgQ',
			   'BQACAgQAAxkBAAITemAXl1Eyi9WKw3eKQMkLAsq43lISAAIfCQACVzGgUI9zuj-6Y98JHgQ',
			   'Master 2021 Telugu HDRip'
	],
			   
	'krack' : ['BQACAgQAAxkBAAIcRmAcsoh_IUhbt3pN6fjgSdlMissyAALcCAAC2lrpUHZNnzBop7HUHgQ',
			   'BQACAgQAAxkBAAIcR2Acsoj5kbLSINPtgXSLV3BpcZKfAALfCAAC2lrpUKjTWiBoBQyLHgQ',
			   'BQACAgQAAxkBAAIcSGAcsoiXSalsE7qQdAeoRa54lKARAALiCAAC2lrpUCG_81OJpY7MHgQ',
			   'BQACAgQAAxkBAAIcSWAcsogCFfp1dUWKogZAWrZFQZptAAL4CgACIxfpUCXQSsULrLgpHgQ',
			   'BQACAgQAAxkBAAIcSmAcsojiCHIT5GiIRsj-tqQ1HpY9AALkCAAC2lrpULS8NjXBhrS1HgQ',
			   'Krack 2021 Telugu HDRip'
	],
	
	'rangde' : ['BQACAgQAAxkBAAI0dmBq0F5AwEMRifIEygiEe8gR2puZAAKLCQACP7TwUufxCYSqDGE9HgQ',
			    'BQACAgQAAxkBAAI0d2Bq0F7Hy7hWVHgsnyZcTv9Ul-0mAAJ9CQACP7TwUkIN7GTFOB0QHgQ',
		 	   'BQACAgQAAxkBAAI0eGBq0F5ldoGhavnbvP_ZtAo09cvbAAJ-CQACP7TwUtnjMIiXCSWeHgQ',
	 		   'BQACAgQAAxkBAAI0eWBq0F5DiWD-oawSj69Cbu0C1kSMAAJ8CQACP7TwUrx4OyRF2M1iHgQ',
		 	   'BQACAgQAAxkBAAI0emBq0F67iawXa_JgaLs1GR1W7eZ_AAJ5CQACP7TwUvhycAlvq7nOHgQ',
			    'Rang De! 2021 Telugu DVDRip'
	],
	
	'sbsb'  : ['BQACAgQAAxkBAAITkmAXowag3DFChGScDlUrDMAruaBwAAIkDgACVGV5UzeMNg6c6SGsHgQ',
			   'BQACAgQAAxkBAAITk2AXowZr4u3JuBr4Y38giMSHhuojAAImDgACVGV5U8iwDfhrflEaHgQ',
			   'BQACAgQAAxkBAAITlGAXowavfPmqPZQ-jX55pMuxZFV-AAIqCQACUwR5U9UHPvg638ETHgQ',
			   '0',
			   'BQACAgQAAxkBAAITlWAXowa4ZwrB3xeh4NxhXiwm-2YlAAIoCQACUwR5U2cb738s_CchHgQ',
			   'Solo Brathuke So Better 2021 Telugu HDRip'
	],
	
	'red'   : ['BQACAgQAAxkBAAInSmA0WaEf-aUhjX8sOeRWGSiUght0AAK4DAACJIKhUSzlue2PralHHgQ',
			   'BQACAgQAAxkBAAInS2A0WaFHAAE5u4QEKWZOgofcn3zoUQACvgwAAiSCoVEwmFPP7EcmsR4E',
			   'BQACAgQAAxkBAAInTGA0WaFfHNFfo54sel8dav_WHQvcAAK9DAACJIKhUT5qJgnpXPpLHgQ',
			   'BQACAgQAAxkBAAInfGA1FW3UhzUwBtyswHPNA-OwjVoCAALUCQAC9yepUR9-TP28S7uGHgQ',
			   'BQACAgQAAxkBAAInfWA1FW183NyVOx4BxOy_-ztCh7MRAAL4CAAC9yexUVGj4XV47RTMHgQ',
			   'Red 2021 Telugu HDRip'
	],
	
	'bangarubullodu':
			 ['BQACAgQAAxkBAAITomAXpLowzAFlJ4YvacQQT7-MbZ6pAAI7CQAC__loUBqj-KL-I606HgQ',
			  'BQACAgQAAxkBAAITo2AXpLrWago_dZsCy_s_ZaW040UYAAI9CQAC__loUKzSx9YbYatgHgQ',
			  'BQACAgQAAxkBAAITpGAXpLorHQQDaqR_MxCJyMbnYUW2AAJOCQAC__loUFV0v_cOj9fFHgQ',
			  'BQACAgQAAxkBAAITpWAXpLrNzYe0pl7fxtkYmS9j17-iAAJJCQAC__loULVGiz0EQMrzHgQ',
			  'BQACAgQAAxkBAAITpmAXpLpHs3UAAboywqdV5SGYNb9KpAACSwkAAv_5aFDNRkQvAdSxbx4E',
			  'Bangaru Bullodu 2021 Telugu DVDRip'		  
	],
	
	'alluduadhurs'  :
			 ['BQACAgQAAxkBAAIksWAnrv0_yWZLvxI8pOsRh2s3f90LAALQCQACUI85URIVr6qAWYoGHgQ',
			  'BQACAgQAAxkBAAIksmAnrv0hsBON2lQeDK9btb4oybw-AALNCQACUI85UbHtgxYG24DoHgQ',
			  'BQACAgQAAxkBAAIks2Anrv1YX8TmqMp8J6yVL-J92snxAAIZDQACEIs5UcqWeiTZ0OWJHgQ',
			  'BQACAgQAAxkBAAITrWAXqENLx6PkfYRESDAuCNuTkyk0AAIbCQACocAIUFUYcmX-q9zUHgQ',
			  'BQACAgQAAxkBAAIk32AnsWmBzlKrEALHxTFrtjl7uBgxAALnDQACEIs5UYKOcQzoDXA5HgQ',
			  'Alludu Adhurs 2021 Telugu HDRip'
	],
	
	'aranya': ['BQACAgQAAxkBAAI0lGBq0x6SyHY42h83xGrYKsge3h6rAAK8CgACXArxUhHAHekpwLDpHgQ',
			   'BQACAgQAAxkBAAI0lWBq0x7s3vVMnA9Wu8NLMfkbLf3jAAKrCgACXArxUh5FcfNRkyjMHgQ',
			   'BQACAgQAAxkBAAI0lmBq0x4Q0W-MJQacm0xGYd0T_Lt7AAKyCgACXArxUuk6ud5eISBNHgQ',
			   'BQACAgQAAxkBAAI0l2Bq0x4jTGBN08poNit9KevEgTffAAKxCgACXArxUrFYmvVK9UxhHgQ',
			   'BQACAgQAAxkBAAI0mGBq0x7YxuPJny7c4h8TYSwFlv7wAAK1CgACXArxUrC6qmdKrRNaHgQ',
			   'Aranya 2021 Telugu DVDRip'
	],
	
	'30rpe': ['BQACAgQAAxkBAAIVD2AX7FRuA_B46rmyWkWw_wJxhn5gAAJhCAACZvywUKm6huERWtjkHgQ',
			  'BQACAgQAAxkBAAIVEGAX7FSVyBx5moNkF_W08EFXgl0-AAJcCAACZvywUESZKaDDz8uqHgQ',
			  'BQACAgQAAxkBAAIVEWAX7FTMlaWdlXGXKmkH-D1RhdxpAAJzCAACZvywUMro9YkFRAXdHgQ',
			  'BQACAgQAAxkBAAIVEmAX7FQhSee1Qr48_Tpal3NhI1iIAAJvCAACZvywUPP5pSo2rJ_hHgQ',
			  'BQACAgQAAxkBAAIVE2AX7FSNQdeFX6iKh-W6usazQTnvAAJiCAACZvywUDrRXWenZJrKHgQ',
			  '30 Rojullo Preminchadam Ela 2021 Telugu DVDRip'
	],
	
	'check': ['BAACAgQAAxkBAAIpU2A9AboouCMnJkbsyHNubQYrp75MAAIiEgACOwrJUfKYz0SsIEnSHgQ',
			  'BAACAgQAAxkBAAIpVGA9Abr6sWKNHgABncmjhqIoZeDKnAACBBIAAjsKyVH8sVQWSYMeSB4E',
			  'BAACAgQAAxkBAAIpVWA9Abo5shSmgRUQiqauI2EYIGwBAAIBCAACqYLIUVKJKydcRbJdHgQ',
			  'BAACAgQAAxkBAAIpVmA9AboGjuIf-P80ULwleRsJdqHxAALsCAACpGPIUWCf0b7tc4n6HgQ',
			  'BAACAgQAAxkBAAIpV2A9AbqIPUa_LfvbamUD77VfsFJwAAJ_CgACD1TAUV-d6p5nQGJ2HgQ',
			  'Check 2021 Telugu DVDRip',
			  'video'
	],
	
	'jr'	 :['BQACAgQAAxkBAAIqEmBPGxr5YQ8q5pfq_w2YnWf1lZfuAAImCgACsddRUlfywgnbVqPwHgQ',
			   'BQACAgQAAxkBAAIqE2BPGxqf6p8hwAQXtfr1UrT3epJFAAKADAAC_8dRUvZf4bQ7u0kxHgQ',
			   'BQACAgQAAxkBAAIqFGBPGxq9Q99uoAMOT8hzPirNWuiPAAIoCgACsddRUh6ecEfBd5dOHgQ',
			   '0',
			   'BQACAgQAAxkBAAIqFWBPGxpO9Zkh5pTDaLzcYv9M4h7eAAJyBgAC6Z9QUu2fGyyKxoY7HgQ',
			   'Jaathiratnalu 2021 Telugu PreDVD'
	],
	
	'sreekaram':
			  ['BQACAgEAAxkBAAIqOmBPHuZRkRLKnn6cYYQh40M-xMn8AAK_AQAC6ZJYRqJDbjwYvGaXHgQ',
			   'BQACAgQAAxkBAAIqO2BPHuZ_FLNZJNMFi0ZlZ5rt9Zj9AALKCgACiBZZUgPgUbzSFniaHgQ',
			   'BQACAgQAAxkBAAIqPGBPHuaTcQZjF9Fao0_x43EQy_-DAALXDAACxxtZUnd-lhM_z5JaHgQ',
			   '0',
			   'BQACAgQAAxkBAAIqPWBPHuY_8nkO4V_CCe0kPww2KKAvAALWDAACxxtZUiyQJlzDCpMmHgQ',
			   'Sreekaram 2021 Telugu PreDVD'
	
	],
	
	'uppena' :['BQACAgEAAxkBAAIj52AnfMgq1jaPq5SRqfHKlCI4cpFOAAKqAQACIcc4RQ7X4MqBd53SHgQ',
			   'BQACAgQAAxkBAAIj6GAnfMi0-itBPItHAAHCZchzo-W9YwADCwACUI85USUeb68UQoDmHgQ',
			   'BQACAgQAAxkBAAIj6WAnfMjcYYnXBah9eBR2IlHPHiYlAAJSDQACNOg5UcpfJsS6VYURHgQ',
			   '0',
			   'BQACAgQAAxkBAAIj6mAnfMgkQ-_qmq22u7pANqUdmBoPAAJTDQACNOg5UTrjRIlwNMjyHgQ',
			   'Uppena 2021 Telugu PreDVD'
	],
	
	'pogaru' :['BQACAgQAAxkBAAInvGA3CAN7Fh8Y7FX109GDNbiFF6YlAALiCAAC6HeIURbnC6otHIoGHgQ',
			   'BQACAgQAAxkBAAInvWA3CAMhgsCmONRP45Zep0UJn72kAAI7CQAC6HeIUfiTapnSeY8kHgQ',
			   'BQACAgQAAxkBAAInvmA3CAN7B4V4VZ7ZPsX1ux9tqzguAAI-CQAC6HeIUSNxzhesX57QHgQ',
			   '0',
			   'BQACAgQAAxkBAAInv2A3CAN53n0Qud5K1WF78YWycJ5TAAJGCQAC6HeIUcPP058L2n-gHgQ',
			   'Pogaru 2021 Telugu PreDVD'
	],
	
	'naandhi':['BQACAgQAAxkBAAInzmA3CasmbnOWbW_lyc5tT1ocezphAALRCgACqR6QUYIQvejJmtMLHgQ',
			   'BQACAgQAAxkBAAInz2A3CauZoH8I6TDMTYizB97yDkPsAALSCgACqR6QUWdjbk_oJhTzHgQ',
			   'BQACAgQAAxkBAAIn0GA3Cavo-ixBrYtVip5GuvRuXHSVAALTCgACqR6QUR1KCUBdQAABth4E',
			   'BQACAgQAAxkBAAIn0WA3CauAQTQSktU38XRHdWwNTS77AALICAACsjCQUbWBy5U7BfyDHgQ',
			   'BQACAgQAAxkBAAIn0mA3CauLTvYAAacwh3750K4YixmaIgAC1AoAAqkekFErT5ttj2wkxB4E',
			   'Naandhi 2021 Telugu PreDVD'
	],

}

def moviecheck(a):
	if a=="m1":
		b="master"
	elif a=="m2":
		b="krack"
	elif a=="m3":
		b="rangde"
	elif a=="m4":
		b="sbsb"
	elif a=="m5":
		b="red"
	elif a=="m6":
		b="bangarubullodu"
	elif a=="m7":
		b="alluduadhurs"
	elif a=="m8":
		b="aranya"
	elif a=="m9":
		b="30rpe"
	elif a=="m10":
		b="check"
	elif a=="m11":
		b="jr"
	elif a=="m12":
		b="sreekaram"
	elif a=="m13":
		b="uppena"
	elif a=="m14":
		b="pogaru"
	elif a=="m15":
		b="naandhi"
	else:
		b=""
	return b

def sizecheck(a):
	if a=="s1":
		b=0
	elif a=="s2":
		b=1
	elif a=="s3":
		b=2
	elif a=="s4":
		b=3
	elif a=="s5":
		b=4
	elif a=="s0":
		b="a"
	else:
		b=5
	return b

def msize(a):
	if a==0:
		b="200MB 220p"
	elif a==1:
		b="400MB 360p"
	elif a==2:
		b="700MB 480p"
	elif a==3:
		b="900MB 720p"
	elif a==4:
		b="1.4GB 1080p FHD"
	else:
		b="Unknown"
	return b

key = {
		  "inline_keyboard": [
						[
							{"text": "Master", "callback_data": "m1"},
						],
						[
							{"text": "Krack", "callback_data": "m2"},
						],
						[
							{"text": "Rang De!", "callback_data": "m3"},
						],
						[
							{"text": "Solo Brathuke So Better", "callback_data": "m4"},
						],
						[
							{"text": "Red", "callback_data": "m5"},
						],
						[
							{"text": "Bangaru Bullodu", "callback_data": "m6"},
						],
						[
							{"text": "Alludu Adhurs", "callback_data": "m7"},
						],
						[
							{"text": "Aranya", "callback_data": "m8"},
						],
						[
							{"text": "30 Rojullo Preminchadam Ela", "callback_data": "m9"},
						],
						[
							{"text": "Check", "callback_data": "m10"}
						],
						[
							{"text": "Jaathiratnalu", "callback_data": "m11"},
						],
						[
							{"text": "Sreekaram", "callback_data": "m12"},
						],
						[
							{"text": "Uppena", "callback_data": "m13"},
						],
						[
							{"text": "Pogaru", "callback_data": "m14"},
						],
						[
							{"text": "Naandhi", "callback_data": "m15"},
						],
						[
							{"text": "❌ Cancel ❌", "callback_data": "clear"},
						],
					]
	  }

key1 = types.InlineKeyboardMarkup(row_width=3)
a = types.InlineKeyboardButton(text="Master", callback_data="m1")
b = types.InlineKeyboardButton(text="Krack", callback_data="m2")
c = types.InlineKeyboardButton(text="Rang De!", callback_data="m3")
d = types.InlineKeyboardButton(text="Solo Brathuke So Better", callback_data="m4")
e = types.InlineKeyboardButton(text="Red", callback_data="m5")
f = types.InlineKeyboardButton(text="Bangaru Bullodu", callback_data="m6")
g = types.InlineKeyboardButton(text="Alludu Adhurs", callback_data="m7")
h = types.InlineKeyboardButton(text="Aranya", callback_data="m8")
i = types.InlineKeyboardButton(text="30 Rojullo Preminchadam Ela", callback_data="m9")
j = types.InlineKeyboardButton(text="Check", callback_data="m10")
k = types.InlineKeyboardButton(text="Jathiratnalu", callback_data="m11")
l = types.InlineKeyboardButton(text="Sreekaram", callback_data="m12")
m = types.InlineKeyboardButton(text="Uppena", callback_data="m13")
n = types.InlineKeyboardButton(text="Pogaru", callback_data="m14")
o = types.InlineKeyboardButton(text="Naandhi", callback_data="m15")
p = types.InlineKeyboardButton(text="❌ Cancel ❌", callback_data="clear")

key1.add(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p)

	
def sizekeyedit(a):
	  
	sizekey = {
		  "inline_keyboard": [
						[
							{"text": "All Qualities", "callback_data": a+" s0"},
						],
						[
							{"text": "220p", "callback_data": a+" s1"},
						
						
							{"text": "360p", "callback_data": a+" s2"},
						],
						[
							{"text": "480p", "callback_data": a+" s3"},
						
						
							{"text": "720p MHD", "callback_data": a+" s4"},
						],
						[
							{"text": "1080p FHD", "callback_data": a+" s5"},
						
						
							{"text": "<< Go Back", "callback_data": "m0"},
						],
						[
							{"text": "❌ Cancel ❌", "callback_data": "clear"},
						],
					]
	  }
	return sizekey
