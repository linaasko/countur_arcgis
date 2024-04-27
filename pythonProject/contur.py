import arcpy
inraster = arcpy.GetParameterAsText(0)
if inraster == '#' or not inraster:
    inraster = r"E:\university\3 course\programming in gis\lections\arcpy, pr5\Lesson1\Lesson1\foxlake"

outcontur = arcpy.GetParameterAsText(1)
if outcontur == '#' or not outcontur:
    outcontur = r"E:\university\3 course\programming in gis\lections\arcpy, pr5\Lesson1\Lesson1\countur.shp"
import arcpy
inraster = arcpy.GetParameterAsText(0)
if inraster == '#' or not inraster:
    inraster = r"E:\university\3 course\programming in gis\lections\arcpy, pr5\Lesson1\Lesson1\foxlake"

outcontur = arcpy.GetParameterAsText(1)
if outcontur == '#' or not outcontur:
    outcontur = r"E:\university\3 course\programming in gis\lections\arcpy, pr5\Lesson1\Lesson1\countur.shp"
contour_interval = arcpy.GetParameterAsText(2)
if contour_interval == '#' or not contour_interval:
    contour_interval = '25'
if float(contour_interval) <= 0:
    raise Exception('height value is not suitable for contour construction')
