awpugwiki
=========
A silly project providing a basic wiki to show some of the basics of django


Installation
------------

On a Unix-y environment do the following::

    sudo easy_install pip
    sudo pip install virtualenvwrapper
    echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.profile
    echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile
    mkvirtualenv awpug
    pip install django
    git clone git://github.com/dmclain/awpugwiki.git
    cd awpugwiki


License
-------
Copyright 2011 Dave McLain

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
