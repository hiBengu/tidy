from pathlib import Path
import os
import logging
import yaml
import shutil

'''
Features
    - Group files with same extensions under same folder
    - Remove compressed files if they are opened
'''

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
        self.project_name = "tidy"
        self.home_directory = os.path.expanduser("~")
        self.organizer_config_path = self.home_directory + "/.config/" + self.project_name
        self.config_file = self.organizer_config_path + "/config"
        self.example_config = "./example.config"
        self.log_file = self.organizer_config_path + '/organizer.log'

        self.bypass_parameter = '_'

        # Create path for config
        if (not os.path.isdir(self.organizer_config_path)):
            os.makedirs(self.organizer_config_path)

        # Folder type definitions
        self.misc_folders = []
        self.note_folders = []

        # Logger definitons
        self.logger = logging
        self.logger.basicConfig(filename=self.log_file, encoding='utf-8', level=logging.DEBUG, filemode = 'w')

        self.logger.info('Init of organizer is started.')


        if (not os.path.exists(self.config_file)):
            example_config = open(self.example_config, 'r')
            self.initial_config_file = example_config.read()
            example_config.close()
            config_file = open(self.config_file, 'w+')
            config_file.write(self.initial_config_file)
            config_file.close()
            self.logger.info('Config file created.')
        else:
            self.logger.info('Config file already exists.')

        self.logger.info("Init of organizer object is completed.")

    def readConfig(self):
        '''
        Desc:
            Read the config file and get necessary variables
        Input:
            self.config_file: location of the config file
        Output:
            self.folders: paths of the folders that will be organized
        '''

        self.logger.info('Start to read config!')

        with open(self.config_file) as config:
            configStr = config.read()
            attributes = yaml.safe_load(configStr)
            self.misc_folders = attributes['miscFolders']
            self.note_folders = attributes['noteFolders']
            self.unique_folders = ['txt', 'zip', 'gz', 'pdf'] # todo: read from config
            config.close()

        # Rearrange folder paths
        for i, path in enumerate(self.misc_folders):
            if '~' in path:
                self.misc_folders[i] = path.replace('~', self.home_directory)

        for i, path in enumerate(self.note_folders):
            if '~' in path:
                self.note_folders[i] = path.replace('~', self.home_directory)

        self.logger.info('Misc Folders: '+ ' '.join(self.misc_folders))
        self.logger.info('Note Folders: '+ ' '.join(self.note_folders))

        self.logger.info('Read config ended!')

    def tidyFolders(self):
        '''
        Desc:
            Tidy given Folders
                - Read previously created folders
                - List all files under a certain folder
                - Create subfolders
                - Move files
        Input:
            self.misc_folders: Folder paths
            self.note_folders: Folder paths
        Output:
            Na
        '''
        self.logger.info('Start to tidy folders!')

        for folder in self.misc_folders:
            current_folders = []
            contents = os.listdir(folder)
            for i, content in enumerate(contents):
                if(os.path.isdir(folder+'/'+content)):
                    current_folders.append(contents.pop(i))

            if 'misc' not in current_folders:
                current_folders.append('misc')
                os.makedirs(folder+'/misc/', exist_ok=True)

            for content in contents:
                content_splits = os.path.splitext(content)
                extension = content_splits[1]
                extension = extension.replace('.', '');
                if extension != '' and extension not in current_folders:
                    if extension in self.unique_folders:
                        current_folders.append(extension)
                        if (not os.path.isdir(folder+'/'+extension+'/')):
                            os.makedirs(folder+'/'+extension+'/')
                if extension in self.unique_folders:
                    shutil.move(folder+"/"+content, folder+'/'+extension+'/')
                else:
                    shutil.move(folder+"/"+content, folder+'/misc/')

            self.logger.info('Main folders under the directory: ' + str(folder))
            self.logger.info(current_folders)

        self.logger.info('End tidy folders!')

    def startProcess(self):
        '''
        Desc:
            Starts the main process of the tidy
        Input:
            Na
        Output:
            Na
        '''
        self.readConfig()
        self.tidyFolders()

tidyObject = Tidy()
tidyObject.startProcess()
