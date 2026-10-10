"""Render a captioned 64-second conceptual robotic arm film. Requires Python, Pillow, NumPy and ffmpeg."""
from PIL import Image, ImageDraw, ImageFont
import numpy as np, math, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'media'; OUT.mkdir(exist_ok=True)
W,H,FPS=1280,720,24
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
fonts={n:ImageFont.truetype(font,n) for n in [16,18,20,22,24,28]}
fonts[44]=ImageFont.truetype(bold,44); fonts[34]=ImageFont.truetype(bold,34)
chapters=[
('MEET THE ARM','Four movements.','One small robot.',['Base • shoulder • elbow • gripper','Two joysticks command four servos.'], 'A virtual model explains the project. Actual hardware still needs testing.'),
('01 / BASE','Turn left.','Turn right.',['Joystick 1 X → A0','Uno D3 → base servo signal'], 'Moving the base rotates the whole arm around its vertical axis.'),
('02 / SHOULDER','Raise the arm.','Lower the arm.',['Joystick 1 Y → A1','Uno D5 → shoulder servo signal'], 'The shoulder lifts the links and everything they carry.'),
('03 / ELBOW','Reach out.','Fold back.',['Joystick 2 X → A2','Uno D6 → elbow servo signal'], 'Changing the elbow angle changes the reach of the gripper.'),
('04 / GRIPPER','Open. Close.','Hold an object.',['Joystick 2 Y → A3','Uno D9 → gripper servo signal'], 'Close gently around an object. Grip strength depends on the real mechanism.'),
('05 / CONTROL & POWER','You move the stick.','The Uno responds.',['Read joystick → change target angle','Servo signal → joint movement'], 'Servos use a separate rated supply. Connect supply ground to Uno ground.'),
('06 / A COMPLETE MOVE','Reach. Grip.','Lift. Turn. Place.',['Coordinated motion • illustrative sequence','Current firmware: joystick control'], 'The scripted motion here is a simulation, not an autonomous hardware feature.'),
('07 / BUILD IT NEXT','Wire. Calibrate.','Test. Then extend.',['First: one unloaded servo at a time','Later: camera tracking on a laptop'], 'Camera → Python → USB → Uno is a planned upgrade, not implemented yet.')]
def txt(d,x,y,s,size=22,fill='#e9f0fc'):d.text((x,y),s,font=fonts[size],fill=fill)
def smooth(t):return t*t*(3-2*t)
def proj(p):
 x,y,z=p;return (830+100*(.84*x-.54*y),478+100*(.30*x+.46*y-.90*z))
def depth(p):x,y,z=p;return .54*x+.84*y+.38*z
faces=[]
def face(ps,col):faces.append((sum(depth(p) for p in ps)/len(ps),[proj(p) for p in ps],col))
def box(c,s,col):
 c=np.array(c); s=np.array(s)/2
 v=[c+s*np.array([x,y,z]) for x,y,z in [(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)]]
 for ids,k in [([0,1,5,4],.75),([1,2,6,5],.90),([2,3,7,6],.65),([3,0,4,7],.8),([4,5,6,7],1.15)]:face([v[i] for i in ids],tuple(min(255,int(a*k)) for a in col))
def tube(a,b,r,col,n=12):
 a=np.array(a,float);b=np.array(b,float);v=b-a;v/=np.linalg.norm(v)
 u=np.cross(v,[0,0,1] if abs(v[2])<.9 else [1,0,0]);u/=np.linalg.norm(u);w=np.cross(v,u)
 rings=[[p+r*(u*math.cos(i*2*math.pi/n)+w*math.sin(i*2*math.pi/n)) for i in range(n)] for p in [a,b]]
 for i in range(n):
  j=(i+1)%n;k=.68+.28*(1+math.cos(i*2*math.pi/n))/2
  face([rings[0][i],rings[0][j],rings[1][j],rings[1][i]],tuple(int(q*k) for q in col))
 face(rings[1],col)
