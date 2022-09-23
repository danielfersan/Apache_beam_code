
<h1 align="center"> RelationalDB to Google Cloud Storage </h1>

A simple code that runs a process in apache beam, to connect a relational data bank on premises to google cloud Storage

## Introduction
This code is the result of a project I worked on, in which, due to the volume of files that were being imported into the same table in bigquery, it was necessary to create an unload stage to then perform a single insertion job in Bigquery.
In order to solve the problem, a code was created in Apache beam that accesses any type of relational database using the library:

`from beam_nuggets.io import relational_db`

And record to google cloud storage using the library:

`from apache_beam.io import WriteToText`

### Simple to use
> Install the requirements.txt \
> Change the variable in the terminal command
### Choose where to run
> Choose in which environment you run your code by changing only the variable runner

## Installation
To execute the code, first install the requirement.txt

```bash
pip install requirements.txt
```
Execute the comand in terminal
```bash
python3 -m main \
    --runner \
    --output gs://path_to_storage/output/ \
    --job_name name_of_job_in_dataflow \
    --requirements_file ./requirements.txt \
    --region us-east1 \
    --temp_location gs://path_to_storage/temp/ \
    --staging_location gs://path_to_storage/temp/ \
    --project my_project \
    --machine_type n1-standard-2 \
    --jdbc_url  \
    --username  \
    --password  \
    --db_name db_name \
    --table_name table_name \
    --subnetwork in_case_to_use_VPN
```