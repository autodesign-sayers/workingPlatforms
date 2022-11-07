# **Working Platforms Automation**
Version 1.0 , Benjamin Sayers (Costain Automated Design)

Link to the Working Platform Tool on our SharePoint site <br/>
https://costaingroup.sharepoint.com/sites/DES/SitePages/Working-Platforms.aspx

## **Contents**
1. [Introduction](#introduction)
2. [Dependencies](#dependencies)
3. [Inputs](#inputs)
4. [Process](#process)
5. [Outputs](#outputs)
6. [User Guide](#user-guide)
   1. [Launch Application](#u10--launch-applicationu)
   2. [Import](#u20--import-tabu)
   3. [GA Plan](#u30--ga-plan-tabu)
   4. [Section](#u40--section-tabu)
   5. [Model](#u50--model-tabu)
   6. [Export](#u60--export-tabu)
   7. [Info](#u70--info-tabu)
7. [Further Development](#further-development)
8. [Known Issues](#known-issues)

--- 

## **Introduction**
This grasshopper scripts automates the design and drawing production of a singular working platform. It consumes a surface model and polygon and auto-generates a working platform design. The user has a number of user defined parameters available to further refine the design and drawing annotations. A python script is then run to generate a GA Plan and Section drawing which can be exported as PDF. The entire file can then be saved as a .dwg for import into other design software

This repository (repo) contains:
- A Rhino file that includes the required drawing templates.
- A Grasshopper file which automates the design and drawing production of a working platform.
- A Python file that is used for drawing automation.
- A CSV file that contains the format to upload SOP coordinates.
- A dependencies folder with the required plugins needed to run the software.


---

## **Dependencies**
For the Grasshopper script, you will need the following dependencies (included in repo folder):

*packageName, version, Link to webstore (e.g. Food4Rhino)*

- Pufferfish, Version=3.0.0.0, https://www.food4rhino.com/en/app/pufferfish
- HumanUI, Version=0.8.8.0, https://www.food4rhino.com/en/app/human-ui
- Human, Version=1.7.3.0, https://www.food4rhino.com/en/app/human
- MetaHopper, Version=1.2.4.0, https://www.food4rhino.com/en/app/metahopper
- EleFront_Beta, Version=5.0.0.0, https://www.food4rhino.com/en/app/elefront
- CORE.Grasshopper.Public, Version=1.9.6353, https://www.food4rhino.com/en/app/tt-toolbox

If a dependency is missing grasshopper will flag this up as a missing pacakge. If this is the case please get in contact so this can be rectified.

---

## **Inputs**
Required input files and geometry 

- Site terrain / topography file (.dwg / .dgn)
- Platform edge polygon
  - Manually drawn closed polygon
  - CSV file input with SOP coordinates using file in repo with correct data format (.csv)

---

## **Process**
Through a series of user input parameters the working platform is generated in real time and outputs drawings and a CAD file. See the user guide for more information. This process is handled by the grasshopper script in the background, made accessible by the UI and is displayed in the Rhino model window.

---

## **Outputs**
- 1 x GA Plan drawing (.pdf)
- 1 x Section drawing (.pdf)
- 1 x CAD file for import into other software (.dwg)

---

## **User Guide**

Follow the link for a video demonstration on our MS Stream site <br/>
https://web.microsoftstream.com/video/84120873-257a-4ad6-a30e-2aa85b31ce97

<br/>

*All slider inputs can be used by dragging the handle or double clicking and entering your parameter value.*

<br/>

*All slider inputs can be used by dragging the handle or double clicking and entering your parameter value.*

### <u>**1.0 | Launch Application**</u>
- Launch Rhino 7
- In Rhino, Open `AWP_Automated_Piling_Platforms.3dm`
- In the Rhino Command Line type
    ```
    Grasshopper
    ```
  and press `Enter`
- In Grasshopper, Open `AWP_Automated_Piling_Platforms.gh`

<br/>

### <u>**2.0 | Import Tab**</u>


<br/>

![Import Tab](media/Import.png?raw=true)

<br/>

#### **2.1 | Import DWG Topo Surface**
- Import your terrain / topo surface using the file picker
- Press `Import` button to import
- Press git update-ref -d MERGE_HEAD`Reset` button to delete an imported surface to reset and reimport a different file

#### **2.2 | Import DWG topo surface**
- Press `Draw Polyline` to manually draw a polyline for your platform edge
- Press `Select Manual Polyline` to select the manually drawn polyine as an input

#### **2.3 | Import SOP points from a CSV file**
- Press `Select SOP File (CSV)` to select a CSV file that contains SOP coordinates for your platform edge curve.
- **Please Note** you must use the csv format provided in the example file found in this repo

#### **2.4| Select your curve input**
- Select `Manually Drawnm Platform Edge Curve` to use a manually drawn polygon for your platform edge curve
- Select `CSV Import Platform Edge Curve` to use CSV imported coordinates for your platform edge curve

#### **2.5 | SOPs**
- Once your polyline has been selected the list of SOPs will be displayed here

#### **2.6 | Error message log**
- Any errors found in the current design will be flagged here

<br/>

### <u>**3.0 | GA Plan Tab**</u>

<br/>

![Plan Tab](media/Plan.png)

<br/>

#### **3.1 | Define edge zone width**
- Use the slider to define the edge zone width

#### **3.2 | Pick spot levels**
- Press `Create Spot Levels` and pick your spot level points in the model window.
- Press `Select Spot Level Locations` to select the spot level points previously defined in the model window.

<br/>

### <u>**4.0 | Section Tab**</u>

<br/>

![Section Tab](media/Section.png)

<br/>

#### **4.1 | Set Section Curves**
- Press `Create Section Location Point` and pick the centre point of the section plane in the model window.
- Press `Select Section Location Points` to select the section point previouslyd defined in the model window
- Use the slider to the rotation angle of the section plane

#### **4.2 | Annotation**
- Use the slider to define the dim leader length
  
#### **4.3 | Working Platform**
- Use the sliders to define the platform depth and hatch scale
  
#### **4.4 | Exclusion Zone**
- Use the sliders to define the edge zone dime height and leader length
  
#### **4.5 | Earthworks Hatch**
- Use the sliders to define the earthworks hatching radius and scale

#### **4.6 | Slope Gradient: 1 in X**
- In the text box enter your cut and fill earthworks gradient.

<br/>

### <u>**5.0 | Model Tab**</u>

<br/>

![Model Tab](media/Model.png)

<br/>

#### **5.1 | Earthworks Volumes**
- Toggle `Caluclate` to calculate the earthworks volumes for your design
- The Cut / Fill / Total volume will display below
- *PLASE NOTE: This may not work 100% of the time. This is under further development*

<br/>

### **<u>6.0 | Export Tab</u>**

<br/>

![Export Bake](media/Export-Bake.png)

<br/>

#### **6.1 | Bake Model**
- Press `Bake Geometry` to finalise your design and bake the geometry to the model window.

#### **6.2 | Drawings**
- Press `Create Drawing Sheets` and open `AWP_Create_Layouts.py` to run the drawing automation.

#### **6.3 | Export CSV Coordinates**
- Press `CSV File Path` and open a folder location to save your SOP CSV file to. In the dialogue box enter your file name.
- Select `Open`
- Press `Export` to export your SOP coordinates to your chosen CSV file location

<br/>

![Export Plan](media/Export-Plan.png)

<br/>

![Export Section](media/Export-Section.png)

<br/>

### <u>**7.0 | Info Tab**</u>
- For any issues, bugs or requirements please feel free to contact us with the information provided 

<br/>

---

<br/>

## **Further Development**
List Potential Further Developments (Planned & Potential)
To further improve the script, the following has been considered (but not at all tested) for the Proof of Concept. The followin should be included if funding is acquired:

- Integration with Tekla Tedds to run engineering calculations and provide calc sheet as an output for engineering checks
- Feedback engineering calc checks to user interface
- Calc sheet to inform platform thickness
- Load table to be included in drawing sheets
- Fall annotation
- Access ramp annotation
- Multiple polygons for multiple platforms
- Piling rig / equipment shown in drawing
- SOP annotation in section

<br/>

---

<br/>

## **Known Issues**

- Only one section can be created per design
- Only one polygon can be used at a time
- Auto scaling of text annotation isnt 100% accurate