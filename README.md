# Guess The Number for humans (and computers too)

#### Clone the repo
```
cd ~/code/
git clone git@github.com:Renzo04/guess-the-number.git
cd guess-the-number
```

#### Install it (use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/))!
```
mkvirtualenv -p python3 -r requirements.txt gtn
workon gtn
```

#### Let's play!
```
python main.py
```

#### Run tests
```
pytest
# Coverage
py.test --cov=gtn tests
```
