# -*- coding: utf-8 -*-
"""

Read hygiene data from XML to CSV

"""

import xml.etree.ElementTree as ET
import csv
import requests

def readDataFromWeb():
    r = requests.get('http://ratings.food.gov.uk/OpenDataFiles/FHRS520en-GB.xml')
    with open('southKen.xml', 'w') as f:
        f.write(r.text)



def hygieneDataToCSV():
    # Use element tree library to parse XML data
    tree = ET.parse("southKen.xml")
    root = tree.getroot()
    
    # We want specific data from the XML file    
    headers = ['BusinessName','FHRSID','BusinessType','RatingDate','RatingValue','AddressLine1',
                     'AddressLine2','AddressLine3','Hygiene','Structural','ConfidenceInManagement','Longitude','Latitude']  
    simpleHeaders = ['BusinessName','FHRSID','BusinessType','RatingDate','RatingValue','AddressLine1',
                     'AddressLine2','AddressLine3']                    
    scoreHeaders = ['Hygiene','Structural','ConfidenceInManagement']
    geoHeaders = ['Longitude','Latitude']
    
    # CSV file to write in
    write_file = open('southKenHygiene.csv','w')
    output = csv.writer(write_file, delimiter=',', lineterminator='\n')
    output.writerow(headers)     
    
    # Loop through fields in XML, create a list, write the list as a new line in csv file
    for member in root.findall('EstablishmentCollection'):
        for mm in member.findall('EstablishmentDetail'):
            establishment = []
            
            for elem in simpleHeaders:            
                if mm.find(elem) != None:
                    establishment.append(mm.find(elem).text)
                else: establishment.append('')      

            for m in mm.findall('Scores'):
                for elem in scoreHeaders:
                    found = m.find(elem)
                    if found != None:
                        establishment.append(found.text)
                    else: establishment.append('')

            for m in mm.findall('Geocode'):
                for elem in geoHeaders:                
                    found = m.find(elem)
                    if found != None:
                        establishment.append(found.text)
                    else: establishment.append('')
            
            output.writerow(establishment)
    write_file.close()


# Run code 
readDataFromWeb()

hygieneDataToCSV()