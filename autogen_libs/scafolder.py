#!/usr/bin/env python
# scafolder for my flask project
# @author alfin.akhret@gmail.com
import os
import sys
import zipfile

class Scafolder():
    '''
    Scafold basic flash directory structures
    and files
    '''
    def __init__(self, project_name, project_type):
        self.project_name = project_name + '/'
        self.project_type = project_type

    def install(self):
        '''
        create a project folders
        if project name is empty then
        create the project in current CWD
        @param pf (project folder, default='')
        ''' 

        print 'Creating project folders and files'

        base_contents = 'base_contents/' + self.project_type + '.zip'
        print base_contents
        if os.path.exists(base_contents):
            try:
                self.__unzipper(base_contents, self.project_name)
            except OSError as e:
                print e
                sys.exit(1)
        
        # self.__create_virtual_environment()

    
    def __unzipper(self, file_to_unzip, outpath):
        fh = open(file_to_unzip, 'rb')
        z = zipfile.ZipFile(fh)
        for name in z.namelist():
            z.extract(name, outpath)
            print 'writing...' + name
        fh.close()

    def __create_virtual_environment(self):
        '''
        create project virtual environment
        '''
        os.chdir(self.project_name)
        
        print 'Setting up virtual environment ...'
        os.system('virtualenv venv')
        
        print 'Done!'


if __name__ == '__main__':

    if len(sys.argv) > 1:
        project_name = sys.argv[1]
        project_type = sys.argv[2]
    else:
        project_name = '.'
    scafolder = Scafolder(project_name, project_type)
    scafolder.install()


