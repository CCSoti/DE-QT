DE-QT
=====

Data Evolution and Quality Tracking of Scientific Data Sets

1) Project Description
The project is about measuring data quality of a specific data set – the data set of the
BRITICE-CHRONO project, constraining rates and style of marine-influenced ice sheet decay.
The School of Geographical and Earth Sciences at Glasgow University is currently involved
in with the BRITICE-CHRONO project, which is a consortium based research project which aims
to determine the rate and timing of the retreat of the last British-Irish ice sheet. This research
involves the collection and analysis of thousands of rock, sediment and organic samples. There is a
web-based application, which enable users to upload, edit, view and search sample information. The
web-based application is created by a PhD student from University of Glasgow – Fiona Steven, by
the proposal of the leader of the consortium, Dr. Derek Fabel.
By collecting and analysing the data of the thousands of rock, sediment and organic samples,
the researchers, involved in the project, will be able to establish the dates at which the retreating ice
had re-exposed the underlying surfaces at each collection location. The data will help with
estimating the rate of the ice sheet’s retreat.
In order to use the collected data, it needs to be managed, and that depends on the types of
data involved, how data is collected and stored, and how it is used - throughout the research
lifecycle. Managing data helps with the organization of research files and data for easier access and
analysis. It helps ensure the quality of the research. It supports the published results of the work
and, in the long term, helps ensure accountability in data analysis. This project has a long term goal
to develop a process to support the tracking of data set evolution in a comparable way to source
code configuration management.
The project is looking to achieve representation and visualization of the data in a way that
will be manageable. An additional web page will be created to the Fiona's web-based application in
order to visualize the data in metrics that will help the researchers to see how the data has been
changing over time and the variation of the different data types.

2) Running the prototype
You can see how to run the prototype by watching the uploaded video.
Also, here is an  explanation of how you can run it:
 - download the DQDV folder - it contains the whole ptototype;
 - open the folder with command prompt window;
 - you will see the cmd script "britice.bat" and the database - codemets.db;
 - you can replace the database with another database, which has the SAME structure and tables as the original one;
 - run the command: britice.bat codemets.db, in the cmd window;
 - it will take a few minutes to generate the html files;
 - after that go to the HTMLFiles folder and open - coordinates.html, bearing_inclination.html, sample.html, osl_sample.html,    tcn_sample or core_details.html; The other files are additional functions to these files;
 - on the html files you will see all of the metrices and charts;
 
3) Dissertation
In the Report of the project you will find more details for each part of the metrices and graphs.
