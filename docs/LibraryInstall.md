conda create -n toss python=3.10

conda acivate toss

conda install cudatoolkit

pip install insightface
※사용할려면 'vs_BuildTools.exe'를 설치해야한다.

pip install transformers

pip install fastapi

pip install "uvicorn[standard]"

uvicorn CategoryPage:app