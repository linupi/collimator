# collimator
This is a collection of scripts to design 3d printed radial collimators.

## Prerequisite & Setup
as this project is not stable yet and there are still pathes everywhere in the scripts it is suggested to put a link to the git in the user home
```
$ cd ~
$ ln -s [PATH TO collimator git] collimator.git
```
- FreeCAD
  - tested with FreeCAD 0.18 (Linux App Image)
  - To have the scripts availabe in the either change the _User macros location_ or link the files inside `FreeCAD_scripts` to the default _user macros location_ (`ln -s collimator.git/FreeCAD_scripts/Collimator.FCMacro ~/.FreeCAD/MacroCollimator.FCMacro`)

## Steps to design a (Soller) collimator
### 1. create grid
  - using python
  
    _to come_
  - using Mathematica
  
    _to come_
### 2. create 3d model
  - using FreeCAD
  
    - put the correct pathes in the `/.FreeCAD/Macro`
  - OpenSCAD
  
    _to_come
    
### 3. validate 3d model
  This is the procedure to do some raytracing on the files generated in the steps above.
  - convert a _.stl_ file into _.inc_ as  _povray_
    
```
$ python2.7 external_tools/py-stl-3.1/stl2pov.py RadialCollimator.stl RadialCollimator.inc
```

  - For the follwoing steps some python dependencies need to be installed e.g. in conda enviroment:
  
```
conda create --name collimator_env python=3.7
conda activate collimator_env
conda config --env --append channels conda-forge
conda install silx moviepy scipy numpy matplotlib imageio jupyter pyyaml
pip install vapory
```
 
 - run povray using
 
```
$ ./raytracing/run_rings_povray.sh
--- or --- if you happen to have a cluster at hand:
$ oarsub -l nodes=1/core=8,walltime=00:02:00 ./raytracing/run_rings_povray.sh
```
 
 - look at the results in a jupter notebook
 
```
$ cd raytracing
$ jupyter notebook
```

## Software dependencies
- python
- [FreeCAD](https://www.freecadweb.org)
- [OpenSCAD](https://www.openscad.org)
- povray

## Further reading
- [A novel 3D printed radial collimator for x-ray diffraction](https://aip.scitation.org/doi/suppl/10.1063/1.5063520) by S. Kowarik, L. Bogula, S. Boitano, F. Carlà, H. Pithan, P. Schäfer, H. Wilming, A. Zykov and L. Pithan 


## Thanks to ... 
- [py-stl-3.1](https://rsmith.home.xs4all.nl/software/py-stl-stl2pov.html) by Roland Smith
   ... the corresponding packages are parcially redistributed in `\external_toos`
