#!/bin/sh

# Update Detection on Demand
openapi-generator generate -i ../developer-hub/src/apis/detection_on_demand.yml -o detection_on_demand -g python --package-name fireeye.detection

rm -r fireeye/detection
mv detection_on_demand/fireeye/detection fireeye

mkdir docs/detection_on_demand
rm -r docs/detection_on_demand/docs
mv detection_on_demand/docs docs/detection_on_demand
mv detection_on_demand/README.md docs/detection_on_demand
rm -r detection_on_demand

sed -n '/Getting/,$p' docs/detection_on_demand/README.md | sed 's/import\ detection/from\ fireeye\ import\ detection/' > docs/detection_on_demand/README.md