import logging
import os

def setupLogger():
    logFilePath = os.path.join(os.getcwd(), "logs/custom_widgets.log")
    # Ensure the log directory exists
    logDirectory = os.path.dirname(logFilePath)
    if logDirectory != "" and not os.path.exists(logDirectory):
        os.makedirs(logDirectory)

    # Set up the logger
    logging.basicConfig(filename=logFilePath, level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def logInfo(self, message):
    logging.info(message)
    if self.showCustomWidgetsLogs:
        print(message)

def logWarning(self, message):
    logging.warning(message)
    if self.showCustomWidgetsLogs:
        print(message)

def logError(self, message):
    logging.error(message)
    if self.showCustomWidgetsLogs:
        print(message)

def logException(self, exception, message="Exception"):
    logging.exception(f"{message}: {exception}")
    if self.showCustomWidgetsLogs:
        print(message)

setupLogger()

# Log messages
# logInfo("This is an informational message.")
# logWarning("This is a warning message.")
# logError("This is an error message.")
# logException(e, "An exception occurred")

