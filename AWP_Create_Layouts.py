import rhinoscriptsyntax as rs
import time

#Drawing template sizes
A1 = (841, 594)
A2 = (594, 420)
A3 = (420, 297)

#drawing scales
#1:1 1:2 1:20 1:5 1:10 1:50 1:100 1:200 1:500 1:1000 1:1250 1:2500 1:5000
scale = [0, 0.001, 0.002, 0.005, 0.01, 0.05, 0.1, 0.2, 0.5, 1, 1.25, 2.5, 5]

class Layout:
    
    layout_list = []
    if layout_list:
        print layout_list
    
    def __init__(self, title, size, layer):
        self.title = title
        self.size = size
        self.layer = layer
        self.layout_list.append(self)
        
    def addLayout(self):
        title = self.title
        size = self.size
        
        #create new layout
        layout_id = rs.AddLayout(title, size)
        self.layout_id = layout_id
        
        if layout_id:
            #change to new layout
            rs.CurrentView(title)
            #add detail view
            detail_id = rs.AddDetail(layout_id, (10,10), (291.5,287), None, 1)
            self.detail_id = detail_id
            #wait
            time.sleep(0.5)
            #insert drawing template
            if title == "Section":
                rs.InsertBlock("Section-A3", (0,0,0), (1,1,1))
            elif title == "Plan":
                rs.InsertBlock("Plan-A3", (0,0,0), (1,1,1))
            else:
                pass
        
        
    def scaleDetailView(self):
        layer = self.layer
        layout_id = self.layout_id
        detail_id = self.detail_id
                
        #get objects by layer
        if layer == "Section":
            obj = rs.ObjectsByLayer(layer, True)
            section_dim_obj = rs.ObjectsByLayer("SectionLeader", True)
        elif layer == "Plan":
            obj = rs.ObjectsByLayer(layer, True)
        
        #find object extents bbox
        box = rs.BoundingBox(obj)
        print box
            
        bbox_0 = str(box[0])
        bbox_2 = str(box[2])
        
        bbox_0 = bbox_0.split(",")
        bbox_2 = bbox_2.split(",")
        
        #get layer model extents 
        x_extents = float(bbox_2[0]) - float(bbox_0[0])
        y_extents = float(bbox_2[1]) - float(bbox_0[1])
        
        #detail view extents in layout
        detail_extents_x = 281.5
        detail_extents_y = 277
        
        #get rhino detail scale
        detail_scale_x = x_extents / detail_extents_x
        detail_scale_y = y_extents / detail_extents_y
        
        #get max scale extents
        xy_scales = [detail_scale_x, detail_scale_y]
        detail_scale = max(xy_scales)
        
        #hide in detail & zoom extents
        rs.CurrentDetail(layout_id, detail_id)
        rs.InvertSelectedObjects()
        rs.Command("_HideInDetail")
        rs.ZoomBoundingBox(box)
        
        #set detail scale to nearest upper scale range
        for i in range(len(scale)):
            if detail_scale <= 5:
                if scale[i]<detail_scale<=scale[i+1]:
                    #print(scale[i+1])
                    rs.DetailScale(detail_id, scale[i+1], 1)
                else:
                    pass
            else:
                pass
                #print(detail_scale)

def addSOPDetail():
    #find object extents bbox
    sop_table = rs.ObjectsByLayer("SOP", True)
    sop_box = rs.BoundingBox(sop_table)

    bbox_0 = str(sop_box[0])
    bbox_2 = str(sop_box[2])

    bbox_0 = bbox_0.split(",")
    bbox_2 = bbox_2.split(",")
    
    #get detail extents
    sop_x = float(bbox_2[0]) - float(bbox_0[0])
    sop_y = float(bbox_2[1]) - float(bbox_0[1])
    
    #add & scale detail to plan drawing sheet 
    rs.CurrentView("Plan")
    sop_detail_id = rs.AddDetail(planLayout.layout_id, (291.5 - sop_x, (287 - sop_y)), (291.5, 287), None, 1)
    rs.DetailScale(sop_detail_id, 0.7, 1)
    rs.CurrentDetail(planLayout.layout_id, sop_detail_id, True)
    rs.ZoomBoundingBox(sop_box)
    
    #hide everything else in detail view
    rs.InvertSelectedObjects()
    rs.Command("_HideInDetail")
    rs.UnselectAllObjects()
    rs.DetailLock(sop_detail_id, True)

#create new Layout instance
sectionLayout = Layout("Section", A3, "Section")
#add new layout for instance
sectionLayout.addLayout()
#scale detail view for instance
sectionLayout.scaleDetailView()

#deselet all objects
rs.UnselectAllObjects()

#create new Layout instance
planLayout = Layout("Plan", A3, "Plan")
#add new layout for instance
planLayout.addLayout()
#scale detail view for instance
planLayout.scaleDetailView()

#deselect all objects
rs.UnselectAllObjects()

#add SOP Detail to Plan Layout
addSOPDetail()

#def exportLayout(title):
#    rs.CurrentView(title)
#    rs.AllObjects(True)
#    rs.Command("Export")

#Export both layouts to .dwg
#exportLayout("Plan")
#exportLayout("Section")

#print both layouts to .pdf
#rs.Command("Print")



#sop_table = rs.ObjectsByLayer("SOP", True)
#
#if sop_table:
#    box = rs.BoundingBox(sop_table)
#    if box:
#        for i, point in enumerate(box):
#            rs.AddTextDot( i, point )
#
#rs.ZoomBoundingBox(box, "Top", False)

