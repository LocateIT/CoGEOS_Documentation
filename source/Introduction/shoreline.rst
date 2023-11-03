SHORELINE
==========

Introduction
==============

Shoreline extraction is the process of identifying the position of the land-water interface in satellite images.
It is an important task for various applications, such as coastline change detection and coastal zone management.
The task of shoreline extraction is very difficult, time-consuming, and sometimes impossible for entire coastal systems 
when using traditional ground survey techniques.

 Advanced remote sensing (RS) and geographic information system (GIS) techniques are being used for detection of shoreline position and change analysis.
 For accurate subpixel accuracy for characterising the shoreline changes, an automated way/tool for shoreline extraction in required.

 In general, the shoreline extraction process involves obtaining satellite images, pre-processing the data, and applying machine learning algorithms to extract the shoreline.

 How accurate are the machine learning algorithms in extracting shorelines?
 ----------------------------------------------------------------------------
 The accuracy of machine learning algorithms in shoreline extraction depends on various factors such as quality of the satellite images, the complexity of the shoreline, and the type 
 of machine learning algorithm used.

 For instance, a study by Celik and Gazioglou (2022) assessed the accuracy of three machine learning classifier groups (Support Vector Machines, Multilayer Perceptron (MLP), 
 and Ensemble Learning classifiers) on different coastal types for coastline extraction. The authors tested four kernel functions and four activation functions and found that 
 the Random Forest algorithm had better accuracy than the SVM algorithm. The overall accuracy values of all maps were 97.18%, and the kappa coefficient was 0.97 for RF algorithm, 
 while for SVM algorithm, the mean overall accuracy and kappa coefficient of maps were 85.15% and 0.79, respectively 

Another study by Zhang et al. (2019) proposed a deep learning-based method for shoreline extraction from Sentinel-2 images. The authors used a U-Net architecture with a ResNet-50 encoder to 
extract shorelines from Sentinel-2 images. The proposed method achieved an overall accuracy of 96.7% on a test dataset.

However, it is important to note that the accuracy of machine learning algorithms in shoreline extraction is not always perfect and can be affected by various factors such as weather conditions, 
image quality, and other environmental factors. Therefore, it is important to validate the results of any machine learning algorithm with ground truth data or other reliable sources.

Challenges in automated shoreline Extraction
---------------------------------------------
Automated shoreline extraction is a complex task that involves several challenges. Some of these challenges include: |br|
| * **Image quality:** The quality of the satellite images can affect the accuracy of the shoreline extraction process. Poor image quality can lead to errors in the detection of the shoreline.
| * **Shoreline complexity:** The complexities of the shoreline has been the major challenge in the automatic shoreline process especially the coastlines of Madagascar which has complex geometries coupled with many inlets and bays.
* **Weather conditions:** Weather conditions such as cloud cover, fog and haze affects the quality of satellite images especially with optical satellite images which makes it difficult to extract shorelines accurately.
* **Environmental factors:** Environmental factors such as such as tides, waves, and currents can also affect the accuracy of shoreline extraction.
* **Machine learning algorithms:** The choice of machine learning algorithm used for shoreline extraction can also affect its accuracy. Different algorithms have different strengths and weaknesses,  and choosing the right one for a particular application is important.
* **Ground truth data** Validating the results of machine learning algorithms with ground truth data/other reliable sources is important to ensure their accuracy.

shoreline extraction applications
----------------------------------
Shoreline extraction has several applications in various fields. Some of the applications of shoreline extraction include:
* **Coastal zone management:** Shoreline extraction can be used to monitor changes in the coastline and assess the impact of human activities on the coastal environment.
* **Coastal erosion monitoring** It can be used to monitor the rate of coastal erosion and identify areas that are at risk of erosion.
* **Marine ecology** Shoreline extraction can be used to study the distribution and abundance of marine organisms along the coast.
* **Coastal engineering** Shoreline extraction can be used to design coastal structures such as breakwaters, jetties, and seawalls.
* **Navigation** Shorelne extraction can be used to create nautical charts and maps for navigation purposes.


Data Acquisition
=================


Pre-processing
===============


Shoreline Extraction
=====================


