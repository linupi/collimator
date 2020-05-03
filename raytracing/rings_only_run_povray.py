
# coding: utf-8

# In[5]:

### manual change in vapory after installation : remove the follwoing line in the code:
### self.camera = self.camera.add_args(['right', [1.0*width/height, 0,0]])

from vapory import *
import numpy as np
from moviepy.editor import ImageSequenceClip
from silx.math.histogram import Histogramnd


# In[2]:

# calculate ring pattern
dis = 1; #(*distance lightsource pinhole in mm*)
widthInRadian =  np.deg2rad(0.25) #(*natual width of the reflections*)
ringpos = np.deg2rad([2,  4, 6, 9,12,15,18]) #(*angular position of diffraction features*)

def CalcMinMaxRad(r): 
    return np.transpose(np.array([np.tan(r - widthInRadian/2)*dis,np.tan(r + widthInRadian/2)*dis]))

rings = CalcMinMaxRad(ringpos)
rings=np.array(rings).flatten()

##position in the simulation
sim_pos=np.arange(-10,10,.1)


# In[3]:

# povray output parameters
pov_width = 601
pov_height=601
pov_antialiasing=0.001
soller="../RadialCollimator.inc"



# In[8]:

# camera = Camera( 'orthographic','up', [0,500,0] , 'right', [500,0,0],'location', [0, 100, 0], 'look_at', [0,400, 0])
#camera = Camera( 'orthographic','angle 100', 'up', [0,100,0],'right', [100,0,0] ,'location', [0, 100, 0], 'look_at', [0,400, 0])
camera = Camera( 'orthographic','angle 57', 'up', [0,100,0],'right', [100,0,0] ,'location', [0, 100, 0], 'look_at', [0,400, 0])


camera = Camera( 'orthographic','angle 35', 'up', [0,100,0],'right', [100,0,0] ,'location', [120, 100, 120], 'look_at', [120,600, 120])


def scene(p,useSoller=False,showMask=True):
    """ Returns the scene at time 't' (in seconds) """
    #p=t #*10-20
    box = Box( [1.5, p+dis+0.001, 1.5], [-1.5, p+dis-0.001, -1.5])
    
    cylinders_thin=[]
    cylinders_thick=[]
    for i in range(0,len(rings)):
        cylinders_thin.append(Cylinder ( [0,p+dis-.001, 0], [0, p+dis+.001, 0], rings[i] ))
        cylinders_thick.append(Cylinder ( [0,p+dis-.002, 0], [0, p+dis+.002, 0], rings[i] ))

    difs=[]
    for i in range(2,len(rings),2):
        difs.append(Difference(cylinders_thin[i],cylinders_thick[i-1]))
        
    #cylinder1 = Cylinder ( [0,p-.2, 0], [0, p+.2, 0], .5 )
    #cylinder2 = Cylinder ( [0, p-.2, 0], [0, p+.2, 0], .4 )

   # mydif=Difference(box,cylinder1)
   # myunion=Union(mydif,cylinder2)
    
    #myunion=Union(difs)
    
    myunion=cylinders_thin[0]
    for i in range(0,len(difs)):
        myunion=Union(myunion,difs[i])
    
    myunion=Union(myunion,Difference(box,cylinders_thick[-1]))
    
    ###for test
   # myunion = Cylinder ( [0,p+dis-.1, 0], [0, p+dis+.1, 0], rings[6] )
    
    #print(len(difs))
    
    #camera = Camera( 'orthographic','angle 57', 'up', [0,1,0],'right', [5,0,0] ,'location', [135, 100, 0], 'look_at', [135,400, 0])

    
    s= Scene( camera,
            [ LightSource( [0, p,0],'color', [1, 1, 1]),
              
              Plane([0,1,0],800,Texture(Pigment('color', [1, 1, 1]))),
            ])
    #s.add_objects(['m_OpenSCAD_Model'])
    if showMask:
        s.objects.append(myunion)
    
    if useSoller:
        s.objects.append('m_OpenSCAD_Model')
        s.included=[soller]
    

    
    return s


# In[ ]:

frames=[]

radial_intensities=[]

for i in sim_pos:
    a=scene(i).render(width = pov_width, height=pov_height, antialiasing=pov_antialiasing,remove_temp=False)
    b=np.sum(a,axis=2)
    frames.append(a)
    print(i)


clip = ImageSequenceClip(frames, fps=5)
clip.write_gif("no_soller.gif")
    


# In[ ]:

frames=[]

radial_intensities=[]

for i in sim_pos:
    a=scene(i,useSoller=True).render(width = pov_width, height=pov_height, antialiasing=pov_antialiasing,remove_temp=False)
    b=np.sum(a,axis=2)
    frames.append(a)
    print(i)


clip = ImageSequenceClip(frames, fps=5)
clip.write_gif("soller.gif")

#####


frames=[]

radial_intensities=[]

a=scene(0,useSoller=False,showMask=False).render(width = pov_width, height=pov_height, antialiasing=pov_antialiasing,remove_temp=False)
frames.append(a)


a=scene(0,useSoller=True,showMask=False).render(width = pov_width, height=pov_height, antialiasing=pov_antialiasing,remove_temp=False)
frames.append(a)



clip = ImageSequenceClip(frames, fps=5)
clip.write_gif("shadow.gif")
    
