# Watkins

This dataset contains data from [Watkins Marine Mammal Sound Database, Woods Hole Oceanographic Institution](https://cis.whoi.edu/science/B/whalesounds/index.cfm), formatted in a way that should make it amenable to machine learning processing. 

One of the founding fathers of marine mammal bioacoustics, [William Watkins](https://www.whoi.edu/oceanus/feature/william-watkins), carried out pioneering work with William Schevill at the Woods Hole Oceanographic Institution for more than four decades, laying the groundwork for our field today. One of the lasting achievements of his career was the Watkins Marine Mammal Sound Database, a resource that contains approximately 2000 unique recordings of more than 60 species of marine mammals. Recordings were made by Watkins and Schevill as well as many others, including G. C. Ray, D. Wartzok, D. and M. Caldwell, K. Norris, and T. Poulter. Most of these have been digitized, along with approximately 15,000 annotated digital sound clips.

The Watkins database has enormous historical and scientific value. The recordings provide sounds professionally identified as produced by particular marine mammal species in defined geographic regions during specific seasons, which can be used as reference datasets for marine mammal detections from the growing amounts of passive acoustic monitoring (PAM) data that are being collected worldwide. In addition, the archive contains recordings that span seven decades, from the 1940's to the 2000's, and includes the very first recordings of 51 species of marine mammals. These data provide a rich resource to efforts aimed at examining long-term changes in vocal production that may be related to changes in ambient noise levels, as well as serve as a voucher collection for many species. 

The database is organized into three subsets: Best of' cuts, All cuts, and Master tapes. The 'Best of' cuts section contains 1,694 sound cuts deemed to be of higher sound quality and lower noise from 32 different species. The All cuts section contains approximately 15,000 sound cuts, which includes those in the 'Best of' section. The Master tapes section contains almost 1,600 entire tapes. Metadata for cuts and master tapes are available by clicking on the 'Metadata' link associated with each file. Metadata for master tapes are also included in the zip file for that tape. Metadata is explained in detail in [WHOI Technical Report 92-31](https://cis.whoi.edu/science/B/whalesounds/WHOI-92-31.pdf): SOUND Database of Marine Animal Vocalizations - Structure and Operations.

## Dataset information

We chose to explore the 'Best of' subset of the [Watkins Marine Mammal Sound Database, Woods Hole Oceanographic Institution](https://cis.whoi.edu/science/B/whalesounds/index.cfm), which contains 1697 recordings, over 4 hours of audio, across 32 marine mammal species. The majority of the recordings are short, on the order of seconds. Out of 1697 recordings, only forty three are longer than a minute.

Data is available for download from Internet Archive as [a single zip file](https://archive.org/download/watkins_202104/watkins.zip). This dataset contains only file level labels.

## Table of contents

1. [How to download the dataset](https://github.com/earthspecies/library/blob/main/watkins/01_Download_Dataset.ipynb).
2. [Data Exploration](https://github.com/earthspecies/library/blob/main/watkins/02_Data_Exploration.ipynb).
3. [Data Preprocessing](https://github.com/earthspecies/library/blob/main/watkins/99_Data_Preprocessing.ipynb)
