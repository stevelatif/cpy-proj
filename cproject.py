#!/usr/bin/env python
import argparse
from string import Template
import os
import logging
import pwd
from datetime import date

"""
Toolkit for creating projects in C python string templates. Sets up a basic project that can be
built on. 
unittests, code coverage, profiling are set up from the get go, just jumo in and start coding your
project. At any time you need an example of how unittests, code profiling and code coverage should be
set up, you have the examples.

Everything will compile with no errors on Linux and BSD
Everything will run without error on Linux and BSD

"""

class CProject():
    def __init__(self, name, ptype):
        self.project_name = name
        self.project_name_gate = name
        self.project_type = ptype
        #self.project_style = pstyle
        self.unit_tests = ""
        self.header_banner = ""

    '''Create a directory to put all the project files. The name
    of the directory will be the project name and will be in the
    directory where the program is being run. 
    Assume that the user has permission to create the directory. 
    We check first that the directory does not exist.
    '''
    def _create_project_dirs(self, dir_name):
        # Check if the directory exists
        self.unit_tests = dir_name
        if os.path.exists(dir_name):
            print "a file with the name already exists, bailing "
            logging.info(
                "a file or directory with that name %s already exist, exiting" % dir_name)
            os._exit(-1)
        else:
            # try is redundant with the above check, but just in case ...

            try:
                os.mkdir(dir_name)
                #os.mkdir(self.unit_tests)
            except OSError, ose:
                logging.error("Directory already exists " +  str(ose))
                
    def _populate_template(self, template_name, values, header = ""):
        # open template and populate values
        try:
            filein = open(os.path.join('templates', template_name))
        except Exception, oe:
            print "open error " + str(oe)
        src = Template( filein.read() )
        try:
            result = src.substitute(values)
        except Exception, e:
            print "substition error: " + str(e)
        filein.close()
        return result
    def read_header(self):
        txt = open(self.header)
        self.header = txt.read()
    def _write_file(self, filename, content):
        outfile = open(filename, "w")
        outfile.write(content)

    def simple_console(self):
        self.project_name_gate = "__" + str.upper(self.project_name) + "__" + "H__"
        self._create_project_dirs(self.project_name)
        
        # Add source file
        proj = self._populate_template('hello.c', {'project_name':self.project_name,
                                                   'header_banner':self.header_banner})
        self._write_file(os.path.join(self.project_name, self.project_name) + ".c", proj)

        # Create Header
        header = self._populate_template('hello.h', {'project_name_gate':self.project_name_gate,
                                                     'header_banner':self.header_banner})
        self._write_file(os.path.join(self.project_name, self.project_name) + ".h", header)

        # Create Makefile
        project_name_test = self.project_name + "_test"
        make = self._populate_template('hello_makefile', 
                                       {'project_name':self.project_name, 
                                        'project_name_test':project_name_test})
        self._write_file(os.path.join(self.project_name, 'Makefile'), make)

        # Create Unittests 
        unitt = self._populate_template('unit_test.c', {'project_name':self.project_name,
                                        'header_banner':self.header_banner})
        filename = os.path.join(self.unit_tests, 'unit_tests.c')
        self._write_file(filename, unitt)

    def simple_daemon(self):
        self.project_name_gate = "__" + str.upper(self.project_name) + "__" + "H__"
        self._create_project_dirs(self.project_name)
        
        # Add source file
        proj = self._populate_template('simple_daemon_02.c', {'project_name':self.project_name,
                                                   'header_banner':self.header_banner})
        self._write_file(os.path.join(self.project_name, self.project_name) + ".c", proj)

        # Create Header
        header = self._populate_template('hello.h', {'project_name_gate':self.project_name_gate,
                                                     'header_banner':self.header_banner})
        self._write_file(os.path.join(self.project_name, self.project_name) + ".h", header)

        # Create Makefile
        project_name_test = self.project_name + "_test"
        make = self._populate_template('hello_makefile', 
                                       {'project_name':self.project_name, 
                                        'project_name_test':project_name_test})
        self._write_file(os.path.join(self.project_name, 'Makefile'), make)

        # Create Unittests 
        unitt = self._populate_template('unit_test.c', {'project_name':self.project_name,
                                        'header_banner':self.header_banner})
        filename = os.path.join(self.unit_tests, 'unit_tests.c')
        self._write_file(filename, unitt)

    def event_server(self):
        self.project_name_gate = "__" + str.upper(self.project_name) + "__" + "H__"
        self._create_project_dirs(self.project_name)
        
        # Add source file
        proj = self._populate_template('libevent_server01.c', {'project_name':self.project_name,
                                                   'header_banner':self.header_banner})
        self._write_file(os.path.join(self.project_name, self.project_name) + ".c", proj)

        # Create Header
        header = self._populate_template('hello.h', {'project_name_gate':self.project_name_gate,
                                                     'header_banner':self.header_banner})
        self._write_file(os.path.join(self.project_name, self.project_name) + ".h", header)

        # Create Makefile
        project_name_test = self.project_name + "_test"
        make = self._populate_template('hello_makefile', 
                                       {'project_name':self.project_name, 
                                        'project_name_test':project_name_test})
        self._write_file(os.path.join(self.project_name, 'Makefile'), make)

        # Create Unittests 
        unitt = self._populate_template('unit_test.c', {'project_name':self.project_name,
                                        'header_banner':self.header_banner})
        filename = os.path.join(self.unit_tests, 'unit_tests.c')
        self._write_file(filename, unitt)

def main():
    default_header = "/*\n * Copyright (c) " + pwd.getpwuid( os.getuid() )[ 0 ] + " " + str(date.today().year) + "\n */"
    using_default = False
    parser = argparse.ArgumentParser()
    parser.add_argument("--project_name", help = "name of the project")
    parser.add_argument("--project_type", help = "accepted types: simple_console, simple_daemon, event_server")
    parser.add_argument("--header", 
                        help = "header template: default is copyright only",
                        default = 'default_header')
    parser.add_argument("--project_templates", help = "template file directories")
    args = parser.parse_args()
    cproj = CProject(args.project_name, args.project_type)
    if args.header != "default_header": #### FIXME ####
        if os.path.isfile(args.header):
            # open the file and load the text into the header
            header_file = ""
            try:
                header_file = open(args.header)
            except Exception, oe:
                print "open error " + str(oe)
            cproj.header_banner = header_file.read()
    else:
        cproj.header_banner = default_header

    if args.project_type == 'simple_console':
        cproj.simple_console()
    elif args.project_type == 'simple_daemon':
        cproj.simple_daemon()
    elif args.project_type == 'event_server':
        cproj.simple_daemon()

if __name__ == '__main__':
    main()
