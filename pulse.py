from analyze import analyze, trigger
import time

def clean(STRING):
    return (''.join([c for c in STRING if c.lower() in 'abcdefghijklmnopqrstuvwxyz ']))[:140]

#---needs to be tested!
def tidapiobj_to_html(tweetid, apiobject):
    return json.loads(apiobject.get_oembed(id=tweetid))['html']

#---removes tweets from the bottom of the queue
def remove_thread(queue):
    timer = time.time() * -1
    try:
	(t_time, tweet) = queue.get()
        while t_time - timer > 60*15:  #15 minute expiry
	    (t_time, tweet) = queue.get()
	queue.put((t_time,tweet))

    except Queue.Empty:
	return

    return

#---analyzes queue for news events
def analysis_thread(queue):
    #analyze current queue
    event = analyze(queue)
    if event:
	trigger(event)
    return

