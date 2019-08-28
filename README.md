# My Gallery

## Description

> This a personal gallery application that displays a veriaty of my photos.

### Author

**Danmark Mutai**_- create on 25/8/2018_

## BDD

| Behaviour         | Input            | Output                     |
| ----------------- | ---------------- | -------------------------- |
| serch by category | category         | images under that category |
| serch by location | location         | images under that category |
| Copy Image link   | click bitton     | link copied                |

### Technologies used

    - Python 3.6
    - HTML
    - Bootstrap 4
    - Heroku
    - Postgresql
    - Django

## Setup and installations

#### Prerequisites

1. [Python3.6](https://www.python.org/downloads/)
2. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
3. [Pip](https://pip.pypa.io/en/stable/installing/)

#### Clone the Repo and rename it to suit your needs.

```bash
git clone https://github.com/Dnmrk4/Gallery.git
```

#### Initialize git and add the remote repository

```bash
git init
```

```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment

```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables

> Create a `.env` file and paste paste the following filling where appropriate:

```
SECRET_KEY='9bf71cb57c4c8811'
DEBUG=True #set to false in production
DB_NAME='gallery'
DB_USER='user'
DB_PASSWORD='password'
DB_HOST='127.0.0.1'
MODE='dev' #set to 'prod' in production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies

Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Run chmod a+x start.py

```bash
chmod a+x start.py
```

#### Run the app

```bash
./start.sh
```

#### Access the application through localhost:5000

Open [localhost:5000](http://127.0.0.1:5000/)

## Contributing

Please read this [comprehensive guide](https://opensource.guide/how-to-contribute/) on how to contribute. Pull requests are welcome :-)

## Bugs

Create an issue mentioning the bug you have found

## Support and contact details

You can [email](https://danmark.chemuren@gmail.com/) for further help/information.

### License

This application uses a [MIT license](/LICENSE).

*Copyright* **Danmark Mutai**