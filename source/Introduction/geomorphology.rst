GEOMOPHOLOGY
=============

Introduction
============

Coastal Zone
-------------

According to the ICZM Protocol, the coastal zone is defined as 'a geomorphologic area either side of the seashore in which the interaction between the marine and land parts occurs in the form of complex ecological and resource systems made up of biotic and abiotic components co-existing and interacting with human communities and relevant socio-economic activities.' The shore is comprised of the backshore and foreshore. The backshore, itself, is essentially comprised of a berm, which is a gently sloping dry portion of the beach.

Tidal fluctuation causes the shoreline to migrate back and forth within the shore range, forming longshore bars near the low tide breaker line. The longshore bar demarcates the region between the nearshore zone and offshore region.

.. figure:: fig1.png
   :alt: Classification of the coastal region

Types of Reefs
-------------

The Indian Ocean Islands investigated are protected by coral reef systems. These are mainly grouped into 3 main types:

Fringing Reef
^^^^^^^^^^^^^^

Typically occur adjacent to land, with little or no separation from the shore and forms a shallow lagoon.

Barrier Reef
^^^^^^^^^^^^

Broader and separated from land by a lagoon extending some kilometers wide. These extend as a broken, irregular ring around the coast or an island, running almost parallel to it.

Atoll Reef
^^^^^^^^^^^^

An atoll is a roughly circular (annular) oceanic reef system surrounding a large (and often deep) central lagoon.

.. figure:: fig2.png
   :alt: Structure of a fringing reef system

Reef Zonation and Geomorphic Classes
------------------------------------

The reef area is comprised of:

Terrestrial Reef Flat
^^^^^^^^^^^^^^^^^^^^

Broad, flat, shallow to semi-exposed area attached to land at one side, and subject to freshwater run-off, nutrients, and sediment.

Lagoon
^^^^^^

Sheltered, flat-bottomed sediment-dominated area (shallow < 5m; Deep >5m).

Inner Reef Flat
^^^^^^^^^^^^^^

Low energy, sediment-dominated, horizontal to gently sloping platform.

Outer Reef Flat
^^^^^^^^^^^^^^

A near horizontal, broad, and shallow platform which dissipates a significant portion of the remaining wave energy.

Reef Crest
^^^^^^^^^^

It is the highest point of the reef, generally shallow and characterized by the highest wave energy absorbance.

Reef Slope
^^^^^^^^^^

Reef slope is a submerged, sloping area extending seaward from the reef crest.

Plateau
^^^^^^^

Deeper submerged (> 5 m), hard-bottomed, horizontal to gently sloping (<10°), seaward facing reef platform.

In contrast to the fringing reef in figure 2 above, the barrier reef has a deeper lagoon section and an extended reef structure. This is depicted in figure 3 below.

.. figure:: fig3.png
   :alt: Structure of a barrier reef system

Coastal Landform
----------------

The coastal landform comprises a diverse range of ecosystems and morphologies. These include:

Beach and Dune System
^^^^^^^^^^^^^^^^^^^^^^

The beach comprises the foreshore and backshore, while the dune comprises the fixed, the shifting, and the embryonic dunes.

Muddy Shoreline
^^^^^^^^^^^^^^^

Present as tidal mud flats, they are composed of silt, clay, or fine sand. These generally form where tidal current velocities are too weak to resuspend completely the mud.

Rocky Shoreline
^^^^^^^^^^^^^^

These originate from the rapid cooling and hardening of volcanic lava outflows into the sea. A rocky shore is an intertidal area of seacoasts where solid rock predominates. They are mostly basaltic in nature.

Cliffs
^^^^^^

It is a high area of rock with a very steep side, at the edge of the sea. Cliffs are formed as erosion landforms due to the processes of erosion and weathering.

Saltmarshes (Coastal Wetland)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Saltmarshes are coastal wetlands dominated by high vegetation that are periodically inundated by saltwater. They are marshy because the soil may be composed of deep mud and peat (plant matter in decomposition).

Cobble/Shingle Beach
^^^^^^^^^^^^^^^^^^^^

These occur principally on high wave energy shores and originate from cliff erosion of moderate to strong bedrock. Generally, cobble beaches are much steeper than sandy beaches and provide natural defense to shore.

Calcareous Limestone Shore
^^^^^^^^^^^^^^^^^^^^^^^^^^

It is a carbonate sedimentary rock essentially composed of minerals calcite and aragonite (formed by the fragmentation of shell, coral, algal, and other organic debris).

Estuary
^^^^^^^

An estuary is a partially enclosed area of water on the coast where saltwater from the sea mixes with fresh water from rivers and streams.

Benthic Habitat
---------------

The benthic ecosystems comprise essentially of:

Corals
^^^^^

Having survived several mass extinctions, corals are animals (marine invertebrates) despite having a plant-appearance. The coral animals are referred to as polyps and are colonial in nature, being hosted on calcium carbonate skeletons. All polyps exist in harmony on the same calcium carbonate skeleton. Coral polyps have tentacles with nematocyst – stinging cells to catch preys, even small fish (~10% of food source). Symbiotic algae living inside the coral polyp tissue (zooxanthellae) provide ~90% of food source through photosynthesis. The zooxanthellae is also responsible for giving the corals their pigmentation.

.. figure:: fig4.png
   :alt: The coral polyp

