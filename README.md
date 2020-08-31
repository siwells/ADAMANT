# README #

## Adamant(ium) ##
### What is this repository for? ###

* Fork of adamant tool project with necessary changes for sensors, bug fixes, code refactor and overall improvements.

### How do I get set up? ###

Run `pip install -r requirements.txt`

Main dependencies: Python 3.5.1 plus [Flask 0.12](http://flask.pocoo.org/docs/0.12/) and [SQLAlchemy](http://docs.sqlalchemy.org/en/latest/intro.html) 


How do I create dialogue description? Well that's a completely different story. I have used [antlr](http://www.antlr.org) to generate all the lexers and parsers given the DGDL grammar (link soon), and that's in /gen folder. Example dialogue descriptions and an actual link to DGDL coming soon. 

### How does it work?? ###

Well mostly it runs as a web server, but to be honest how you communicate and exchange data can be easily changed in the future (I think so).
Each sensor, main unit, runs it's own server, allowing to communicate without actual central unit that processes all dialogues. It is not designed to work as a web server for communication with web clients (but could be). 
 
 
To initiate a dialogue, both units have to have a version of the dialogue description (in DGDL) available. If not they can share them and then initiate dialogue (swagger file with routes coming soon).


Send initial utterance according to the dialogue description, and this will be verified, adjusted and game status returned to the unit. Unit invited to dialogue will reply with it's own utterance and the same dialogue status (will add uuid verification of the change at some point). 
  

Whatever it is that the unit has to do, it'll have to be attached int the OutputController as an utterance.

### What does it do? ###

Based on dialogue games it (tries to) provides a structured communication framework that allows for specific interactions based on the rules defined in the dgdl file of the game/dialogue description.
 
 
### Can you guarantee it will solve my problems?? ###

100% not. There is still very extensive work to do to make sure this thing works 100% and actually can be used as an external library.