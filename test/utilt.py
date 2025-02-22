import math
import cnc_figure_mover

def ras (x1, y1, x2, y2, x3, y3):
  if x1==x2:
    x1, y1 = y1, x1
    x2, y2 = y2, x2
    x3, y3 = y3, x3
  k=(y1-y2)/(x1-x2)
  d=y1-k*x1
  xz=(x3*x2-x3*x1+y2*y3-y1*y3+y1*d-y2*d)/(k*y2-k*y1+x2-x1)
  dl=-1
  if ( xz<=x2 and xz>=x1 ) or ( xz<=x1 and xz>=x2 ):
    dl=math.sqrt((x3-xz)*(x3-xz)+(y3-xz*k-d)*(y3-xz*k-d))
  return dl

def segment_dist(xa, ya, xb, yb, xc, yc, xd, yd):

  min_t=-1
  t=-2
  s=-2

  o=(xb-xa)*(-yd+yc)-(yb-ya)*(-xd+xc)
  o1=(xb-xa)*(yc-ya)-(yb-ya)*(xc-xa)
  o2=(-yd+yc)*(xc-xa)-(-xd+xc)*(yc-ya)

  if o!=0:
    t=o1/o
    s=o2/o

  if (t>=0 and s>=0) and (t<=1 and s<=1):
    min_t=0
  else:

    dl1=ras(xa,ya,xb,yb,xc,yc)
    min_t=dl1
    dl2=ras(xa,ya,xb,yb,xd,yd)
    if (dl2 < min_t and dl2 != -1) or min_t==-1 :
      min_t=dl2
    dl3=ras(xc,yc,xd,yd,xa,ya)
    if (dl3 < min_t and dl3 != -1) or min_t==-1 :
      min_t=dl3
    dl4=ras(xc,yc,xd,yd,xb,yb)
    if (dl4 < min_t and dl4 != -1) or min_t==-1 :
      min_t=dl4
    if min_t==-1 :
      dl1=math.sqrt((xa-xc)*(xa-xc)+(ya-yc)*(ya-yc))
      min_t=dl1
      dl2=math.sqrt((xb-xd)*(xb-xd)+(yb-yd)*(yb-yd))
      if dl2<min_t :
        min_t=dl2
      dl3=math.sqrt((xb-xc)*(xb-xc)+(yb-yc)*(yb-yc))
      if dl3<min_t :
        min_t=dl3
      dl4=math.sqrt((xa-xd)*(xa-xd)+(ya-yd)*(ya-yd))
      if dl4<min_t :
        min_t=dl4

  print (min_t)

  

  return min_t


segment_dist(166.509, 389.251, 1424.745, 512.012, 1383.610, 562.410, 57.012, 433.915)
segment_dist(1424.745, 110.088, 166.509, 232.916, 57.012, 187.972, 1383.610, 59.514)
