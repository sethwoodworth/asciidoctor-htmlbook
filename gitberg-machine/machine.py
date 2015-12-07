#!/usr/bin/env python2
""" templating machine for gitberg

Usage: python machine.py [options] [templatefiles]

Options:
  -m   put specified metadata file or URL into context
  -h, --help              show this help
  -o   put result in -o directory

Example:
  machine.py -m metadata.yaml content.html   process content.html as a template file with metadata.yaml in the context, save in place

"""

import sys ,getopt, os.path
from jinja2 import FileSystemLoader, Environment
from gitenberg.metadata.pandata import Pandata

def main(argv):                          
    try:                                
        opts, templatefiles = getopt.getopt(argv, "hm:o:", ["help",])
    except getopt.GetoptError:          
        usage()                         
        sys.exit(2) 
    metadata_file = None  
    output_dir = ''                  
    for opt, arg in opts:                
        if opt in ("-h", "--help"):      
            usage()                     
            sys.exit()                  
        elif opt == '-m':                
            metadata_file = arg               
        elif opt == '-o':                
            output_dir = arg               
    if metadata_file:
        pandata = Pandata(metadata_file)
    else:
        pandata = {}
    for templatefile in templatefiles:
        template = env.get_template(templatefile)
        output = template.render(metadata=pandata)
        outputfile = open(os.path.join(output_dir,templatefile),'w')
        outputfile.write(output.encode("UTF-8"))
        outputfile.close()

def usage():
    print __doc__

tempdir = os.path.join(os.path.dirname(sys.argv[0]), 'templates/')
env = Environment(loader=FileSystemLoader([tempdir,'/',]))
main(sys.argv[1:])