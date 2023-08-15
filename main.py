# -*- coding: utf-8 -*-
"""
Created on Sat May 21 15:01:34 2022

@author: AH34926
"""
class Container:
    _element_positions = []
    _copybook_impacts = []
    _move_static_impacts = []
    _move_dynamic_impacts = []
    _call_static_impacts = []
    _call_dynamic_impacts = []
    _perform_impacts = []
    
    def get_Elements(self,data):
        for line in range(len(data)):
            if "ELEMENT" in data[line]:
                self._element_positions.append([line,data[line].split()[-1]])
                
                
    def print_data(self,data):
        for i in list(set(data)):
            print(i)
            
    def do_ImpactAnalysis(self,data):
        for i in range(len(self._element_positions)-1):
            first,last = self._element_positions[i],self._element_positions[i+1]
            #print("first is ",first)
            #print("last is ",last)
            for j in range(first[0],last[0]):
                #print(j)
                if "COPY" in data[j]:
                    self._copybook_impacts.append(first[1])
                if "MOVE " in data[j]:
                    if "MOVE '" in data[j]:
                        self._move_static_impacts.append(first[1])
                    else:
                        self._move_dynamic_impacts.append(first[1])
                if "CALL " in data[j]:
                    if "CALL '" in data[j]:
                        self._call_static_impacts.append(first[1])
                    else:
                        self._call_dynamic_impacts.append(first[1])
                if "PERFORM" in data[j]:
                    self._perform_impacts.append(first[1])
                    
                
                    
        
                
    
                
                
    
        

if __name__ == "__main__":
    obj = Container()
    with open("input.txt") as f:
        datas = f.read()
        datas = datas.split("\n")
        #obj.print_data(datas)
        data =[]
        for i in datas:
            if not "*" in i:
                data.append(i)
        #print("*******************")        
        #obj.print_data(data)
        obj.get_Elements(data)
        last_element_index = data.index(data[-1])
        #print(last_element_index,data[-1])
        obj._element_positions.append([last_element_index,"BOTTOM"])
        obj.do_ImpactAnalysis(data)

        print("copybook impacts are :")
        obj.print_data(obj._copybook_impacts)
        #print(obj._element_positions)
        print("Static moves are :")
        obj.print_data(obj._move_static_impacts)
        print("Static Calls are :")
        obj.print_data(obj._call_static_impacts)
        print("Dynamic moves are :")
        obj.print_data(obj._move_dynamic_impacts)
        print("Dynamic Calls are :")
        obj.print_data(obj._call_dynamic_impacts)
        print("perform impacts are :")
        obj.print_data(obj._perform_impacts)

        
        
        
        
        
        

