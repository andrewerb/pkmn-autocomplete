# -*- coding: utf-8 -*-
"""
fetch.py

Aggregate list of Pokemon names (there are a lot of them) from PokeAPI, via the Requests library
"""
__author__ = "@_andrewerb"

import requests
import json
from time import sleep

#######
'''
    ping for name, if status code is good cool, else abort
    if cool, add to list with # then next
    save current string/pkmn name as var in loop, then output. last successful and current. with #s.
'''

'''
    try name up to val, or indef until error code. start val. 
    call from function
    write to file

    >## num at node, *dict node, *overlap words, *dump trie, list?, child words, count. more pythonic.
    print tree. char space queue + lines. string of mutual chars
    regexp + lower
'''
###########

## pkmn_names.txt ##as list or JSON or Dict?
    ## a to append
## last_num_read.txt
    ## w to overwrite as num. use to set #

############

# test for passive params for start and end
# print to file / CLI

def pkmn_query_string( pkmn_num ): #query_url ++ merge pkmn_url
    """Returns URL for API call, given a Pokemon #"""
    pokeapi_url = "http://pokeapi.co/api/v2/"
    pkmn_route_url = pokeapi_url + "pokemon/" + str(pkmn_num) + "/"
    #pkmn_route_string = pkmn_url + str(pkmn_num) + "/"

    return pkmn_route_url

    ###
    # enum if you need i, else for elem in iterable_list_or_set

#def error_log():
    #pass


############### FIX
def get_pkmn_list( start_num = 1, max_num = 151 ): #test pre-set
    """Returns list of pokemon names from api request loop
    
    TODO: ??
    * get function (here) 
    > loop type > inner block to get at i. append.
    """
    poke_list = list()
    print("Iterating...")

    
    ### if max num, use for, else while.
    #check fail

######
# for item in list
# print(s, end='', sep='')
# print(str(item), end=' ....  ', sep='.......')

    ### 251; goal to get dict or JSON. 
    # save ongoing to list if it breaks. save all to file. append?
    '''WHILE LOOP!!!'''
    for item in range(start_num,max_num+1): #change to while true, exit by status code or bad response
        ### break out code block to function
        ### While vs For variant!
        ##use status code to proceed or not?
        if (item % 5) == 0: #multiple of 5
            print( "Fetching:  " + str(item) + " -- a multiple of 5." ) 
            
        current_req = requests.get( pkmn_query_string(item) )
        
        
        if current_req.status_code != 200:
        #if current_req.json()["detail"] or current_req.status_code != 200:
            '''failure'''
            #break ##will cut loop without result
            print("Failed at No. " + str(item) )
            print("STATUS: " + str(current_req.status_code))
            return poke_list

        else:
            poke_name = str(current_req.json()["name"])
            poke_list.append( poke_name )

            if (item % 5) == 0: #multiple of 5
                print(poke_name)
        
        #check fail. report + return, else append, print if valid
        
        if item % 200 == 0:
            sleep(.25)
        elif item == max_num:
            print("Complete. Final count: "+ str(max_num))
        else:
            sleep(0.004)
        ###fail_out_to_file(x): _error_num_date_log.txt

    return poke_list #return list over dict and check count; num is irrelevant for now.
    ###trie enhancement: dump trie, check overlap, search num. UI. live type search


def main():
    print("Fetching PokeAPI data...")
    print( str( get_pkmn_list(1,5) ) ) #Should add I/O here. Default if nothing or whitespace.
    print("Done.")
    ## save to file
    ## use input?

    ### get list of names. write list to file. pick up as needed. cool-down in getter. bigger cooldown in between. prompt to continue maybe? alert in cmd.

if (__name__ == "__main__") :
    main()

##############
# add to JSON
'''
    # WRITE TO FILE - JSON.
    r = s.get("https://pokeapi.co/api/v2/pokemon/25/")
    f = open('pretty_25.json', 'w')
    import json
    f.write(json.dumps(r.json()))
    # 177804
    f = open('prettiest.json', 'w')
    f.write(json.dumps(r.json(),sort_keys=True, indent=4))
    # 365456

'''