Results
========
* **Mauritius:** Shoreline data derived from sentinel-2 imagery in this region reveals a spatial shift in the coastline over the course of two consecutive years. The predominant alteration in the shoreline is characterized by minimal changes, encompassing a substantial 57% of the total variation. Conversely, a significant 24.5% of the shoreline transformation is attributed to a pronounced retreat, with an additional 15.4%, 1.8%, and 1.4% associated with moderate retreat, moderate erosion, and high erosion, respectively. It is worth noting that the Mauritius shoreline exhibits relatively low levels of erosion, which have effectively deterred retreat dynamics, accounting for only 6.6% of the overall transformation. This outcome accentuates the prominence of shoreline expansion, representing a dominant 93.4% of the total change.  
* **Sychelles** Seychelles exhibits remarkably consistent shoreline transformation rates, showcasing similarities in high erosion, minimal change, and substantial retreat, constituting 25.3%, 26.1%, and 23.2% of the total alterations, respectively. During this six-year span, moderate erosion and moderate retreat gained prominence, contributing 14.4% and 11.0%, respectively, to the shoreline's evolution. Seychelles unravels the enigmatic dance between coastal expansion and withdrawal, with growing areas taking up 46.4% of the narrative, albeit overshadowed by the dominance of retreating regions, accounting for 53.6% of the dynamic alterations.
* **Mayotte Island-Comoros** The results delineate the shoreline's transformation rates, where high erosion predominantly covers 64.8% of the shoreline changes. Following high erosion, the second most significant change rate is found to be low change, accounting for 12.0% of the alterations. High retreat, moderate erosion, and moderate retreat come next in line, contributing 10%, 9.4%, and 3.9%, respectively, to the total observed changes. This study further highlights a concerning situation, with a substantial portion of the overall shoreline change area undergoing retreat (86.4%), while a small segment represents growth areas, constituting only 13.6% of the observed alterations.
* **Ngazidja Island-Comoros** The results obtained from the shoreline analysis unveil a substantial portion of the shoreline, approximately 46.0%, characterized by low change dynamics, while high erosion influences around 30% of the shoreline. These two predominant rates serve as valuable indicators when anticipating the state of Grande Comore Island's shoreline. Additionally, we observed occurrences of high retreat, moderate erosion, and moderate retreat, each contributing 14.3%, 6%, and 3.8% to the overall shoreline change rate. Significantly, the findings emphasize the prevalence of retreat in the coastal shoreline, primarily due to the substantial impact of erosion on specific shore sections, accounting for 61.5% of the total changes. In contrast, growth dynamics along the coastal shoreline remain limited, representing only 38.5% of the overall change dynamics. 
* **Nzwani and Mwali Island-Comoros** An analysis of shoreline changes over six years reveals key patterns. The majority (56.7%) of the shoreline remained stable, while 19.5% experienced high erosion levels, indicating vulnerability. Additionally, around 14.1% displayed moderate erosion, and 7.0% witnessed moderate retreat. Although high retreat levels were less prevalent, the 2.9% with the highest retreat rates highlight significant retreat in specific areas. Retreat processes dominated at 85.1% of the total shoreline changes, supported by high erosion rates exceeding retreat levels. In contrast, 14.9% of changes represented growth dynamics, marking a distinct contrast. 

Discussion
===========
* **Mauritius:** Mauritius' coastal shoreline has demonstrated remarkable stability during the observed two-year period. This stability can be primarily attributed to effective measures taken to mitigate the influences of erosion and accretion. Specifically, the establishment of breakwaters along certain sections of the island's shoreline has proven instrumental in shielding it from the potentially adverse effects of wind and waves. Moreover, the implementation of seawalls in the urbanized coastal areas has further bolstered shoreline protection against erosion and accretion, which can result from sediment movements along the coast or tidal waves. These initiatives underscore the government's longstanding commitment to formulating and implementing policies aimed at safeguarding the coastal regions and their surrounding environments.
* **Sychelles** Predominantly, minimal changes characterize the shoreline, with a harmonious equilibrium maintained between heightened erosion and increased retreat levels. These shoreline dynamics are significantly influenced by the island's diverse coastal ecosystem, playing a synergistic role in these alterations. The presence of human settlements along the shoreline presents a dual-edged impact, notably contributing to coastal erosion along the western segment of the island. This can be attributed, in part, to the extraction of sediments for construction purposes, rendering the shoreline susceptible to erosion. Conversely, the human settlement factor contributes to shoreline accretion levels, given that construction activities introduce artificial elements that exert influence on sediment transport and sediment entrapment. These artificial features can foster accretion zones while concurrently safeguarding neighboring areas from erosion processes.
* **Mayotte Island-Comoros** The island of Mayotte grapples with the significant challenge of high erosion levels, stemming from a multifaceted set of factors, prominently including human settlements along its coastal areas. This assertion gains substantial support from research findings, which prominently reveal heightened erosion trends across a substantial portion of the island's coastal settlements. Furthermore, the erosive impacts of tidal wave actions upon the shoreline play a pivotal role in exacerbating this situation. The absence of a biologically diverse shoreline landscape further compounds the predicament by rendering the coastline devoid of natural protective buffers, thus leaving it exposed and susceptible to erosion. This discerning analysis of the results accentuates the pressing need for proactive management strategies to harmonize coastal development endeavors with the imperatives of environmental preservation.
* **Ngazidja Island-Comoros** A substantial portion of Ngazidja's coastal shoreline remained remarkably stable over the observed years, with minimal changes or, in some cases, virtually no alterations. This observation can be attributed to the distinctive composition of Ngazidja’s coastline, characterized predominantly by sandy beaches and ancient volcanic lava flows along the northern, northeastern, and southeastern sectors. These geological features render these shoreline sections more susceptible to erosion and wave-induced actions. Furthermore, the presence of rocky cliffs and shallow reefs, primarily located along the western and southwestern segments, enhances the shoreline's resilience to the potential effects of rising sea levels. The juxtaposition of these two distinctive geological elements contributes to a state of equilibrium in the dynamics of change, counterbalancing the forces of erosion and accretion. Nonetheless, it is worth noting that while a significant portion of the shoreline maintains a state of low change, certain sections exhibit a predisposition to high erosion and limited accretion.
* **Nzwani and Mwali Island-Comoros** Similarly, to Ngazidja, the shoreline dynamics of Nzwani and Mwali primarily exhibited a state of low change as the dominant pattern. This pattern is underpinned by several factors that influence these coastal areas. Notably, both Nzwani and Mwali feature extensive mangrove vegetation along their shorelines, which serves as a natural defense against the impacts of waves and storm surges, effectively mitigating their effect on the coast. Furthermore, these mangroves play a vital role in sediment capture, reducing the erosive potential caused by sediment movement. The application of rigorous coastal management strategies also contributes to this pattern, encompassing initiatives such as the construction of seawalls and breakwaters in various shoreline sections. A compelling example of these measures can be observed in Mutsamudu, the capital city of Nzwani.

Conclusion
===========
