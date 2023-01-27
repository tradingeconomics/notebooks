FROM jupyter/scipy-notebook:85f615d5cafa
RUN git clone https://github.com/tradingeconomics/notebooks
RUN pip install --upgrade tradingeconomics
RUN pip install plotly mplfinance
ENV apikey=guest:guest

# Build
# docker build -t tradingeconomics/notebooks:latest .

# run
# docker run --rm --name te-notebooks -p 8888:8888  -e apikey='guest:guest' -v "${PWD}":/home/jovyan/work tradingeconomics/notebooks:latest  start.sh jupyter lab --LabApp.token=''

# push
# docker push tradingeconomics/notebooks:latest

