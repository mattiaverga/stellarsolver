#include "astrometrylogger.h"

AstrometryLogger::AstrometryLogger()
{
    timeSinceLastOutput.start();
    connect(&logUpdater, &QTimer::timeout, this, &AstrometryLogger::updateLog);
    logUpdater.start(100);
}

void AstrometryLogger::logFromAstrometry(char* text)
{
    logText += text;
    updateLog();
}

void AstrometryLogger::updateLog()
{
    if(readyToLog())
    {
        emit logOutput(logText);
        timeSinceLastOutput.restart();
        logText = "";
    }
}

bool AstrometryLogger::readyToLog()
{
    return timeSinceLastOutput.elapsed() > 100 && logText.length() > 0;
}
