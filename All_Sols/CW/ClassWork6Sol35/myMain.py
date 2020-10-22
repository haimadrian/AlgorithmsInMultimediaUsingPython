__author__ = 'Dmitry Patashov'

from myFunctions import *

img = cv2.imread('img.jpg')

qn = 1

if qn == 1:

    im = img.copy()
    D = im.shape
    c = np.int64(np.asarray(D)[0:2] / 2.)
    w = np.int64(np.min(c) / 2.)

    im = GreenSqr(img, c, w)

    plt.figure()
    plt.imshow(im[:,:,::-1])
    plt.show()

elif qn == 2:

    s = [10, 13, 15, 100, 101, 102, 103, 104, 105, 107]

    im = QuadGreenSqr(img, s)

    plt.figure()
    plt.imshow(im[:,:,::-1])
    plt.show()

elif qn == 3:

    im = ColorShift(img)

    plt.figure()
    plt.imshow(im[:,:,::-1])
    plt.show()

elif qn == 4:

    im = myColorReplacement(img, 50, 100, 30, 250)

    plt.figure()
    plt.imshow(im[:,:,::-1])
    plt.show()

elif qn == 5:

    im = TwoLiner(img)

    plt.figure()
    plt.imshow(im[:,:,::-1])
    plt.show()

elif qn == 6:

    time = np.arange(0, 2*np.pi, 0.01)
    nSin1, fSin1, noise1 = NoisySin(time)
    nSin2, fSin2, noise2 = NoisySin(time, 'u')

    plt.figure()
    plt.subplot(221)
    plt.plot(time, fSin1, time, noise1)
    plt.legend(['Sin(t)','Gauss Noise'])
    plt.subplot(223)
    plt.plot(time, nSin1)
    plt.legend(['Noisy Sin G|N'])
    plt.subplot(222)
    plt.plot(time, fSin2, time, noise2)
    plt.legend(['Sin(t)', 'Uniform Noise'])
    plt.subplot(224)
    plt.plot(time, nSin2)
    plt.legend(['Noisy Sin U'])
    plt.show()

elif qn == 7:

    time = np.arange(0, 2*np.pi, 0.01)
    nSin, fSin, noise = NoisySin(time)

    filtSig = myMAF(nSin, 10)

    plt.figure()
    plt.subplot(211)
    plt.plot(time, nSin, time, filtSig)
    plt.legend(['Noisy signal', 'Filtered signal'])
    plt.subplot(212)
    plt.plot(time, fSin, time, filtSig)
    plt.legend(['Sin(t)', 'Filtered signal'])
    plt.show()

elif qn == 8:

    time = np.arange(0, 2*np.pi, 0.01)
    nSin, fSin, noise = NoisySin(time, 'u')

    filtSig = myMedFilt(nSin, 20)

    plt.figure()
    plt.subplot(211)
    plt.plot(time, nSin, time, filtSig)
    plt.legend(['Noisy signal', 'Filtered signal'])
    plt.subplot(212)
    plt.plot(time, fSin, time, filtSig)
    plt.legend(['Sin(t)', 'Filtered signal'])
    plt.show()

elif qn == 9:

    fsr, rs = wfl.read('rain.wav')
    fsw, ws = wfl.read('Walking.wav')

    L = np.min([len(ws), len(rs)])

    sig1 = rs[0:L,:]
    sig2 = ws[0:L].reshape(-1,1)

    def adjustSound(sig1, sig2, a1=1., a2=1.):
        newSig = np.round(a1*np.float64(sig1) + a2*np.float64(sig2))
        newSig[newSig > 32767] = 32767
        newSig[newSig < -32767] = -32767
        return np.int16(newSig)

    newSig0 = adjustSound(sig1, sig2)
    newSig1 = adjustSound(sig1, sig2, 2, 0.5)

    wfl.write('WalkingRain0.wav', fsr, newSig0)
    wfl.write('WalkingRain1.wav', fsr, newSig1)

    plt.figure()
    plt.subplot(221)
    plt.plot(sig2)
    plt.legend(['Walking (mono)'])
    plt.subplot(222)
    plt.plot(np.mean(sig1, 1))
    plt.legend(['Rain (mono)'])
    plt.subplot(212)
    plt.plot(np.mean(newSig0, 1))
    plt.legend(['Walking in the rain (mono)'])
    plt.show()
















