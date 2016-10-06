# Make Talk Good

Some of us at the [Lansing Makers Network](https://www.lansingmakersnetwork.org/) are 
attempting to create a machine which will mechanically reproduce intelligible human 
speech. This software uses [wit.ai](https://wit.ai) to convert incoming audio into text.
Then [espeak](http://espeak.sourceforge.net/) is used to convert the text into phonemes 
in the [IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet). A utility
from the [listener](https://github.com/mcfletch/listener) project is used to map IPA to
[Arpabet](https://en.wikipedia.org/wiki/Arpabet). Very, very, very crude audio files for 
each phoneme are included in order to verify the translation and triggering is correct. 
The goal is to trigger the playing of various acoustic instruments to synthesize the vocal
sounds.