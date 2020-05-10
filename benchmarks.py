import numpy as np
import math

def prod( it ):
    p= 1
    for n in it:
        p *= n
    return p

def Ufun(x,a,k,m):
    y=k*((x-a)**m)*(x>a)+k*((-x-a)**m)*(x<(-a))
    return y
    
def fitness( x, dimensions, f ):
    
    if f == 1:
        ans=np.sum(x**2)
        return ans
   
    if f == 2:
        ans=sum(abs(x))+prod(abs(x))
        return ans

    if f == 3:
        dimensions=len(x)+1
        ans=0
        for i in range(1,dimensions):
            ans=ans+(np.sum(x[0:i]))**2
            return ans

    if f == 4:
        ans =max(abs(x))
        return ans
    
    if f==5:
        dimensions=len(x)
        ans=np.sum(100*(x[1:dimensions]-(x[0:dimensions-1]**2))**2+(x[0:dimensions-1]-1)**2);
        return ans
    
    if f == 6:
        ans=np.sum(abs((x+.5))**2)
        return ans
   
    if f==7:
        dimensions=len(x)
        w=[i for i in range(len(x))]
        for i in range(0,dimensions):
            w[i]=i+1;
            ans=np.sum(w*(x**4))+np.random.uniform(0,1)
            return ans
    
    if f==8:
        ans=sum(-x*(np.sin(np.sqrt(abs(x)))))
        return ans
    
    if f==9:
        dimensions=len(x)
        ans=np.sum(x**2-10*np.cos(2*math.pi*x))+10*dimensions
        return ans
    
    if f==10:
        dimensions=len(x)
        ans=-20*np.exp(-.2*np.sqrt(np.sum(x**2)/dimensions))-np.exp(np.sum(np.cos(2*math.pi*x))/dimensions)+20+np.exp(1)
        return ans
 
    if f==11:
        dimensions=len(x)
        w=[i for i in range(len(x))]
        w=[i+1 for i in w]
        ans=np.sum(x**2)/4000-prod(np.cos(x/np.sqrt(w)))+1
        return ans
    
    if f==12:
        dimensions=len(x);
        ans=(math.pi/dimensions)*(10*((np.sin(math.pi*(1+(x[0]+1)/4)))**2)+np.sum((((x[1:dimensions-1]+1)/4)**2)*(1+10*((np.sin(math.pi*(1+(x[1:dimensions-1]+1)/4))))**2))+((x[dimensions-1]+1)/4)**2)+np.sum(Ufun(x,10,100,4))   
        return ans
    
    if f==13:
        dimensions=len(x)
        ans=.1*((np.sin(3*math.pi*x[1]))**2+sum((x[0:dimensions-2]-1)**2*(1+(np.sin(3*math.pi*x[1:dimensions-1]))**2))+ 
    ((x[dimensions-1]-1)**2)*(1+(np.sin(2*math.pi*x[dimensions-1]))**2))+np.sum(Ufun(x,5,100,4));
        return ans
    
    if f==14:
        aS=[[-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32],[-32,-32,-32,-32,-32,-16,-16,-16,-16,-16,0,0,0,0,0,16,16,16,16,16,32,32,32,32,32]]
        aS=np.asarray(aS)
        bS =np.zeros(25)
        v=np.matrix(x)
        for i in range(0,25):
            H=v-aS[:,i]
            bS[i]=np.sum((np.power(H,6)))  
            w=[i for i in range(25)]   
            for i in range(0,24):
                w[i]=i+1
                ans=((1./500)+np.sum(1./(w+bS)))**(-1)
                return ans
    
    if f==15:
        aK=[.1957,.1947,.1735,.16,.0844,.0627,.0456,.0342,.0323,.0235,.0246]
        bK=[.25,.5,1,2,4,6,8,10,12,14,16]
        aK=np.asarray(aK)
        bK=np.asarray(bK)
        bK = 1/bK
        ans=np.sum((aK-((x[0]*(bK**2+x[1]*bK))/(bK**2+x[2]*bK+x[3])))**2)
        return ans
    
    if f==16:
        ans=4*(x[0]**2)-2.1*(x[0]**4)+(x[0]**6)/3+x[0]*x[1]-4*(x[1]**2)+4*(x[1]**4)
        return ans

    if f==17:
        ans=(x[1]-(x[0]**2)*5.1/(4*(np.pi**2))+5/np.pi*x[0]-6)**2+10*(1-1/(8*np.pi))*np.cos(x[0])+10
        return ans
    
    if f==18:
        ans=(1+(x[0]+x[1]+1)**2*(19-14*x[0]+3*(x[0]**2)-14*x[1]+6*x[0]*x[1]+3*x[1]**2))*(30+(2*x[0]-3*x[1])**2*(18-32*x[0]+12*(x[0]**2)+48*x[1]-36*x[0]*x[1]+27*(x[1]**2)))
        return ans
    if f==19:
        aH=[[3,10,30],[.1,10,35],[3,10,30],[.1,10,35]]
        aH=np.asarray(aH)
        cH=[1,1.2,3,3.2]
        cH=np.asarray(cH)
        pH=[[.3689,.117,.2673],[.4699,.4387,.747],[.1091,.8732,.5547],[.03815,.5743,.8828]];
        pH=np.asarray(pH)
        ans=0
        for i in range(0,4):
            ans=ans-cH[i]*np.exp(-(np.sum(aH[i,:]*((x-pH[i,:])**2))))  
        return ans
    if f==20:
        aH=[[10,3,17,3.5,1.7,8],[.05,10,17,.1,8,14],[3,3.5,1.7,10,17,8],[17,8,.05,10,.1,14]]
        aH=np.asarray(aH)
        cH=[1,1.2,3,3.2]
        cH=np.asarray(cH)
        pH=[[.1312,.1696,.5569,.0124,.8283,.5886],[.2329,.4135,.8307,.3736,.1004,.9991],[.2348,.1415,.3522,.2883,.3047,.6650],[.4047,.8828,.8732,.5743,.1091,.0381]]
        pH=np.asarray(pH)
        ans=0
        for i in range(0,4):
            ans=ans-cH[i]*np.exp(-(np.sum(aH[i,:]*((x-pH[i,:])**2))))
        return ans
    
    if f==21:
        aSH=[[4,4,4,4],[1,1,1,1],[8,8,8,8],[6,6,6,6],[3,7,3,7],[2,9,2,9],[5,5,3,3],[8,1,8,1],[6,2,6,2],[7,3.6,7,3.6]]
        cSH=[.1,.2,.2,.4,.4,.6,.3,.7,.5,.5]
        aSH=np.asarray(aSH)
        cSH=np.asarray(cSH)
        fit=0
        for i in range(0,4):
            v=np.matrix(x-aSH[i,:])
            fit=fit-((v)*(v.T)+cSH[i])**(-1)
            ans=fit.item(0)
        return ans
    
    if f==22:
        aSH=[[4,4,4,4],[1,1,1,1],[8,8,8,8],[6,6,6,6],[3,7,3,7],[2,9,2,9],[5,5,3,3],[8,1,8,1],[6,2,6,2],[7,3.6,7,3.6]]
        cSH=[.1,.2,.2,.4,.4,.6,.3,.7,.5,.5]
        aSH=np.asarray(aSH)
        cSH=np.asarray(cSH)
        fit=0
        for i in range(0,6):
            v=np.matrix(x-aSH[i,:])
            fit=fit-((v)*(v.T)+cSH[i])**(-1)
            ans=fit.item(0)
        return ans
    if f==23:
        aSH=[[4,4,4,4],[1,1,1,1],[8,8,8,8],[6,6,6,6],[3,7,3,7],[2,9,2,9],[5,5,3,3],[8,1,8,1],[6,2,6,2],[7,3.6,7,3.6]]
        cSH=[.1,.2,.2,.4,.4,.6,.3,.7,.5,.5]
        aSH=np.asarray(aSH)
        cSH=np.asarray(cSH)
        fit=0
        for i in range(0,9):
            v=np.matrix(x-aSH[i,:])
            fit=fit-((v)*(v.T)+cSH[i])**(-1)
            ans=fit.item(0)
        return ans
        
        