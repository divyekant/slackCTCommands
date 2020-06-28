import re
import Constants


def getCommandKeys(text):
    templates = Constants.command_templates
    isTokenSet = False
    for template in templates:
        tokens = re.match(template, text)
        if tokens is not None:
            isTokenSet = True
            break

    if not isTokenSet:
        return Constants.error_command_not_matched
    else:
        commandStructure = getCommandStructure(tokens)
        return generateCommandObject(commandStructure, tokens)


def getCommandStructure(tokens):
    cType = tokens.group(1)
    if cType.lower() == Constants.trend:
        if tokens.lastindex == Constants.trend_base_template_token_count:
            return Constants.trend_command_base_keys
        elif tokens.lastindex == Constants.trend_base_template_with_property_token_count:
            return Constants.trend_command_base_keys_with_property
        elif tokens.lastindex == Constants.trend_base_template_with_time_token_count:
            return Constants.trend_command_base_keys_with_time


def generateCommandObject(commandStructure, tokens):
    commandObject = {}
    for i in range(0, len(commandStructure)):
        if tokens.group(i + 1) is not None:
            commandObject[commandStructure[i]] = tokens.group(i + 1)
        else:
            commandObject[commandStructure[i]] = None
    return commandObject
