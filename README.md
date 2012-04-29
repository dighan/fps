# Flash Player Switcher

FPS eases installation of Flash Player. It is able to switch between all versions between 10.1 and 11.2
(Content Debugger distribution). It is cross-browers and supports only Mac OS X.

# Installation

* Download the archive file from the [downloads](https://github.com/dighan/fps/downloads) page. 
* Checkout the git repository: "git clone git://github.com/dighan/fps.git".

# Usage

FPS is accessible through the `fps.py` script. It requires only one argument:

* `flash_player_version`- The Flash Player version you want to install

To execute it, just type:

    ./fps.py flash_player_version

To avoid to specify each time the complete flash player version, you can use shortcuts:

    ./fps.py 11
    ./fps.py 11.1
    ./fps.py 11.2.202
    ./fps.py 11.2.202.23

The previous examples will always load the lastest Flash Player version that starts with `flash_player_version`
