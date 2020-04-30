#!/bin/sh

# Update Detection on Demand
openapi-generator generate -i ../developer-hub/src/apis/detection_on_demand.yml -o detection_on_demand -g python --package-name detection

mv detection_on_demand/detection fireeye

mkdir docs/detection_on_demand
mv detection_on_demand/docs docs/detection_on_demand
mv detection_on_demand/README.md docs/detection_on_demand
rm -r detection_on_demand