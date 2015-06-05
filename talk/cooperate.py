import listen.listen as listener
import comp.comprehender as comprehender

#( main unit -> unit )
def main():
    print ("  'cooperate.py' is running.")
    lsnr = listener.Listener(600)
    result = lsnr.listen()

    if result == None:
        print ("! no word recognized.")
    else:
        print ("  writing output file...")
        cmprhdr = comprehender.Comprehender()
        words_dict = cmprhdr.comprehend(result)

#        f = open("test_coop.txt", "w")
#        f.write("All: " + ", ".join(words_dict['all']).encode("utf-8") + "\n")
#        f.close()
        print ("All: " + ", ".join(words_dict['all']).encode("utf-8") + "\n")
        print ("  end.")
    #end if
    return
#end def

# ---- Execute ----
if __name__ == "__main__":
    main()
#end if