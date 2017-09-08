# JSTMB_O38_Pipeline

This is the source code for our JSTMB primitive on the seed data O38.

Once you clone this folder into your local repo, you can directly build the Docker image by:

docker build -t jstmb38 ./

Then, you can run the pipeline script in the following way:

docker run jstmb38 python O38_JSTMB_wrapper.py "trainData.csv" "trainTargets.csv"

The output is the selected features stored in a csv file
