from ij import IJ, ImagePlus, WindowManager
from ij.process import ByteProcessor, StackStatistics
from mosaic.plugins import ParticleTracker_ as PT

import re
import sys

# read image from command line
if len(sys.argv) > 1:
    imp = IJ.openImage(sys.argv[1])
# if command line not given, use current image (works in CellProfiler)
else:
    imp = WindowManager.getCurrentImage()

pt = PT()

pt.frames_number = 1
pt.stack = imp.getStack()
stack_stats = StackStatistics(imp)
pt.global_max = stack_stats.max
pt.global_min = stack_stats.min

pt.percentile = 0.8 / 100
pt.cutoff = 3.0
pt.radius = 2
pt.makeKernel(pt.radius)
pt.generateMask(pt.radius)

pt.setup("only_detect", imp)

pt.processFrames()
frame = pt.frames[0]

prog = re.compile("%.*Particle (\d+) \((\d+.\d+), (\d+.\d+)\)")
lines = frame.toString().split("\n")

ip_old = imp.getProcessor()
ip_new = ByteProcessor(ip_old.getWidth(), ip_old.getHeight())
for l in lines:
    #print "line", l
    result = re.search(prog, l)
    if result:
        n = result.groups()[0]
        y = result.groups()[1]
        x = result.groups()[2]
        #print n, x, y 

        x = int(round(float(x)))
        y = int(round(float(y)))
        ip_new.putPixel(x,y,255)

imp_new = ImagePlus("mosaic_pt", ip_new)

# show image 
if len(sys.argv) > 1:
    imp_new.show()
# if command line not given, set current image (works in CellProfiler)
else:
    WindowManager.setTempCurrentImage(imp_new)


