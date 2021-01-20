# A python program for  HTML Parser
"""
Created by @Hrishikesh Salunkhe
"""
from html.parser import HTMLParser
metacount=0
class myparser(HTMLParser):
    def handle_comment(self, data):
        print("Encountered comment:", data)
        pos=self.getpos()
        print("\tAt  line: ",pos[0],"Position",pos[1])
    def handle_starttag(self, tag, attrs):
        global metacount
        if tag == "meta":
            metacount +=1
        print("Encountered tag:", tag)
        pos = self.getpos()
        print("\tAt  line: ",pos[0],"Position",pos[1])
        
        if attrs.__len__() > 0:
            print("\t Attributes:")
            for a in attrs:
                print(a[0],"=",a[1])
            

    def handle_endtag(self, tag):
            print("Encountered tag:", tag)
            pos=self.getpos()
            print("\tAt  line: ",pos[0],"Position",pos[1])

    def handle_data(self, data):
        if(data.isspace):
            return 
        print("Encountered comment:", data)
        pos=self.getpos()
        print("\tAt  line: ",pos[0],"Position",pos[1])
        
        
def main():
    parser= myparser()
    f=open("sample.html")
    if f.mode == 'r':
        content=f.read()
        parser.feed(content)    

if __name__ == "__main__":
    main()