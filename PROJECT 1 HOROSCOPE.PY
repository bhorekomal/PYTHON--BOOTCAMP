Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # An application which tells future based on zodiac
>>>next = True
>>>while next == True:
>>> print('''
1)Aries
2)Tauras
3)Gemini
4)Cancer
5)Leo
6)Virgo
7)Libra
8)Scorpio
9)Sagittarius
10)capricorn
11)Aquarius
12)Pisces
''')

1)Aries
2)Tauras
3)Gemini
4)Cancer
5)Leo
6)Virgo
7)Libra
8)Scorpio
9)Sagittarius
10)capricorn
11)Aquarius
12)Pisces

>>> s = int(input("pick your zodiac sign number and press enter"))
pick your zodiac sign number and press enter7
>>> print(s)
7
>>> print(int(s))
7
>>> 
>>> 
>>> if s==1:
	print("Today, you may wake up with your nose in the air. Though you may feel bossy and important, others may not feel that way about you. Avoid giving orders that sound like insults. Otherwise, the whole thing may fall flat on your face, says Ganesha.")
elif s==2:
	print("Getting through today will be like a cruise, says Ganesha. Business deals will kneel to the charm of your honey tongue and you will taste success. As the day progresses, you may lose interest in things. Beware of being too sentimental in the evening, warns Ganesha. You will feel loved and generous in social gatherings tonight.")
elif s==3:
	print("A marathon brainstorming session with your colleagues, a scamper for meeting deadlines, and a demanding spouse will leave you quite stressed out by the end of the day. You, however, are an expert in dividing time between business, home and pleasure. The answer to your prayers is a late-night party, at least that's what you think.")
elif s==4:
	print("This is your big moment. You are going to deal with a huge amount of money — the kind of amount you would want to fill your swimming pool with and swim in it. Statutory warning issued by Ganesha: Don't dive in it, for you may hurt yourself as something or someone is likely to pull the plug, draining out most of the wealth that was amassed overnight. However, you will regain some of that lost money by the end of the day.")
elif s==5:
	print("Since when was a day complete without a little bit of a scruff and a small squabble? These are the annoying little situations that remind you just how better the alternative is. Ganesha portends a day in which you are jinxed with a propensity for quarrels. So, it is advisable to shun any open confrontation at work. Be good during the day because Ganesha foresees a particularly enjoyable evening in store for you.")
elif s==6:
	print("It is quite probable that today will be an action-packed day for you, feels Ganesha. It is going to be a progressive day for your business. Later in the day, you may retreat into your shell, and refuse company.")
elif s==7:
	print("It's now or never for you, as today, you may finally take out time to do some sound thinking for your future goals and success. Things seem to go your way, and all your plans are beautifully executed towards the afternoon. Also, find time in the evening to be with the ones dear to you. A movie and dinner sounds like a good idea to Ganesha. Enjoy life in all its goodness!")
elif s==8:
	print("Armed with a good sense of judgement, you will make a number of encouraging changes in your behaviour today, foretells Ganesha. Habits die hard, but all the effort that you put in to refine your routine will pay off brilliantly by the end of the day. Close friends and family will be pleasantly surprised by your efficiency and decisions.")
elif s==9:
	print("Expect to be on the go for business related work. Money matters will be a pressing issue in the afternoon. Be the team player and catch all that comes your co-workers' way. Expect to relax and end the day on a cheerful, romantic note.")
elif s==10:
	print("In all probability, you will be in a bizarre frame of mind. At work, there will be a sudden turn of events that shall suddenly create a tottering pile of tasks on your table. In financial matters, you are likely to remain very cautious. In the evening, you can relax and enjoy yourself with your sweetheart, suggests Ganesha.")
elif s==11:
	print("You are fully charged and raring to go! Your friends are supportive of your new schemes, and your bosses are pushing you to complete pending projects. This shouldn't be a problem, considering your current levels of energy and enthusiasm, says Ganesha.")
elif s==12:
	print("You will need to be as scheming as the proverbial fox if you hope to wriggle out of the tricky situations that you are likely to find yourself embroiled in today. Keep your temper in check if things don't go your way initially, for the answers to your troubles will come sooner rather than later, says Ganesha.")
else:
	print("Hey,are you sure about the number?")
next = True if input("\n shall we do it again?(Y/N)")=='Y' else false
 
