# this analysis script finds the photons with the highest energy for the crab nebula from the 2FHL event list
from numpy import *


from astropy.io import fits
hdulist=fits.open('gll_psch_v08.fit.gz')
print hdulist.info()

datalist=hdulist[1]       #hdu=1 is the source catalog, found using "ftlist" or "hdulist.info()"

N=len(datalist.data)

print N

#loop over fermi 2FHL catalog 
for i in range(N+1):
    data= datalist.data[i-1]  # -1 otherwise it raises an error
    string =data['Source_Name']
    if (string=='2FHL J0534.5+2201'):
        x=data['RAJ2000']
        y=data['DEJ2000']
        print (x, y)     

        


from astropy.io import fits        
hdulist2=fits.open('2fhl_events.fits.gz')
print hdulist2.info()

datalist2=hdulist2[1] #hdu=1 is the event list 
data2=datalist2.data

N=len(datalist2.data)


#  prepare data
data2= datalist2.data
data2_x=data2['RA']
data2_y=data2['DEC']
data2_energy=data2['ENERGY']
r=sqrt(pow(data2_x-x,2)+pow(data2_y-y,2))

# initialize empty list for events
list = []
#loop over radii to find all events in a circle of 3 deg
for i in range(len(r)):
    if r[i] < 3:
        list.append(data2_energy[i])

print max(list)

a = sorted(list, reverse=True)

#finally print events with highest energies
print (a[1], a[2], a[3])
