import matplotlib.pyplot as plt

med_30 = [0, 0, 29, 59, 78, 59, 59, 59, 59, 59]
teo_30 = [0, 21, 73, 133, 172, 172, 133, 73, 21, 0]

med_40 = [0, 0, 59, 118, 118, 118, 118, 118, 118, 118]
teo_40 = [0, 36, 128, 233, 301, 301, 233, 128, 36, 0]

med_50 = [0, 10, 98, 206, 206, 196, 196, 196, 206, 206]
teo_50 = [0, 58, 206, 374, 484, 484, 374, 206, 58, 0]

med_60 = [0, 29, 196, 343, 343, 334, 334, 334, 343, 343]
teo_60 = [0, 85, 301, 547, 707, 707, 547, 301, 85, 0]

med_70 = [0, 59, 275, 451, 451, 432, 432, 432, 451, 451]
teo_70 = [0, 114, 402, 730, 944, 944, 730, 402, 114, 0]

med_80 = [0, 78, 353, 598, 589, 579, 589, 589, 598, 598]
teo_80 = [0, 149, 526, 954, 1234, 1234, 954, 526, 149, 0]

med_90 = [0, 98, 451, 746, 746, 726, 726, 726, 746, 746]
teo_90 = [0, 182, 642, 1165, 1506, 1506, 1165, 642, 182, 0]

med_100 = [0, 98, 510, 746, 746, 726, 736, 736, 765, 765]
teo_100 = [0, 208, 735, 1334, 1725, 1725, 1334, 735, 208, 0]

gr = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180]

plt.figure()
plt.plot(gr, med_30)
plt.plot(gr, teo_30)
plt.xlabel("theta")
plt.ylabel("pressão")
plt.show()

plt.figure()
plt.plot(gr, med_40)
plt.plot(gr, teo_40)
plt.xlabel("theta")
plt.ylabel("pressão")
plt.show()

plt.figure()
plt.plot(gr, med_50)
plt.plot(gr, teo_50)
plt.xlabel("theta")
plt.ylabel("pressão")
plt.show()

plt.figure()
plt.plot(gr, med_60)
plt.plot(gr, teo_60)
plt.xlabel("theta")
plt.ylabel("pressão")
plt.show()

plt.figure()
plt.plot(gr, med_70)
plt.plot(gr, teo_70)
plt.xlabel("theta")
plt.ylabel("pressão")
plt.show()

plt.figure()
plt.plot(gr, med_80)
plt.plot(gr, teo_80)
plt.xlabel("theta")
plt.ylabel("pressão")
plt.show()

plt.figure()
plt.plot(gr, med_90)
plt.plot(gr, teo_90)
plt.xlabel("theta")
plt.ylabel("pressão")
plt.show()

plt.figure()
plt.plot(gr, med_100)
plt.plot(gr, teo_100)
plt.xlabel("theta")
plt.ylabel("pressão")
plt.show()
