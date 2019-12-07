import apache_beam as beam
import sys

PROJECT='YOUR_PROJECT'
BUCKET='YOUR_BUCKET'
REGION='us-central1'

def run():
   argv = [
      '--project={0}'.format(PROJECT),
      '--staging_location=gs://{0}/staging/'.format(BUCKET),
      '--temp_location=gs://{0}/staging/'.format(BUCKET),
      '--runner=DataflowRunner'
   ]

   p = beam.Pipeline(argv=argv)

   (p
      | 'ReadAvroFromGCS' >> beam.io.avroio.ReadFromAvro('gs://cloud-samples-data/bigquery/us-states/us-states.avro')
      | 'WriteToBigQuery' >> beam.io.WriteToBigQuery('{0}:dataset.avrotable'.format(PROJECT))
   )

   p.run()

if __name__ == '__main__':
   run()
