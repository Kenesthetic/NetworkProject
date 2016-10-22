_author__ = 'JohnAdams'

import nltk
import os
import re
import unicodedata
import codecs
import collections
import csv
from nltk.compat import raw_input
import shutil
import cgi
##from pythonFunction import function
##from tyler.py import funtion(creation, connection)



class KnowledgeBaseArticles(object):
    def __init__(self):
        self.KnowledgeBasic = {'kb0':'This Knowledge Base Article verifies if ConfD process has died.  Technician'
                               'will need to access root and fsck all partitions', 'processWatch':'Process Watch has'
                               'found dead processes.'}

class crunchText(object):
    fileDef = 'none'

    def __init__(self):
        self.accountDir = '/'
        self.uploadDir = self.accountDir
        print('Welcome to KnowledgeBasic! \nPlease Press Enter to Proceed...')

    def processWatch(self):
        print('Check File for Process Death')
        print('Please Input Filename')
        file = raw_input('')
        self.log = open(file, 'r')
        self.logRaw = self.log.read()
        self.logs = self.logRaw.splitlines()
        self.processWatch = ['Stopping xhad...', 'Stopping xactiond', 'Stopping xconfigd...']
        self.countProcessWatch = set(self.processWatch) & set(self.logs)
        self.percentProcessWatch = float(len(self.countProcessWatch)) / float(len(self.processWatch))
        self.percentInt = int(self.percentProcessWatch * 100)
        self.prep = repr(self.countProcessWatch)
        self.results = [self.prep]
        print('the messages found in common:')
        print(self.countProcessWatch)
        print('the likely match to KnowledgeBasic0 is:')
        print(self.percentInt)
        print('Creating Result Files...')
        for item in self.countProcessWatch:
            resultsString = open('results.txt', 'w')
            resultsString.write(self.prep)
            resultsFile = open('results.csv', 'w')
            wr = csv.writer(resultsFile, delimiter=' ', lineterminator='\n')
            wr.writerows(self.results)


    def kb0(self):
        print('Check File against KnowlegeBasic')
        print('Please Input Filename')
        self.file = raw_input()
        self.log = open(self.file, 'r')
        self.logRaw = self.log.read()
        self.logs = self.logRaw.splitlines()
        self.KB0 = ['xlicense: ERROR! ERR_STATE_ERR(-18)Confd not running',
                    'xlicense: ERROR! ERR_SYS_ERR (-5)Error calling start_or_wait_for_confd((null))',
                    'xlicense: ERROR! ERR_CONFD_ERR(-300)Could not commit changes!']
        self.countKB0 = set(self.KB0) & set(self.logs)
        self.percentKB0 = float(len(self.countKB0)) / float(len(self.KB0))
        self.percentInt = int(self.percentKB0 * 100)
        self.prep = repr(self.countKB0)
        self.results = [self.prep]
        print('the messages found in common:')
        print(self.countKB0)
        print('the likely match to KnowledgeBasic0 is:')
        print(self.percentInt)
        print('Creating Result Files...')
        for item in self.countKB0:
            resultsString = open('results.txt', 'w')
            resultsString.write(self.prep)
            resultsFile = open('results.csv', 'w')
            wr = csv.writer(resultsFile, delimiter=' ', lineterminator='\n')
            wr.writerows(self.results)


    def upload(self):
        print('Upload Log file to KnowledgeBasic Server')
        print('Please Print File Name')
        self.file = raw_input()
        print('Please Print Directory Path')
        self.uploadDir = raw_input()
        self.uploadFile= self.uploadFile(self.file, self.uploadDir)
        self.form = cgi.FieldStorage()
        if not self.form.has_key(self.file):
            return
        self.fileitem = self.form[self.file]
        if not self.fileitem.file:
            return
        self.outpath = os.path.join(self.uploadDir, self.fileitem.filename)
        with open(self.outpath, 'wb') as fout:
            shutil.copyfileobj(self.fileitem.file, fout, 100000)

    def define(self):
        print('Define New Knowledge Basic Article')


    def prompt(self):
        print('Menu:  u = Upload  a = Analyze d = Define')
        self.option = raw_input()
        while self.option != 'q':
            if self.option == 'a':
                self.kb0()
                print('Completed... Heading back to menu')
            elif self.option == 'u':
                self.upload()
            elif self.option == 'd':
                self.define()



##    print('Testing Reach Into alternate.py file')
##    print(creation())

ct = crunchText()
a=1
while a == a :
    ct.prompt()
