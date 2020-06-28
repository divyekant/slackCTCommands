import Constants
import slackAlert

error_url = ""


def exit_code():
    quit()


def setErrorURL(url):
    global error_url
    error_url = url


def handleError(errorMessage):
    if errorMessage == Constants.error_command_not_matched:
        slackAlert.simpleMessage(Constants.error_command_not_matched_message, error_url)
        exit_code()
    elif errorMessage == Constants.error_API_keys_mismatch:
        slackAlert.simpleMessage(Constants.error_API_keys_mismatch_message, error_url)
        exit_code()
