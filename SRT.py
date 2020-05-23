#
# Made by Seba7236
# Date: 23-05-2020
# 
#Feel free to change the test.srt to any other filename, just keep the .SRT extension
#same goes for script.txt, call it whatever you like
#reads text from file
with open('script.txt') as f:
    text = f.readlines() #reads line by line of .txt file
text = [x.strip() for x in text] #strips text of whitespace

f = open('test.srt','w+') # opens file to write to it


# Format for input = 00 00 00 000 ( hours, minutes, seconds, milliseconds)

for i in range(len(text)):
    hour,minute,second,milli = input('Timestamp of start of line"%s" '%(text[i])).split() #takes start input
    start = hour+':'+minute+':'+second+','+milli 
    hour,minute,second,milli = input('Timestamp of end of line "%s" '%(text[i])).split(' ') #takes end input
    end = hour+':'+minute+':'+second+','+milli 

    f.write('%d\n'%(i+1)) #writes number to line 
    f.write('%s --> %s\n'%(start,end)) #followed by the timestamps
    f.write('%s\n\n'%(text[i])) #followed by the text
f.close() #closes the file

