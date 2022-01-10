# make version info json

import hashlib
import json


def getVersion():
    with open("version.json", "r", encoding="UTF-8") as f:
        v = json.load(f)
    return v


def calcPackageHash(versionobject):
    h = hashlib.sha1()
    path = "build\\nvda\\HISS-%s.zip" % versionobject["version"]
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def calcPatchHash(versionobject):
    h = hashlib.sha1()
    path = "build\\nvda\\HISS-%s.nvda-addon" % versionobject["version"]
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def save(jsonname, versionobject, packagehash, patchhash):
    newjson = {
        "version": versionobject["version"],
        "release_date": versionobject["release_date"],
        "package_hash": packagehash,
        "patch_hash": patchhash
    }
    with open(jsonname, "w", encoding="UTF-8") as f:
        json.dump(newjson, f)


versionobject = getVersion()
jsonname = "HISS-%s_info.json" % versionobject["version"]
packagehash = calcPackageHash(versionobject)
patchhash = calcPatchHash(versionobject)
save(jsonname, versionobject, packagehash, patchhash)
