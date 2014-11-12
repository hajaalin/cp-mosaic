cp-mosaic
=========

ImageJ plugin script for using MosaicSuite for particle detection in CellProfiler.

MosaicSuite: http://mosaic.mpi-cbg.de/?q=downloads/imageJ#
ParticleTracker_.java: https://git.mpi-cbg.de/gitweb/?p=ImageJ.git;a=blob;f=plugin/src/mosaic/plugins/ParticleTracker_.java;h=9ab7e31563c237cc455244755840022af6ede98d;hb=HEAD

1. Testing from command line

Prerequisites:
- install Fiji
- enable Mosaic suite in Fiji -> Help -> Update ... Manage update sites

Run from command line:
ImageJ-linux64 mosaic.py testimage.tif


2. Using with CellProfiler

Prerequisites:
- place mosaic_pt.py in "ImageJ plugins folder"
- place Mosaic_ToolSuite.jar in "ImageJ plugins folder"

Run with "RunImageJ" module:
Macro:  run("mosaic pt");


