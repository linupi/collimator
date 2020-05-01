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
  
   _to_come_
  
## Software dependencies
- python
- [FreeCAD](https://www.freecadweb.org)
- [OpenSCAD](https://www.openscad.org)

## Further reading
- [A novel 3D printed radial collimator for x-ray diffraction](https://aip.scitation.org/doi/suppl/10.1063/1.5063520) by S. Kowarik, L. Bogula, S. Boitano, F. Carlà, H. Pithan, P. Schäfer, H. Wilming, A. Zykov and L. Pithan 
