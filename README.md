# Trading Economics Notebooks

The Trading Economics Python Jupyter Notebooks GitHub repository showcases examples on how one can easily interact with our data to make interesting data findings and insights. Trading Economics is a gateway to 20 million indicators from 196 countries. Trading Economics provides its subscribers with a near real-time economic calendar updated 24 hours a day, historical data time series sourced recently and directly from national statistics offices, quotes for thousands of financial markets, and active support. 


## Getting started

Users also have the choice to fork or clone this repository into their local computer. Be aware that if you just clone the repository you will not be able to push changes into our master branch. Thus forking is probably better as it allows you to add new files and push changes. 

![Alt Text](https://github-images.s3.amazonaws.com/help/bootcamp/Bootcamp-Fork.png)

```bash
git clone https://github.com/tradingeconomics/notebooks
```
#

## Installation

JupyterLab allows users to do data science using a web-based user interface.

```bash
pip install jupyterlab
```

## Credentials

While many examples can be run with an anonymous guest:guest key, the best path is for you to sign up for a free developer account at https://developer.tradingeconomics.com/ to get your own API key. With a developer account one gets free access to datasets from the Worldbank, the United Nations, the Federal Reserve, the EUROSTAT, and much more.  Dont' worry! We will never share your email information with anyone. If you do not want to register, consider, the API key guest:guest is very limited.


Protect your credentials! Please set your keys as environment variables before you launch your application.

```bash
# linux / mac 
export apikey='guest:guest'
```

```bash
# windows
set apikey='guest:guest'
```
#

## Running


```bash
jupyter lab
```

#

## Running with Docker

Trading Economics Notebooks Docker packages everything you need. Please swap 'guest:guest' with your key.

```bash
docker run --rm --name te-notebooks -p 8888:8888  -e apikey='guest:guest' tradingeconomics/notebooks:latest  start.sh jupyter lab --LabApp.token=''
```

#

## Documentation: 

https://docs.tradingeconomics.com


## Examples: 

https://github.com/tradingeconomics/tradingeconomics 


## Learn more

https://tradingeconomics.com/api/


## Support

Do you have any suggestions? Please let us know

https://tradingeconomics.com/contact.aspx?subject=notebooks



