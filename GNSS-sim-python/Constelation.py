import datetime
import numpy as np
import RINEX
import Satallite

class Constelation:

    prefix = ""
    RINEXDataRecordDesciption = []
    RINEXheaderDescription = []
    postProcessRINAXData = lambda data, header: None
    getSatPosVel = lambda eph, t : (np.zeros(1,3), np.zeros(1,3))

    bitsPerFrame = -1

    utcToConstelationTime = lambda t : t
    checkEphemeris = lambda self, eph, t : eph
    clockCorection = lambda self, eph, syncTime: syncTime
    timeDifference = lambda self, t1, t2: 0
    travelTimeCorection = lambda self, eph, satPos, userPos, t: 0

    fillBuffer = lambda self, t, sat, sats : [0, 1]

    getIdString = lambda self, eph : eph["name"]

    getSetupHeader = lambda sats : ""

    def addTimeStamp(self, ephList):
        for eph in ephList:
            eph["datetime"] = datetime.datetime(eph["year"], eph["month"], eph["day"], eph["hour"], eph["minute"], eph["second"])

    def ephsToSats(self, ephList):
        ephPerSat = {}
        for eph in ephList:
            if eph["name"] not in ephPerSat:
                ephPerSat[eph["name"]] = []
            ephPerSat[eph["name"]].append(eph)
        sats = {}
        for name in ephPerSat:
            sats[name] = Satallite.Satallite(name, self, ephPerSat[name])
        return sats

    def loadSatsFromRinax(self, filename):
        ephList, headerData = RINEX.parseRINEX(filename, self.RINEXDataRecordDesciption, self.RINEXheaderDescription, self.prefix)
        newList = self.postProcessRINAXData(ephList, headerData)
        ephList = newList if newList is not None else ephList
        self.addTimeStamp(ephList)
        sats = self.ephsToSats(ephList)
        return sats, headerData

def loadSats(files: list[tuple[Constelation, str]]):
    sats = {}
    constSats = {}
    consts : list[Constelation] = []
    for file in files:
        newSats, _ = file[0].loadSatsFromRinax(file[1])
        for sat in newSats:
            if sat in sats:
                sats[sat].add(newSats[sat])
            else:
                sats[sat] = newSats[sat]
            if file[0].prefix not in constSats:
                constSats[file[0].prefix] = {}
                consts.append(file[0])
            constSats[file[0].prefix][sat] = sats[sat]

    setup = "setup"
    for const in consts:
        setup = setup+" "+const.getSetupHeader(constSats[file[0].prefix])

    return sats, setup
