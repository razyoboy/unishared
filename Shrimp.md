ANSYS - TRUE SIMULATION PLATFORM 
======
So they say.

**NEEDS REPORT SEND IT TO JARN KUNG EMAIL (1-WEEK)**
* Show your results after simulation
* Explain your steps and stuffs
* No need for full formal cover, just throw in your name and your results and conclusion
    * Only one or two pages are fine 
* **_Screenshot is often more than enough_** and just a few explaination are extremely fine.
* Filename should be the student number 6213xxx

Now lets continue,

* ANSYS Fluent -> For CFD (Computational Fluid Dynamics) Simulation
* Where ANSYS Student is absolutely free.

**TYPES OF PROGRAMS**
----

* ROCKY -> For simulation of bulk object, either solid or liquid (Particle Simulation)
* MarkForged -> 3D Printer Line Ups

**ANSYS itself has many applications, those being;**
---
* Aerospace / Defense
* High Tech Electronics
* Healthcare and Biomedical Industries

We shall focus on the Healthcare part
* 80% of the top 50 healthcare companies used ANSYS, Johnson-Johnson, Moderna. (fuck China and your Sinovac bullshit)

By which these healthcare companies would simulate the Simulation Flight for the on-going COVID-19, which includes;
* Fitting the Facial Mask Properly
* General Flight Path of Airborne COVID-19 specimen
* Static Air Simulation of COVID-19 particles when sneezing

**ANSYS FLUENT INTRODUCTION**
===

What does Computational Fluid Dynamics (CFD) give you?
* Distribution of pressure, velocity, temperature, etc.
* Pressure drop, Flow rates, Forces like drift and drags.
* Distribution of multiple phases (Gas-Liquid, Gas-Solid, etc)
* Species Combustion (Reactions, Comnbustions, etc)

By which ANSYS CFD is based on (like every CFD) on the **_Finite Volume Method_**

CDF Workflow using ANSYS Fluent
---
* **Problem Identification**
    * Define Goals
    * Identify Domains
* **Preprocessing**
    * Geometry
    * Mesh
    * Physics and Solver Settings
* **Solve**
    * Compute Solution
* **Post Processing**
    * Examine Results

**ANSYS Meshing**

SpaceClaim -> CAD for ANSYS family of softwares, so you can use the damn thing directly.

Purpose of Meshing
* Equations are solved at the mesh node location, hence it is required.
* By which the parameters must be met as follows;
    * SKEWNESS = 0 - 0.94 is okay. (0 - 0.25 is the best)
    * ORTHOGONAL QUALITY = 0.15 - 1.00 is okay. (0.95 - 1.00 is the best)

**ANSYS Fluent**

Fluent supports the new GEKO model (Generalized k-Omega Model), which is created by ANSYS themselves lol.
For **_Multi-Phase Flow_** however, we either use Euler-Euler Models or Eular-Lagrane Method
