import os
import logging
import yaml

class Tidy():
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
        self.projectName = "tidy"
        self.homeDirectory = os.path.expanduser("~")
        self.organizerConfigPath = self.homeDirectory + "/.config/" + self.projectName
        self.configFile = self.organizerConfigPath + "/config"
        self.exampleConfig = "./example.config"
        self.logFile = self.organizerConfigPath + '/organizer.log'

        self.bypassParameter = '_'

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

        with open(self.configFile) as config:
            configStr = config.read()
            attributes = yaml.safe_load(configStr)
            self.miscFolders = attributes['miscFolders']
            self.noteFolders = attributes['noteFolders']
            config.close()

        # Rearrange folder paths
        for i, path in enumerate(self.miscFolders):
            if '~' in path:
                self.miscFolders[i] = path.replace('~', self.homeDirectory)

        for i, path in enumerate(self.noteFolders):
            if '~' in path:
                self.noteFolders[i] = path.replace('~', self.homeDirectory)

        self.logger.info('Misc Folders: '+ ' '.join(self.miscFolders))
        self.logger.info('Note Folders: '+ ' '.join(self.noteFolders))

        self.logger.info('Read config ended!')

    def tidyFolders(self):
        '''
        Desc:
            Tidy given Folders
                - List all files under a certain folder
                - Create subfolders
                - Move files
        Input:
            self.miscFolders: Folder paths
            self.noteFolders: Folder paths
        Output:
            Na
        '''


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
        self.tidyFolders()

tidyObject = Tidy()
tidyObject.startProcess()
