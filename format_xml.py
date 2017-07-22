import xml.dom.minidom

doc = xml.dom.minidom.parse('test.hfp')
str_xml = doc.toprettyxml()

filexml = open('test.hfp', 'w')
filexml.write(str_xml)
filexml.close()
