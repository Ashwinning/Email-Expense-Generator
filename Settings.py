settings = {}

'''
Removes tags and leading/trailing whitespaces.
'''
def Sanitize(description):
    sanitized = description
    for tag in description.split():
        if tag.startswith("#"):
            sanitized = sanitized.replace(tag, "")
    #Remove trailing whitespaces
    sanitized = sanitized.rstrip()
    return sanitized


class GetSettings:
    settings = {}
    def __init__(self):
        with open(".settings", "r") as values:
            for value in values:
                value.strip() #Remove whitespaces
                #Not a comment, not just a linebreak
                if not(value.startswith('#') or (value in ['\n', '\r\n'])):
                    #print ('Found Line : ' + value)
                    #Remove trailing comments
                    Sanitize(value)
                    keyVal = value.split('=')
                    settings[keyVal[0]] = keyVal[1].strip()
                    #print(keyVal[0] + ' ' + settings[keyVal[0]])

'''
Store settings in the following format in a `.settings` file:
    ###
    # Required Settings.
    ###
    emailID=emailgoeshere
    password=passwordgoeshere
    ###
    # Other Settings.
    ###
    emailID=emailgoeshere
    password=passwordgoeshere

Usage:
    from Settings import *


    #Initialize this at the beginning of the lifecycle.
    settings = GetSettings()

    >>> settings['emailID']
    'emailgoeshere'

'''
