import numpy as np
from cycler import cycler
from bluesky.plans import scan_nd

def SWCarbon_acq(multiple,mesh,det,en):
    energies = np.arange(270,282,.5)
    energies = np.append(energies,np.arange(282,286,.1))
    energies = np.append(energies,np.arange(286,292,.2))
    energies = np.append(energies,np.arange(292,305,1))
    energies = np.append(energies,np.arange(305,320,1))
    energies = np.append(energies,np.arange(320,350,5))
    times = energies.copy()
    times[energies<282] = 1
    times[(energies < 286) & (energies >= 282)] = 5
    times[energies >= 286] = 2
    times *= multiple
   # print(times)
   # print(energies)
   # print(len(times))
   # print(len(energies))
    times2 = times.copy()
   # print(len(times2))

    yield from scan_nd(
        [mesh,det],
        cycler(det.saxs.cam.acquire_time, times) +
        cycler(mesh.parent.exposure_time, times2) +
        cycler(en, energies))


