import os
import logging
import configparser

class Organizer():
    def __init__(self):
        '''
        Desc:
            Initialize function for Organizer.
            Create config file and directory if not already exist.
        Input:
            Na
        Output:
            Na
        '''
        # Variable definitions
        self.projectName = "folderOrganizer"
        self.homeDirectory = os.path.expanduser("~")
        self.organizerConfigPath = self.homeDirectory + "/.config/" + self.projectName
        self.configFile = self.organizerConfigPath + "/config"
        self.exampleConfig = "./example.config"
        self.logFile = self.organizerConfigPath + '/organizer.log'

        # Create path for config
        if (not os.path.isdir(self.organizerConfigPath)):
            os.makedirs(self.organizerConfigPath)

        # Folder type definitions
        self.miscFolders = []
        self.noteFolders = []

        # Logger definitons
        self.logger = logging
        self.logger.basicConfig(filename=self.logFile, encoding='utf-8', level=logging.DEBUG, filemode = 'w')

        self.logger.info('Init of organizer is started.')


        if (not os.path.exists(self.configFile)):
            exampleConfig = open(self.exampleConfig, 'r')
            self.initialConfigFile = exampleConfig.read()
            exampleConfig.close()
            configFile = open(self.configFile, 'w+')
            configFile.write(self.initialConfigFile)
            configFile.close()
            self.logger.info('Config file created.')
        else:
            self.logger.info('Config file already exists.')

        self.logger.info("Init of organizer object is completed.")

    def readConfig(self):
        '''
        Desc:
            Read the config file and get necessary variables
        Input:
            self.configFile: location of the config file
        Output:
            self.folders: paths of the folders that will be organized
        '''

        self.logger.info('Start to read config!')

        config = configparser.ConfigParser()
        config.read(self.configFile)

        self.logger.info('Read config ended!')

    def listFiles(self):
        '''
        Desc:
            Na
        Input:
            Na
        Output:
            Na
        '''

    def createSubFolders(self):
        '''
        Desc:
            Na
        Input:
            Na
        Output:
            Na
        '''

    def moveFiles(self):
        '''
        Desc:
            Na
        Input:
            Na
        Output:
            Na
        '''

    def saveLog(self):
        '''
        Desc:
            Na
        Input:
            Na
        Output:
            Na
        '''

    def exitOrganizer():
        '''
        Desc:
            Na
        Input:
            Na
        Output:
            Na
        '''
        self.saveLog()
        exit()

    def startProcess(self):
        '''
        Desc:
            Starts the main process of the organizer
        Input:
            Na
        Output:
            Na
        '''
        self.readConfig()
        self.listFIles()
        self.createSubFolders()
        self.moveFiles()
        self.saveLog()

organizerObject = Organizer()
organizerObject.readConfig()