def ik(r,z):
 z-=.65;c=np.clip((r*r+z*z-1.6**2-1.4**2)/(2*1.6*1.4),-1,1);b=-math.acos(c);a=math.atan2(z,r)-math.atan2(1.4*math.sin(b),1.6+1.4*math.cos(b));return a,b

def render(t):
 global faces;faces=[];im=Image.new('RGB',(W,H),'#0b1322');d=ImageDraw.Draw(im);idx=min(7,int(t//8));u=t%8;ch=chapters[idx]
 d.rounded_rectangle((550,115,1240,596),24,fill='#111f32')
 txt(d,40,28,'ARDUINO / ROBOTICS LAB',18,'#5de2c1');txt(d,977,30,'ANIMATED SIMULATION',16,'#99aec9')
 txt(d,40,125,ch[0],18,'#5de2c1');txt(d,40,175,ch[1],34);txt(d,40,224,ch[2],34)
 for i,line in enumerate(ch[3]):txt(d,40,301+i*36,line,20,'#b7c7dd')
 # 3D floor
 for q in np.arange(-3,3.1,.5):
  d.line([proj((q,-2.5,0)),proj((q,2.5,0))],fill='#21354b',width=1)
  d.line([proj((-3,q,0)),proj((3,q,0))],fill='#21354b',width=1)
 base=.1;a=1.15;b=-1.35;opening=.27;held=False;obj=(2.1,0,.16)
 wave=math.sin(u*math.pi/4)
 if idx==0:base=.6*math.sin(t*.5)
 if idx==1:base=wave*.95
 if idx==2:a=1.1+.32*wave
 if idx==3:b=-1.2+.5*wave
 if idx==4:opening=.18+.16*(1+math.sin(u*1.5))/2
 if idx==5:base=.45*wave;a=1.15+.1*wave
 if idx==6:
  # wrist approaches object, closes, lifts, rotates, lowers and releases
  keys=[(0,0,1.8,1.65,.36),(1.5,0,2.1,.48,.36),(2.2,0,2.1,.48,.17),(3.3,0,2.1,1.45,.17),(4.7,1.25,2.1,1.45,.17),(5.9,1.25,2.1,.48,.17),(6.6,1.25,2.1,.48,.36),(8,1.25,1.8,1.65,.36)]
  for f,k in zip(keys,keys[1:]):
   if f[0]<=u<=k[0]:
    v=smooth((u-f[0])/(k[0]-f[0]));base,r,z,opening=[f[j]+(k[j]-f[j])*v for j in range(1,5)];a,b=ik(r,z);break
  held=2.2<=u<5.9
  if u>=5.9:obj=(2.1*math.cos(1.25),2.1*math.sin(1.25),.16)
 if idx==7:base=.35*wave
 radial=np.array([math.cos(base),math.sin(base),0]);side=np.array([-math.sin(base),math.cos(base),0]);up=np.array([0,0,1]);p0=np.array([0,0,.65]);p1=p0+radial*1.6*math.cos(a)+up*1.6*math.sin(a);p2=p1+radial*1.4*math.cos(a+b)+up*1.4*math.sin(a+b)
 # industrial body, joints and parallel gripper
 box((0,0,.10),(1.25,1.10,.2),(71,88,111));tube([0,0,.2],[0,0,.58],.42,(62,79,101));tube(p0,p1,.16,(250,151,61));tube(p1,p2,.13,(250,151,61))
 for p,r in [(p0,.24),(p1,.20),(p2,.15)]:tube(p-side*.22,p+side*.22,r,(79,106,141))
 tube(p2-side*.36,p2+side*.36,.08,(183,203,221))
 for sign in [-1,1]:
  g=p2+side*opening*sign;tube(g,g-up*.32,.055,(202,217,234));tube(g-up*.32,g-up*.32-side*.07*sign,.05,(202,217,234))
 if held:obj=tuple(p2-up*.32)
 if idx in [0,6,7]:box(obj,(.28,.28,.30),(63,219,178))
 # destination pad
 box((2.1*math.cos(1.25),2.1*math.sin(1.25),.025),(.65,.65,.05),(33,124,126))
 for _,poly,col in sorted(faces,key=lambda q:q[0]):d.polygon(poly,fill=col)
 txt(d,576,552,'4 AXES  /  POSITIONAL SERVOS',16,'#88a4c5')
 if idx==5:
  d.rounded_rectangle((582,145,795,239),10,fill='#146779',outline='#4bc6c8',width=2)
  txt(d,601,154,'ARDUINO UNO',18);txt(d,601,207,'USB power + logic',16)
  d.rectangle((618,180,744,199),fill='#152536')
  for pin in range(9):d.rectangle((605+pin*19,232,612+pin*19,242),fill='#d9c68e')
  d.rounded_rectangle((958,145,1210,239),10,fill='#29374b',outline='#70859e',width=2)
  txt(d,976,155,'SERVO SUPPLY',18);txt(d,976,193,'Match voltage + current',16)
  d.ellipse((977,221,986,230),fill='#f17c64');d.ellipse((1190,221,1199,230),fill='#91a1b4')
  d.line([(680,245),(680,270),proj(p1)],fill='#5de2c1',width=3)
  d.line([(981,236),(981,267),proj(p0)],fill='#f17c64',width=3)
  d.line([(1194,237),(1194,280),(705,280),(705,244)],fill='#899bb2',width=2)
  txt(d,782,253,'COMMON GND',16,'#b4c6db')
  dot=(u*1.6)%1;target=proj(p1);sx,sy=680,270
  px=sx+(target[0]-sx)*dot;py=sy+(target[1]-sy)*dot
  d.ellipse((px-5,py-5,px+5,py+5),fill='#caffed')
 # joystick console
 for j,x in enumerate([115,285]):
  d.rounded_rectangle((x-55,410,x+55,513),16,fill='#1c3048',outline='#38516e',width=2)
  d.ellipse((x-31,429,x+31,491),fill='#0c1829',outline='#5c738d',width=2)
  dx=dy=0
  if (idx in [1,5] and j==0) or (idx==3 and j==1):dx=wave*20
  if (idx==2 and j==0) or (idx==4 and j==1):dy=wave*20
  d.line((x,460,x+dx,460+dy),fill='#8ba7c4',width=7);d.ellipse((x+dx-17,443+dy,x+dx+17,477+dy),fill='#5de2c1' if dx or dy else '#829bb6')
  txt(d,x-51,526,'JOYSTICK '+str(j+1),16,'#a3b8d2')
 if idx==5:
  txt(d,40,568,'2° steps • ~20 ms loop • hold at centre',18,'#5de2c1')
 else:txt(d,40,568,'Concept geometry • calibrate real joints',18,'#718cae')
 # two-line subtitle, readable on mobile
 import textwrap
 for i,s in enumerate(textwrap.wrap(ch[4],width=100)):txt(d,40,620+i*29,s,22,'#e0e9f5')
 d.rectangle((40,701,1240,705),fill='#26394f');d.rectangle((40,701,40+1200*t/64,705),fill='#5de2c1')
 txt(d,1160,80,f'{idx+1:02d} / 08',18,'#718cae')
 return im
if __name__=='__main__':
 for t in [3,12,20,28,36,44,51,55,60]:render(t).save(OUT/f'preview-{t}.jpg')
 proc=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-vcodec','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-an','-c:v','libx264','-preset','fast','-crf','25','-pix_fmt','yuv420p','-movflags','+faststart',str(OUT/'robotic-arm-explainer.mp4')],stdin=subprocess.PIPE)
 for f in range(64*FPS):proc.stdin.write(render(f/FPS).tobytes())
 proc.stdin.close();assert proc.wait()==0
 print(OUT/'robotic-arm-explainer.mp4')
