import tweetstream
import json
import os
import types

print "start"

filecounter = 8
filename = "test_stream"+str(filecounter)+".csv"
output = open(filename, "a")

#new york city
nyc = ["-74.5,40.5","-73.2,41.3"]

words = ['dexter','bond']

#stream = tweetstream.SampleStream("601city", "chliklas")
stream = tweetstream.FilterStream("601city", "chliklas", locations = nyc)

counter = 878817

for tweet in stream:
    
    if tweet.get("delete"):
        print "delete"
        continue
    else:
        print counter
    
    # ----- write tweet infos ----- #
    
    # -- write count
    output.write(str(counter)+", ")
    
    # -- write status id
    output.write(str(tweet.get("id"))+", ")
    
    # -- write created at
    output.write(str(tweet.get("created_at"))+", ")
    
    # -- write lat long coordinates
    if tweet.get("geo"):
        geo = tweet.get("geo");
        coordinates = geo.get("coordinates")
        output.write(str(coordinates[0])+", ")
        output.write(str(coordinates[1])+", ")
    else:
        output.write(", , ")

    # -- write in reply to status id
    output.write(str(tweet.get("in_reply_to_status_id"))+", ")

    
    # -- write in reply to user id
    output.write(str(tweet.get("in_reply_to_user_id"))+", ")
    
    # -- write text
    if(tweet.get("text")):    
        text = tweet.get("text").encode('utf8')
        text = text.replace(",","")
        text = text.replace("\n","")
        output.write(text+", ")
    else:
        output.write(",")
    
    
    # ----- write user infos ----- #
    
    user_infos = tweet.get("user")
    
    # -- write user id
    output.write(str(user_infos.get("id"))+", ")
    
    # -- write user name
    name = user_infos.get("name").encode('utf8')
    name = name.replace(",","")
    name = name.replace("\n","")
    output.write(name+", ")
    
    # -- write user screen name
    screenname = user_infos.get("screen_name").encode('utf8')
    screenname = screenname.replace(",","")
    screenname = screenname.replace("\n","")
    output.write(screenname+", ")
    
    # -- write user created_at
    output.write(str(user_infos.get("created_at"))+", ")

    # -- write user favorites_count
    output.write(str(user_infos.get("favorites_count"))+", ")
    
    # -- write user friends_count
    output.write(str(user_infos.get("friends_count"))+", ")
    
    # -- write user statuse_count
    output.write(str(user_infos.get("statuses_count"))+", ")
    
    # -- write user url
    if(user_infos.get("url")):
        url = user_infos.get("url").encode('utf8')
        url = url.replace(",","")
        url = url.replace("\n","")
        output.write(url+", ")
    else:
        output.write(",")
    
    # -- write user profile_background_image_url
    if(user_infos.get("profile_background_image_url")):
        bg_image_url = user_infos.get("profile_background_image_url").encode('utf8')
        bg_image_url = bg_image_url.replace(",","")
        bg_image_url = bg_image_url.replace("\n","")
        output.write(bg_image_url+",")
    else:
        output.write(",")
    
    output.write("\n")

    counter += 1;
  
    if counter % 100000 == 0:
        output.close()
        filecounter = filecounter + 1
        filename = "test_stream"+str(filecounter)+".csv"
        output = open(filename, "a")
    

    

print "end"