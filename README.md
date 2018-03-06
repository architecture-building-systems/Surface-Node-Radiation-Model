# Surface-Node-Radiation-Model
This simple script allows you to quickly calculate the heat transfer between two surface geometries:
- **Step 1** Read csv files describing the geometry of two surfaces, Surface 1 and 2.
- **Step 2** The surface meshes listed in the csv files are converted into 'sub-surfaces'. The Low, Medium and High resolution indicate the density of subsurfaces
- **Step 3** Using a simple 'double-area' formula, the form factor of the two surfaces is calculated
- **Step 4** The subsurfaces which cannot 'see' each other are blocked i.e. If a sub-surface from surface1 can not see a subsurface in surface2, this pair is not considered in the form factor calculation. For example, in the figure below, the 'red' sections of surface are completely blocked from the form factor calculation because they can't be 'seen' by the blue surface.
![image-title-here](/Images/Figure_1.png){:class="img-responsive"}
- **Step 5** A simple RC model incorporates the form factor and calculates the radiative fluxes between the two bodies and the convective fluxes between the bodies and the surrounding medium (air)

You can access the source script .pynb here
