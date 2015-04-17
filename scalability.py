import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def speedup(newTime,referenceTime):
    return referenceTime / newTime

def efficiency(numberOfProcessors,parallelTime,sequentialTime):
  return speedup(parallelTime,sequentialTime) / numberOfProcessors

def plotSpeedup(numbersOfProcessors,parallelTimes,sequentialTime=None):

  if sequentialTime is None:
    sequentialTime = parallelTimes[0]

  actualSpeedup = speedup(parallelTimes,sequentialTime)
  linearSpeedup = numbersOfProcessors

  plt.plot(numbersOfProcessors,actualSpeedup,'o-')
  plt.plot(numbersOfProcessors,linearSpeedup,'ro-')

  red_patch = mpatches.Patch(color='red', label='Linear speedup')
  blue_patch = mpatches.Patch(color='blue', label='Actual speedup')
  plt.legend(handles=[blue_patch, red_patch],loc='upper left')

  plt.xlabel('Number of processing units')
  plt.ylabel('Time in seconds')

  plt.grid()

  plt.show()
