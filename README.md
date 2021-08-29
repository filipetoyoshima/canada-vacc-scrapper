# canada-vacc-scrapper

Check up which vaccines are approved in Canada

## Install

I recommend pip with [virtualenvs](https://docs.python.org/pt-br/3/library/venv.html) to keep dependencies track:

```bash
python -m venv env
source env/bin/activate
pip install requirements.txt
```

## Use

Just call `main.py`. You can pass a list of vaccines to be searched:

```bash
cd src
python main.py coronavac
```