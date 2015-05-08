import listen.listen as listener
import comp.comprehender as comprehender

def main():
    print ("  'cooperate.py' is running.")
    lsnr = listener.Listener(600)
    result = lsnr.listen()
    if result != None:
        print ("  writing output file...")
        cmprhdr = comprehender.Comprehender(result)
        words_dict = cmprhdr.comprehend()
        f = open("test_coop.txt", "w")
        f.write("All: " + ", ".join(words_dict['all']).encode("utf-8") + "\n")
        f.close()
        print ("  end.")
    else:
        print ("! no word recognized.")

# ---- Execute ----
if __name__ == "__main__":
    main()
