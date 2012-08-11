''' 
Michael Allen C. Isaac <michael@thedevel.com>

Hire me.

This challenge was marked as easy, but I'm a newb so I tried all kinds of things that didnt work,
This is what I came up with after about an hour :/

Do I get extra credit for OO design?

http://www.reddit.com/r/dailyprogrammer/comments/xxbbo/882012_challenge_86_easy_runlength_encoding/

Licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
http://creativecommons.org/licenses/by-nc-sa/3.0/
'''

import sys
import pprint

class RunCompactor():
    runString = ''
    
    def __init__( self ):
        self.runString = ' '.join(sys.argv[1:])
        
        if(len(sys.argv) == 1):
            print('class Main() -> Initalized with to few arguments')
            sys.exit(0)
            
        return
       
    def getRunString( self ):
        return self.runString
    
    def deflateRun( self, data ):
        #for iterate the data
        
        iter = 0
        char = None
        charcnt = 0
        result = []
        
        while(True):
            if(data[iter] == char):
                charcnt += 1
            else:
                result.append( [char, charcnt] )
                char = data[iter]
                charcnt = 1
            
            iter += 1
            
            if(iter >= len(data)):
                result.append( [char, charcnt] )
                break
        
        #we trim the first element from the array, its always [None, 0]
        return result[1:]


app = RunCompactor()
print(pprint.PrettyPrinter(indent = 4).pformat( app.deflateRun(app.getRunString()) ))