Algae/Seaweed
^^^^^^^^^^^^

Algae are photosynthetic organisms that contain chlorophyll pigments. They lack the typical roots, stems, and leaves of vascular plants. They are not classified as plants. Instead, they fall into the group of protists and can be unicellular (Phytoplankton) or multicellular (macroalga seaweed). The most common types of algae include: (1) Brown algae/kelp (Shallow-Intermediate seawater); (2) Green algae (mostly in freshwater); Red algae (Deep seawater).

.. figure:: fig5.png
   :alt: The algal specie

Seagrass
^^^^^^^^

Seagrass are flowering plants that are found in shallow coastal seawater and can develop into dense meadows. They play a vital role in stabilizing the coastline and minimizing sediment movement that may lead to erosion areas. They have important carbon sequestration properties – 4000 m² sequesters 550 kg equivalent carbon annually (Equivalent to a car traveling twice the distance from Madagascar, Comoros, Seychelles, and Mauritius).

.. figure:: fig6.png
   :alt: The seagrass specie

Geomorphological Classification Scales
--------------------------------------

Based on the review of existing coastal features in the Indian Ocean Island Countries, the following Classification Scales are employed for terrestrial and benthic features of the coast.

.. figure:: fig7.png
   :alt: The coastal feature classes

Methodology
------------

The framework for the classification of coastal features is presented in Fig. 8. Sentinel 2 data is sourced and employed in the creation of a land and an ocean mask (about 5km from the shoreline). Terrestrial features are thereafter classified using a supervised classification technique (Maximum Likelihood or Support Vector Machine). Signature files are created using a sample set of control points for each feature. The result of the supervised classification is then validated against surveyed and literature sources. A manual correction is then undertaken to refine the classification of the classified features.

Benthic features are classified from the extracted Sentinel 2 image using the ocean mask. A depth invariant index algorithm is applied to correct for the water column and enhance the accuracy of classification. A supervised classification technique is employed to delineate known features, including seagrass, underwater sediments, amongst others. An unsupervised k-means classification is used to detect unidentified classes. Validation and manual correction follow to ensure the correctness of the benthic classifications.

.. figure:: fig8.png
   :alt: Methodological framework for geomorphological feature identification

Supervised Classification
--------------------------

Satellite sensors use the unique reflectance properties of distinct terrestrial features that permit delineation and characterization of their extents. Sentinel 2 high-resolution, multi-spectral images are used and consist of 13 spectral bands that range from the visible range to the shortwave infrared (SWIR). Supervised Classification: This process necessitates the user to manually interpret an image through grouping of grid cells that share common spectral reflectance. The classification procedures are summarized essentially in 3 main stages:

1. Using visual interpretation, the spectral signature for a geomorphological class is defined → Training set for a class
2. A classification algorithm is thereafter utilized and employs the training class to identify grid cells belonging to that spectral class
3. The range of numerical spectral signature values (R,G,B,NIR,…) belonging to distinct feature classes are used to categorize and group cells sharing common spectral properties

.. figure:: fig9.png
   :alt: Sentinel 2 high-resolution, multi-spectral images

Classification Algorithms
-------------------------

Maximum Likelihood Classification (MLC)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The algorithm assumes that the distribution for respective feature classes in each band follows a normal curve and determines the probability that a random pixel belongs to a certain class.

.. figure:: fig10.png
   :alt: Illustration of the underlying principle of MLC

Support Vector Machine (SVM)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SVM performs the classification by drawing a hyperplane. The hyperplane is drawn in such a way as to maximize the distance to points in either class (referred to as the margin).

.. figure:: fig11.png
   :alt: Illustration of the underlying principle of SVM

Random Forest
^^^^^^^^^^^^^

This algorithm works by building multiple decision trees and then merging them together to get more stable and accurate predictions. A training dataset is used and labelled into a decision tree, with an underlying set of rules that will aid in the classification process.

Unsupervised Classification
---------------------------

In unsupervised classification, no training dataset is required. Instead, the user specifies the number of classes and an algorithm automatically groups the classes that share similar statistical behavior. The most used clustering technique is the k-means method.

Reflectance and Spectral Signature
-----------------------------------

The spectral information of features is used to distinguish between them. Energy from the sun is absorbed and reflected by features on earth, which are thereafter detected and measured. Each feature reflects energy to different extents owing to their chemical and structural compositions (Spectral Reflectance). These are interpreted and used to classify coastal terrestrial features.

.. figure:: fig12.png
   :alt: Reflectance spectra of terrestrial features

Capturing the individual feature spectrum is relatively more complex than the terrestrial components. The outgoing radiation from the shallow water has the contribution of both the water column and bottom substrate. Water column correction is therefore applied in case the shallow lagoon section is murky. A Depth Invariant Index algorithm is employed in that regard. The distinction in spectral reflectance of different features helps identify benthic components.

.. figure:: fig13.png
   :alt: Reflectance spectra of benthic features

References
-------------

Coastal zone. Available on: https://commons.wikimedia.org/wiki/File:Littoral_Zones.jpg 
Coral polyp. Available on: https://commons.wikimedia.org/wiki/File:Coral_polyp_it.svg 
Hedley, J.D., et al., Spectral unmixing of coral reef benthos under ideal conditions. Coral Reefs, 2004. 23(1): p. 60-73

