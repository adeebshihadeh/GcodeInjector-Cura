#Name: Gcode Injector (Height)
#Info: Inject gcode at a particular height
#Depend: GCode
#Type: postprocess
#Param: height(string:) Height (in mm)
#Param: userGcode(string:) GCode to insert (use , for new lines)

print "Height: " + height
print "Insert gcode: " + userGcode

targetHeight = "Z" + height
print "Height " + targetHeight

# Read the file into the lines variable
with open(filename, "r") as r:
    lines = r.readlines()

with open(filename, "w") as f:
    for line in lines:
        f.write(line)
        if line.find(targetHeight) != -1:
            f.write(";Begin modified gcode\n")
            f.write(userGcode.replace(",", "\n") + "\n")
            f.write(";End modified gcode\n")
            print "found it"