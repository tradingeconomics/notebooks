FROM jupyter/scipy-notebook:85f615d5cafa
WORKDIR /home/jovyan/tradingeconomics
RUN git clone https://github.com/tradingeconomics/notebooks /home/jovyan/tradingeconomics

# Build
# docker build -t tradingeconomics/notebooks:latest .

# run
# docker run --name te-notebooks -p 8888:8888  tradingeconomics/notebooks:latest

# push
# docker push tradingeconomics/notebooks:latest

