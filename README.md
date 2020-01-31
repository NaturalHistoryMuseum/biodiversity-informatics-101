# Biodiversity Informatics 101

|     |     |
| --- | --- |
| MSc title        | Taxonomy and Biodiversity |
| Module           | Biodiversity 2: Applied   |
| Document version | 1.0 (31/01/2020)          |
| Author           | Ben Scott                 |
| Duration         | 3 hours                   |


#### Scope and outputs

##### This class will familiarise participants with some of the platforms, tools and methodologies practised within the biodiversity informatics landscape.  

##### Students will utilise a suite of freely available tools to parse open data sources, analyse and restructure the information, and publish their datasets online in forms that enable scientific reuse of the data.


By the end of the class, students will have a basic understanding of:

- Key occurrence and observation data portals ([GBIF](https://www.gbif.org/))
- How to manipulate data in [OpenRefine](https://openrefine.org/) and Python. 
- How to work with [DarwinCore Archive](https://dwc.tdwg.org/) files
- How to use [WikiData](https://www.wikidata.org/wiki/Wikidata:Main_Page) to perform name reconciliation and name resolution
- How to import data into a [Scratchpad](http://scratchpads.eu/).



#### To start:

1. Work in groups of two

2. Each pair has its own Scratchpads training site:

   http://mscnhm**[x]**.taxon.name

   *Replace x with the number on your handouts*

   

Please open your Scratchpads training site & login (the login link is at the top right of the page; username and password will be provided by your instructor).



## Part 1 - Import invasive alien species

In the first part of this tutorial, we will import a list of invasive species into our training Scratchpads. The list of invasive species names we'll be using is derived from a 2019 DEFRA report, identifying 14 invasive species widely spread in England and Wales and requiring management [1].



##### 1. 1. Download the data

Download the invasive alien species CSV [invasive-alien-species.csv](https://raw.githubusercontent.com/NaturalHistoryMuseum/biodiversity-informatics-101/master/invasive-alien-species.csv).

##### 1.2 Open OpenRefine

Go to the applications directory, and double click "OpenRefine"

Once OpenRefine is running, a browser window should automatically open, and the address [127.0.0.1:3333](127.0.0.1:3333) should be loaded. If not, open a web browser and open the URL [127.0.0.1:3333](127.0.0.1:3333).

##### 3. Load Data into OpenRefine

- The “Create Project” tab will be activated by default

- Under “Get data from”, select “This Computer”, and click “Choose Files”

- Select the file we have just downloaded. It should be named “invasive-alien-species.csv.”

- Click next

- A preview of the data will be displayed.  Open Refine should have determined this is a comma-separated file, and the list of species should be displayed in a three-column table. 


- Click on “Create Project”

##### 4. Facets

*We want our site to include only botanical records, but the source data contains animals. To remove them we will apply a text facet.*

- Locate the field “Kingdom” and click on the arrow in the title.
- Select “Facet” > “Text Facet”
- In the left-hand column, click the link "Plantae". This will select only those records where Kingdom = “Plantae”

##### 5. Name resolution

*We want to ensure these are the currently accepted taxonomic names, so the next step is to validate the names against a taxonomic name resolution service. Many online services provide this functionality, but in this example we will reconcile our names against WikiData.*  

- Locate the field “Scientific name” and click on the arrow in the title.
- Select “Reconcile” > “Start reconciling”
- In the pop-up window, select "WikiData"

*OpenRefine is now looking up our taxonomic names against the data in Wikidata to see if it can identify a suitable class to reconcile them against.*

- Select "taxon Q16521", and click "Start reconciling"
- The table view now shows the reconciled taxonomic names. The first name has been changed from *Anacharis nuttallii* to *Elodea nuttallii* - that's because *Anacharis nuttallii* was the original name, but in 1920 was moved into the genus *Elodea* [2].
- There are multiple varieties of *Gunnera tinctoria* so we need to clarify which we're interested in. Select "*[Gunnera tinctoria](https://www.wikidata.org/wiki/Q847582)*"

##### 6. Organise the columns

*To easily import this information into a Scratchpad, we need to organise the columns.* 

- Locate the field “Scientific name” and click on the arrow in the title.
- Select “Edit column” > “Add columns from reconciled values...”
- Here we can select extra information from WikiData to include in our report. Select "Taxon name"
- Select "OK".

*A new column "taxon name" has been added showing the reconciled taxonomic name.*

- For this new column, click on the arrow in the title.
- Select “Edit column” > “Rename this column”
- Enter the new name as "Term name" and press "OK"
- Again, click on the arrow in the title for this new column
- Select “Edit column” > “Split into several columns”
- Change the separator from "," to a single space. Press OK.

*Two new columns have been created Term Name 1 and Term name 2, populated with the genus and species name.*

- Locate the field “Term Name 1” and click on the arrow in the title.
- Select “Edit column” > “Rename this column”
- Enter the new name as "Unit name 1" and press "OK"
- Locate the field “Term Name 2” and click on the arrow in the title.
- Select “Edit column” > “Rename this column”
- Enter the new name as "Unit name 2" and press "OK"



##### 1.7. Export the data

- From the top menu, select "Export" > "Comma-separated value"
- Save the file

##### 1.8 Import into your Scratchpad

*Next, we'll import this data into your Scratchpad - but first, we need to create a taxonomy to import it into.*

- Open your Scratchpad site & login.
- In the top menu, select "Structure"
- Click "Taxonomy"
- Click "Add vocabulary"
- Enter a name for the vocabulary - e.g. "UK Invasive species"
- Under biological classification select "Aldea/Fungi/Plants" 
- Click "Save"

*We've created the taxonomy, now let's import the list of names.*

- In the top menu, select "Import"
- Select "Taxonomy" > "CSV file import"
- Under select vocabulary, choose the vocabulary you created in the previous step e.g.  "UK Invasive species"
- Browse, and select the file you exported from OpenRefine.
- Select "Import"



### Part 2 - Import GBIF occurrences

In the second part of this tutorial, we will import UK occurrence records for our 8 invasive species. These have been downloaded from GBIF, the Global Biodiversity Information Facility which aggregates and publishes biodiversity data from institutions across the world. It currently holds 1,391,094,316 occurrence records.

GBIF data is provided as a DarwinCore Archive, a data standard for sharing specimen occurrence and observational records. 

In this part of the course, we will use the Python programming language to manipulate the occurrence records from GBIF, before importing them into our Scratchpads.

##### 2.1 Open Jupyter notebook

The Jupyter notebook is hosted online on Binder [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/NaturalHistoryMuseum/biodiversity-informatics-101/master?filepath=occurrences.ipynb)

Opening the notebook takes a little while, please be patient.

##### 2.2 Run the code in the notebook

- Select "Cell" > "Run all"

##### 2.3 Download localities CSV

Click the "Download localities CSV" link at the bottom of the Notebook, and save the file to your computer.

##### 2.4 Download occurrences CSV

Click the "Download occurrences CSV" link at the bottom of the Notebook, and save the file to your computer.

##### 2.5 Import localities CSV

- Open your Scratchpad site
- In the top menu, select "Import"
- Under "Nodes" select "CSV file import"
- Select "Location"
- Click the "Browse" button, and select the "localities.csv" file you just saved
- Select "Import" to import the locations. Once complete, a status message will tell you whether the process was successful and how many locations were created. 

##### 2.6 Import occurrences CSV

- Within your Scratchpad site, in the top menu, select "Import"
- Under "Nodes" select "CSV file import"
- Select "Specimen/Observation"
- Click the "Browse" button, and select the "occurrences.csv" file you just saved
- Select "Import" to import the occurrences. Once complete, a status message will tell you whether the process was successful and how many occurrences were created. 


*If we now take a look at our Scratchpads, you can now see our taxonomy of UK Invasive species. If you click one of the names in the taxonomy, you can view under maps and specimens the occurrence records we have just imported.*









References

[1]  (https://www.gov.uk/government/consultations/invasive-alien-species-management-measures-for-widely-spread-species-in-england-and-wales).

[2] https://www.cabi.org/isc/datasheet/20761
