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

sed -n '/Getting/,$p' docs/detection_on_demand/README.md | sed '2d' | sed '/Please\ follow/d' > docs/detection_on_demand/README.md.new
rm docs/detection_on_demand/README.md && mv docs/detection_on_demand/README.md.new docs/detection_on_demand/README.md

# Update Helix
# openapi-generator generate -i ~/OneDrive\ -\ FireEye\,\ Inc/api_products/helix/helix_swagger.yaml -o helix -g python --package-name fireeye.helix
# rm -r fireeye/helix
# mv helix/fireeye/helix fireeye

# mkdir docs/helix
# rm -r docs/helix/docs
# mv helix/docs docs/helix
# mv helix/README.md docs/helix
# rm -r helix

# sed -n '/Getting/,$p' docs/helix/README.md | sed '2d' | sed '/Please\ follow/d' > docs/helix/README.md.new
# rm docs/helix/README.md && mv docs/helix/README.md.new docs/helix/README.md