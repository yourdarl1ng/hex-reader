#main class where magic happens
class Main:
    #opening the file
    def __init__(self):
        #we will use these to decode the file
        self.lines = [] 
        self.bytes = 0
        #file path
        self.file = input("Select a file to open: ")
        #rb stands for read bytes
        with open(self.file, "rb") as f:
            #save the read data in a variable
            self.data = f.read()
            #close the file when we're done
            f.close()
    #magic comes in
    def run(self):
        
        for byte in self.data:
            
            self.bytes+=1
            self.lines.append(byte)
            #printing the byte, nice and clean
            print("{0:0{1}x}".format(byte, 2), end=" ")
            #at the end of the line(every 16 bytes) we add a decoded view
            if self.bytes % 16 == 0:
                #we separate the decoded view with this print
                print("#", end="")
                #the last 16 bytes we read are here
                for b in self.lines:
                    #we use the ascii table to determine if the byte is worth decoding or not
                    #32 - 126 is the alphabet and some symbols
                    if b >= 32 and b <= 126:
                        print(chr(b), end="")
                    #if the byte isn't worth decoding we print a star
                    else:
                        print("*", end="")
                #cleaning up, memory management is important
                self.lines.clear()
                #printing a new line
                print("")
        #printing the rest of the file
        print(" "*((3*(16-len(self.lines))-1)), "#", end="")
        for b in self.line:
            if b >= 32 and b <= 126:
                print(chr(b), end="")
            else:
                print("*", end="")

#Running this mess
Main().run()
