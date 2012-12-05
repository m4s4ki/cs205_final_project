import operator


def forme_data():
    #open files
    input_file = open("test_stream0.csv","r")
    output_file = open("formed_test.csv", "w")
    
    #read lines
    for line in input_file:
        
        #split text
        parts = line.split(",")
        text = parts[7]
        
        #look for hashtags
        hash_count = text.count('#')
        hash_index = text.find("#")

        #write text
        if hash_count > 0:
            output_file.write(text.lower() + "," + str(hash_count))
        
        #write hashtags
        for occurency in range(hash_count):
            hash_end_index = text.find(" ", hash_index) + 1
            if hash_end_index:
                hash_text = text[hash_index:hash_end_index]
            else:
                hash_text = text[hash_index:]
            hash_text = hash_text.strip()
            output_file.write(","+hash_text.lower())
            hash_index = text.find("#", hash_end_index - 1)
            
        #close line
        if hash_count > 0:
            output_file.write(",\n")
            
    #close files
    input_file.close()
    output_file.close()
    


def create_hash_tag_list():
    
    #open files
    input_file = open("formed_test.csv","r")
    output_file = open("test_hashtag_list.csv", "w")
    
    hash_dict = dict()
    
    for line in input_file:
        
        parts = line.split(",")
        for hash_index in range(2, len(parts)-1):
            
            print parts[hash_index]
            
            if parts[hash_index] in hash_dict:
                current_count = hash_dict[parts[hash_index]]
                hash_dict[parts[hash_index]] = current_count + 1
                
            else:
                hash_dict[parts[hash_index]] = 1   

        
    sorted_hash_dict = sorted(hash_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
    
    
    for t in sorted_hash_dict:
        print t[0], t[1]
        output_file.write(str(t[0]) + ", " + str(t[1]) + "\n")
            
    #close files
    input_file.close()
    output_file.close()
    
    
def create_order_data():
    # open input files
    input_file = open("formed_test.csv","r")
    output_file = open("test_rate.csv", "w")
    
    # store tweets in dicts
    hash_dict = dict()
    hash_dict2 = dict()
    for line in input_file:
        parts = line.split(",")
        for hash_index in range(2, len(parts)-1):
            if parts[hash_index] in hash_dict:
                hash_dict[parts[hash_index]].append(parts[0])
            else:
                hash_dict[parts[hash_index]] = [parts[0]]
                
            if parts[hash_index] in hash_dict2:
                current_count = hash_dict2[parts[hash_index]]
                hash_dict2[parts[hash_index]] = current_count + 1
            else:
                hash_dict2[parts[hash_index]] = 1
                
           
    sorted_hash_dict = sorted(hash_dict2.iteritems(), key=operator.itemgetter(1), reverse=True)
    # write to files    
    for t in sorted_hash_dict:
        output_file.write(t[0])
        for tx in hash_dict[t[0]]:
            output_file.write(", +++++ "+tx)
        
        output_file.write("\n")
            
        
    # close files
    input_file.close()
    output_file.close()
    
def create_training_data():
    

    # define tags
    good_tags = ['#art', '#love', '#lol', '#foodporn', '#beautiful', '#treeligthing', '#holiday',
                 '#xmas', '#holydays', '#food', '#family', '#friends', '#fun', '#iloveyou', '#sexy',
                 '#lights', '#party', '#yolo', '#bestfriend', '#winning', '#yum', '#amazing', '#thankyou',
                 '#beauty', '#funny', '#cute', '#soexcited', '#bestfriend']
    bad_tags = ['#tred', '#work', '#bored', '#ugh', '#gay', '#wtf', '#sorrynotsorry', '#damn', '#dead',
                '#creepytweet', '#collegeproblems', '#sad', '#jealous', '#stfu', '#smh', '#lmao', '#fuckthis', '#loser',
                '#thoughtsduringschool', '#fml']
    
    neutral_tags = ['#nyc', '#tweetmyjobs', '#oomf', '#internship','#marketing', '#socialmedia','#hr']

    
    '''
    good_tags = ['#love']
    bad_tags = ['#sad', '#fuckthis', '#loser']
    
    neutral_tags = [ '#internship','#marketing', '#socialmedia']
    '''
    
    
    # open files
    input_file = open("formed_test.csv","r")
    output_file = open("test_training.txt", "w")
    output_target_file = open("test_target.txt","w")
    

    
    for line in input_file:
        # strip # from the text
        text = line[0]
        happiness = -1
        parts = line.split(",")
        text = parts[0]
        
        # removing \n
        text = text.replace("\n","")
        text = text.replace("'","")
        text = text.replace('"',"")
        text = text.replace(",","")
        text = text.replace(".","")
        text = text.replace(";","")
        text = text.replace(":","")
        text = text.replace("/","")
        text = text.replace("-","")

        
        
        
        # removing screen names
        number_of_screen_names = text.count("@")
        for name in range(number_of_screen_names):
            name_start = text.find("@")
            name_end = text.find(" ", name_start)
            
            if name_end:
                screen_name = text[name_start:name_end]
            else:
                screen_name = text[name_start:]
            text = text.replace(screen_name, "")
            
        text = text.replace("#", "")
        
        # removing hashtags
        for hash_index in range(2, len(parts)):
            #text = text.replace(parts[hash_index], "")

            if happiness == -1:
                if parts[hash_index] in good_tags:
                    print "happy"
                    happiness = 2
                if parts[hash_index] in bad_tags:
                    happiness = 1
                if parts[hash_index] in neutral_tags:
                    happiness = 0

        if happiness == -1:
            continue

        try:
            decoded = text.decode("utf8")
        except:
            continue
        
        print text
            
        output_file.write(text + "\n")
        output_target_file.write(str(happiness) + "\n")
    
    
    # close files
    input_file.close()
    output_file.close()
    output_target_file.close()
        

    
    
if __name__ == '__main__':
    #forme_data()
    #create_hash_tag_list()
    #create_order_data()
    create_training_data()
   