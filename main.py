from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from beam_nuggets.io import relational_db
from apache_beam.io import WriteToText
import apache_beam as beam
import argparse

def Options(argv=None, save_main_session=True):
    parser = argparse.ArgumentParser()
    parser.add_argument('--output')
    parser.add_argument('--db_name')
    parser.add_argument('--table_name')
    parser.add_argument('--runner')
    parser.add_argument('--requirements_file' ,required=False)
    parser.add_argument('--job_name',required=False)
    parser.add_argument('--project', required=False)
    parser.add_argument('--staging_location', required=False)
    parser.add_argument('--temp_location', required=False)
    parser.add_argument('--region', required=False)
    parser.add_argument('--machine_type', required=False)
    parser.add_argument('--subnetwork', required=False)
    parser.add_argument('--driver_class_name',required=False)
    parser.add_argument('--jdbc_url', required=False)
    parser.add_argument('--username',required=False)
    parser.add_argument('--password', required=False)
    parser.add_argument('--query', required=False)

    known_args, pipeline_args = parser.parse_known_args(argv)

    pipeline_args.extend([
        '--runner={}'.format(known_args.runner),
        '--project={}'.format(known_args.project),
        '--region={}'.format(known_args.region),
        '--subnetwork={}'.format(known_args.subnetwork),
        '--staging_location={}'.format(known_args.staging_location),
        '--temp_location={}'.format(known_args.temp_location),
        '--job_name={}'.format(known_args.job_name),
        '--machine_type={}'.format(known_args.machine_type),
        '--requirements_file={}'.format(known_args.requirements_file),
    ])
    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(SetupOptions).save_main_session = save_main_session
    return known_args,pipeline_options

known_args, pipeline_options = Options()


with beam.Pipeline(options=pipeline_options) as p:
    records = p | "Reading records from db" >> relational_db.ReadFromDB(
        source_config=relational_db.SourceConfiguration(
        drivername='postgresql',
        host=known_args.jdbc_url,
        port=5432,
        username=known_args.username,
        password=known_args.password,
        database=known_args.db_name,
),
        table_name=known_args.table_name
    )

    records | 'save in storage' >> WriteToText("gs://path_to_storage/output/", file_name_suffix=f'{known_args.db_name}.json')