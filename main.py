# SPDX-License-Identifier: MIT
import json,os,urllib.request as u
U=os.environ["MAKEFUN_ENV_URL"]
V=0,100,320,330,500,900,0
W=0,2,6,4,2,2,-4
J=-33,-31,-18,-14,14,18,31,33
D=-17,-15,15,17
R=-16,-1,1,16
G=D+R
H={7:1,0:2,119:4,112:8}
Z={'K':1,'Q':2,'k':4,'q':8}
SQ=[i for i in range(128) if not i&0x88]
PT={2:(J,0),6:(G,0),3:(D,1),4:(R,1),5:(D+R,1)}
M=1e5
B=[0]*128
S=1;A=0;E=-1;K=4;C=116
T=[]
L=[0]*64
N=[0];F=[0]
def X(a,b):return ord(a)-97+(int(b)-1)*16
def Y(x,y):B[y]=B[x];B[x]=0
def p(f):
 global S,A,E,K,C
 q=112
 z=f.split();B[:]=[0]*128
 for c in z[0]:
  if c=='/':q-=24
  elif c.isdigit():q+=int(c)
  else:
   v='PNBRQKpnbrqk'.find(c)
   B[q]=v+1 if v<6 else 5-v
   if v==5:K=q
   elif v==11:C=q
   q+=1
 S=1 if z[1]=='w' else -1
 A=0
 for c in z[2]:A|=Z.get(c,0)
 E=-1 if z[3]=='-' else X(z[3][0],z[3][1])
def m(m2):
 global S,A,E,K,C
 f,t,r=m2
 c=B[f];v=B[t];s=t
 if abs(c)==1 and t==E and not v:
  s=t-16*S;v=B[s];B[s]=0
 T.append((m2,v,s,A,E,K,C))
 B[t]=r*S if r else c;B[f]=0
 if abs(c)==6:
  if abs(t-f)==2:
   a=t+1 if t>f else t-2;b=t-1 if t>f else t+1;Y(a,b)
  if c>0:K=t;A&=~3
  else:C=t;A&=~12
 A&=~(H.get(f,0)|H.get(t,0))
 E=(f+t)//2 if abs(c)==1 and abs(t-f)==32 else -1
 S=-S
def n():
 global S,A,E,K,C
 m2,v,s,a,e,w,k=T.pop()
 f,t,r=m2
 c=B[t]
 if abs(c)==6 and abs(t-f)==2:
  d=t+1 if t>f else t-2;b=t-1 if t>f else t+1;Y(b,d)
 B[f]=-S if r else c
 B[t]=0
 if v:B[s]=v
 A,E,K,C=a,e,w,k
 S=-S
def Q(s,y):
 for q in (s-15*y,s-17*y):
  if not q&0x88 and B[q]==y:return 1
 for O,v in ((J,2),(G,6)):
  for o in O:
   q=s+o
   if not q&0x88 and B[q]==v*y:return 1
 for d in D+R:
  q=s+d
  while not q&0x88:
   v=B[q]
   if v:
    if v==5*y or v==(3 if d in D else 4)*y:return 1
    break
   q+=d
 return 0
def g(cp):
 z=[];A2=z.append;P7=1+5*(S>0)
 for i in SQ:
  p2=B[i]
  if p2*S<=0:continue
  x=abs(p2);r=i>>4
  if x==1:
   d=16*S;t=i+d
   if not B[t] and not cp:
    A2((i,t,5 if r==P7 else 0))
    if r==7-P7:
     t2=i+2*d
     if not B[t2]:A2((i,t2,0))
   for j in (d-1,d+1):
    t=i+j
    if t&0x88:continue
    if B[t]*S<0 or t==E:A2((i,t,5 if r==P7 else 0))
  else:
   O,sl=PT[x]
   for d in O:
    t=i+d
    while not t&0x88:
     v=B[t]
     if not v:
      if not cp:A2((i,t,0))
     elif v*S<0:A2((i,t,0));break
     else:break
     if not sl:break
     t+=d
   if x==6 and i==(4 if S>0 else 116) and not cp:
    for kt,rf,bb in ((i+2,i+3,1),(i-2,i-4,2)):
     bb*=1 if i==4 else 4
     if A&bb and B[rf]==4*S and not any(B[q] for q in range(min(i,rf)+1,max(i,rf))) and not any(Q(q,-S) for q in (i,(i+kt)//2,kt)):A2((i,kt,0))
 return z
def e():
 s=0
 for i in SQ:
  p2=B[i]
  if not p2:continue
  x=abs(p2);f=i&7;r=i>>4
  v=V[x]+W[x]*(6-abs(2*f-7)-abs(2*r-7))
  if x==1:v+=10*(r if p2>0 else 7-r)
  s+=v if p2>0 else -v
 return s*S
def o(z,pl):
 def k(m2):
  f,t,r=m2;v=B[t]
  return 10000+V[abs(v) if v else 1]*10-V[abs(B[f])] if v or (abs(B[f])==1 and t==E) else 2000 if m2==L[pl] else 0
 z.sort(key=k,reverse=True)
 return z
def s(d,a,b,pl):
 N[0]+=1
 if N[0]>2e5:
  F[0]=1;return 0
 h=Q(K if S>0 else C,-S)
 if h and d>0 and pl<24:d+=1
 if d<=0 and not h:
  v=e()
  if v>=b:return b
  if v>a:a=v
  if d<=-6:return a
 q=d<=0 and not h
 z=g(q)
 z=o(z,pl);y=a if q else -M+pl;n2=0
 for m2 in z:
  f,t2,r=m2
  m(m2)
  if Q(K if S<0 else C,S):n();continue
  n2+=1
  v=-s(d-1,-b,-a,pl+1)
  n()
  if F[0]:return 0
  if v>y:y=v
  if v>a:a=v
  if a>=b:L[pl]=m2;return b
 if not n2:return -M+pl if h else a if d<=0 else 0
 return y
def h(legal):
 N[0]=0;F[0]=0
 z=[];mp={}
 for y in legal:
  f=X(y[0],y[1]);t=X(y[2],y[3])
  r=(0,5,4,3,2)[' qrbn'.find(y[4:])]
  mp[(f,t,r)]=y;z.append((f,t,r))
 b=z[0];z=o(z,0)
 for d in range(1,8):
  a=-M;c=M;e2=b;v2=-M
  for m2 in z:
   m(m2)
   v=-s(d-1,-c,-a,0)
   n()
   if F[0]:break
   if v>v2:v2=v;e2=m2
   if v>a:a=v
  if F[0]:break
  b=e2;z.remove(b);z.insert(0,b)
 return mp[b]
d=lambda p2,b2:json.load(u.urlopen(U+p2,json.dumps(b2).encode()))
def main():
 while (g2:=d('/game',{}))['status']>'e':
  while g2['status']=='your_move':
   p(g2['fen']);g2=d('/move',{'game':g2['game'],'move':h(g2['legal_moves'])})
main()
