import cadquery as cq

print(cq.Workplane('XY').box(1,2,3).toSvg())
