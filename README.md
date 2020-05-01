# collimator
This is a collection of scripts to design 3d printed collimators.

## Prerequisite & Setup
- FreeCAD
  - tested with FreeCAD 0.18 (Linux App Image)
  - To have the scripts availabe in the either change the _User macros location_ or link the files inside `FreeCAD_scripts` to the default _user macros location_ (`ln -s collimator.git/FreeCAD_scripts/Collimator.FCMacro ~/.FreeCAD/MacroCollimator.FCMacro`)

## Steps to design a (Soller) collimator
1. create grid
1. create 3d model
  1.1 Using FreeCAD
    - put the correct pathes in the `/.FreeCAD/Macro`
1. validate 3d model

## Software dependencies
- python
- [FreeCAD](https://www.freecadweb.org)
- [OpenSCAD](https://www.openscad.org)

## Further reading
- [A novel 3D printed radial collimator for x-ray diffraction](https://aip.scitation.org/doi/suppl/10.1063/1.5063520) by S. Kowarik, L. Bogula, S. Boitano, F. Carlà, H. Pithan, P. Schäfer, H. Wilming, A. Zykov and L. Pithan 
