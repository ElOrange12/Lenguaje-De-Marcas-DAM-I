# En shell:
# echo 'export NOMBRE="Daniel"' >> ~/.bashrc
# source ~/.bashrc
import os

print(os.environ.get("NOMBRE"))
