# -*- coding: utf-8 -*-
# 
__author__ = "@_andrewerb"
"""
    Input handler
"""
from time import sleep
from trie import *

### base trie setup cli for testing
### better cli for autocomplete?
# break out of file?

class TriePrefixUI:
    #ui_Trie = None
    """
        A barebones user interface for searching Prefixes against the (already initialized) autosuggestion trie.

        ###############
        CLI user input for trie/autocomplete
        #
        Require trie, loop?, or break
    """
    ## loop here. break from program on exit. else loop in main.
    #give prompt.
    #get input.
    #check is string, else num?? else other / error.
    # use trie. get response.
    def __init__(self, search_trie=None):
        self.session_trie = search_trie

        """
        if type(search_trie) is Trie():
            self.session_trie = search_trie
        else:
            self.session_trie is None
        """
        #pass
        #defalt trie = None. needs setting.

    def set_trie(self, search_trie=None):
        self.session_trie = search_trie

    def ui_loop(self):
        #if no trie, return
        while (True):
            print(
                "Type a search term and hit Enter for matching suggestions")
                #\nType \'exit\' or \'quit\' to end the program.
            raw_input = input(">  ")
            ### if ! empty or none, do check. else, prompt text qualifier.
            
            ##print( raw_input + " is the input" )
            ##print( self.__format_input(raw_input) + " is the working input." )
            
            self.__input_handler( self.__format_input(raw_input) )
        
            sleep(.25)

    def __format_input(self, input_str=str("")):
        """
            Returns a string, lowercase and sans whitespace.
        """
        return ( input_str.lower() ).replace(" ", "")
        # numbers are not supported.
        #strip spaces, special chars, regexp, check for #s

    def __input_handler(self, input_str=str("")):
        """
            ;
        """
        #check for trie set. break or exit otherwise.
        #empty or none, nums in check, spaces stripped. cast as string.to lower.
        print("INPUT: "+input_str)
        if input_str == ("exit" or "quit"):
            print("\nGoodbye!\n")
            exit()
        #if input_str == !alpha/special char || num
        else:
            if type(self.session_trie) is type( Trie() ):
                # print("Trie is ready!")
                # retrieve TRIE MATCHes
                # print("Trie is good!") #####
                #  print("X matches for your prefix "+input_str)
                #print(str(pkmn_trie.get_prefix_matches(input_str)))
                
                ##print(str(self.session_trie.get_prefix_matches(input_str)))
                
                for elem in self.session_trie.get_prefix_matches(input_str):
                    print(str(elem))
            else:
                print("Error: Trie is not yet set up.")
                exit()

    #def __print_input_matches(self, input_str)

###################
def main():
    #print("CLI UI running")
    print("Pokémon Search \'Auto\'-Suggestion")
    ui_session = TriePrefixUI()
    ui_session.ui_loop()
    
    # init trie in function that returns trie? 
    # set UI and start loop. break on quit. exit.
    #pass

if __name__ == "__main__":
    main()

def program_notes():
    pass
    ## in main.py...
    # init trie (list and loop)
    # init UI w trie
    # call UI loop
    ######
    # init trie from function with strings at top and loop. return trie.
    ######
    ## Qs: more pythonic?
    ## dict based node, add to trie, overlaps, init from list etc and types handling
    ## dump trie! (trie method, prints tree-ish thing)
    ## lowercase + regexp. walk through what overall program does, then trie, then methods. parts are trie, handler, node, init

