import xml.dom.minidom

def main():
    doc = xml.dom.minidom.parse("test.xml")
    data = doc.getElementsByTagName("data")
    for t in data[0].childNodes:
        print(t.nodeType)

main()