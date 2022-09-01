# cigna-python-challenge

# **How To Send** 

Clone down the solution and copy it into your own GitHub repo.
Please include a section in the ReadMe walking through how you solved it and the process you used. 
You will send your Github repo link to your recruiter when finished. 

# **Instructions**

Create an ETL script, which imports, parses, aggregates and outputs the data in 1 required 
format, and for bonus points, several optional formats (more details below).

The source data can be seen below in CSV format.

The data is formatted as such to supply an hourly snapshot of the percentage of free memory. 
Each unique entry (hostname), is stored on each column.  Each row below the column represents 
a snapshot of the collected data, stored via the 'Date / Time' timestamp stored in epoch time.

The format of the column keys are 'node type#hostname#metric', so as an example, the hostname 
for the string 'host#HOST1#% Free Memory avg 1h' could be identified as HOST1.  Columns are 
comma delimited.

Please create a process which will intake the below provided CSV source, and generate 1 line 
of output for the following aggregations:

- The minimum value for each unique hostname.
- The maximum value for each unique hostname.
- The average value for each unique hostname.

Additionally, generate the following aggregated values:

- The minimum value for all hostnames.
- The maximum value for all hostnames.
- The average value for all hostnames.

Data for your results should be stored in a result format which you can utilize to output your 
results to STDOUT. Optionally, we'd like for you also to provide formatted output for some of 
the following options:

- XML
- JSON
- YAML

Then, export your results to a pipe delimited flat .txt file.

You will be allowed full use of the search engine of your choice, but not allowed to use Pandas/numPy/equivalent library. 
We want to see how you accomplish it, not how the library does it for you.
Also, please put your code in a script that can be easily pulled down and ran locally. 

Good luck!



