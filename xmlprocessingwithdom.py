import xml.dom.minidom

"""
Introduction:
This script demonstrates XML processing using the Document Object Model (DOM) in Python.
The DOM allows you to parse, modify, and create XML documents programmatically.
"""

# Parse the XML file
domtree = xml.dom.minidom.parse('data.xml')
group = domtree.documentElement

# Get all 'person' elements
persons = group.getElementsByTagName('person')

# Print information for each person
for person in persons:
    print("-----PERSON-----")
    if person.hasAttribute('id'):
        print("ID: {}".format(person.getAttribute('id')))
    
    # Print name and weight of each person
    print("Name: {}".format(person.getElementsByTagName('name')[0].childNodes[0].data))
    print("Weight: {}".format(person.getElementsByTagName('weight')[0].childNodes[0].data))

# Modify the XML content
# Update the name of the third person
persons[2].getElementsByTagName('name')[0].childNodes[0].nodeValue = "New Name"

# Update the ID of the first person
persons[0].setAttribute('id', '100')

# Write the changes to the XML file
domtree.writexml(open('data.xml', 'w'))

# Create a new person element
newperson = domtree.createElement('person')
newperson.setAttribute('id', '6')

# Create and append child elements to the new person
name = domtree.createElement('name')
name.appendChild(domtree.createTextNode('Paul Green'))

age = domtree.createElement('age')
age.appendChild(domtree.createTextNode('20'))

weight = domtree.createElement('weight')
weight.appendChild(domtree.createTextNode('70'))

height = domtree.createElement('height')
height.appendChild(domtree.createTextNode('180'))

# Append child elements to the new person element
newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

# Append the new person to the root element
group.appendChild(newperson)

# Write the updated XML to the file
domtree.writexml(open('data.xml', 'w'))
