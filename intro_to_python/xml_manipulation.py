#A program to manipulate XML file
"""
Created by @Hrishikesh Salunkhe
"""
import xml.dom.minidom
def main():
    print("hello")
    doc=xml.dom.minidom.parse('sample.xml')
    print(doc.nodeName)
    print(doc.firstChild.tagName)
if __name__ == "__main__":
    main()
