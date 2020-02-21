'''
Created on 21.06.2012

@author: meyert
'''
import xml.etree.ElementTree as ET
from PySide import QtCore
from PySide.QtCore import QThread
import os, shutil,sys, re 
      
class Tools(object):

    def XML_LoadElemAttribs(self, fp, tag):   
        dic = {}  
        
        if os.path.exists(fp):
            tree = ET.parse(fp)
            elems = tree.findall(tag)
            if elems <> []:
                elem = elems[0]
                dic = elem.attrib
        else:
            print 'can not find file:', fp

        return dic
    
    def XML_SaveElemAttribs(self, fp, tag, dic):  

        if os.path.exists(fp):
            tree = ET.parse(fp)
            root = tree.getroot()        
        else:
            root = ET.XML('<Root_Element/>')
            tree = ET.ElementTree(root)
    
        elems = tree.findall(tag) 
        if elems == []:
            elem = ET.SubElement(root, tag)  #Tag darf keine Leerzeichen enthalten !
        else:
            elem = elems[0] 
    
        for key in dic:
            elem.attrib[key] = str(dic[key]) # neu oder uenerschrieben
        tree.write(fp) 
    
    def getIdRe(self, s):
        hits = []
        reId = r'[.*_]?([0-9]{5,6})[_|\.].*'
        matches = re.findall(reId, s)
        print matches
        if len(matches) > 1:
            print '... mehrere potentielle Ids gefunden'
            return matches
        return matches[0]

    def convert_string(self,s):
        try:
            u = s.decode("utf-8")
        except UnicodeDecodeError:
            u = s.decode("cp1252")
        return u    
        
    def replace(self, myfile, pattern, subst):
        #Create temp file
        oldfile = myfile
        ext = os.path.split(myfile)
        newfile = os.path.join(ext[0],"temp.txt") 
        new_file = open(newfile,'w')
        old_file = open(oldfile,'r')
        for line in old_file:
            line = self.convert_string(line)
            if pattern in line:
                line=line.replace(pattern,subst)
            new_file.write(line)
            
        #close temp file
        new_file.close()
        old_file.close()
        shutil.move(newfile, oldfile)
  
    