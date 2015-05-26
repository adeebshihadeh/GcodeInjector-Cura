#Name: Gcode Injector (Layer)
#Info: Inject Gcode at a layer
#Depend: GCode
#Type: postprocess
#Param: layerNum(string:) Layer Number
#Param: userGcode(string:) GCode to insert (use , for new lines)

print "Layer Num: " + layerNum
print "Insert gcode: " + userGcode

targetLayer = ";LAYER:" + layerNum
print "Target Layer: " + targetLayer

# Read the file into the lines variable
with open(filename, "r") as r:
    lines = r.readlines()

with open(filename, "w") as f:
    for line in lines:
        f.write(line)
        if line.find(targetLayer) != -1:
            f.write(";Begin modified gcode\n")
            f.write(userGcode.replace(",", "\n") + "\n")
            f.write(";End modified gcode\n")
            print "found it"