#!/usr/local/python/2.7.3/bin/python
import naming
import os
import re, sys, subprocess

#TODO integrate constructExpname with the framework


#{p=GFDL-PPnodes, z=Zeus, g=gaea, s=Sooner, k=kd workstation, etc.}.
def constructExpname(lname_project,lname_target,series,method,basedir):
	expconfig = ""
	mapdir = basedir+"/utils/auxfiles/"
	proj_mappings = mapdir+"project_map"
	f = open(proj_mappings,'r')
	sname_project = ''
 	for line in f:
   		if  re.match('^longname:'+lname_project,line):
    			fields=line.split(',')
    			lname_project = fields[0].split(':')[1]
    			sname_project = fields[1].split(':')[1].strip()
      	if(sname_project == ''):
		print "project",lname_project,"not found in project_map."
		sname_project = lname_project
		print "Using ",lname_project," as default for sname_project(short name)"
	print sname_project
	f.close()
        target_mappings = mapdir+"target_map"
        f = open(target_mappings,'r')
        sname_target = ''
        for line in f:
                if  re.match('^longname:'+lname_target,line):
                        fields=line.split(',')
                        lname_target = fields[0].split(':')[1]
                        sname_target = fields[1].split(':')[1].strip()
        if(sname_target == ''):
                print "target",lname_target,"not found in target_map."
                sname_target = lname_target
                print "Using ",lname_target," as default for sname_target(short name)"
        print sname_target
	## get platform code
	system,node,release,version,machine = os.uname()
	if(node.startswith('pp')):
		print "Running on PP node", node
		plat = "p" 
	if(node.startswith('an')):
                print "Running on AN node", node
		plat = "a"
	else:
                print "Running on a workstation", node
	        plat = node 
	plat.strip()
        expconfig = sname_project+sname_target+plat+"-"+method+"-"+series  #eg kd_PMtxp2-GFDL-ARRMv3-B00X01K02
	#print expconfig
	return expconfig
  
 
