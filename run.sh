#!/bin/bash
docker build -t party_generator .
INPUT_DATA=$(pwd)/input_data
OUTPUT_DATA=$(pwd)/output_data
echo $INPUT_DATA
echo $OUTPUT_DATA
docker run -v $INPUT_DATA:/input_data -v $OUTPUT_DATA:/output_data -it party_generator
