#!/usr/bin/env bash
# exit on error
set -o errexit

STORAGE_DIR=/opt/render/project/.render

if [[ ! -d $STORAGE_DIR/chrome ]]; then
  echo "...Downloading Chrome"
  mkdir -p $STORAGE_DIR/chrome
  cd $STORAGE_DIR/chrome
  wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
  rm ./google-chrome-stable_current_amd64.deb
  cd $HOME/project/src # Make sure we return to where we were

  echo "...Downloading ChromeDriver"
  CHROMEDRIVER_VERSION=$(google-chrome-stable --version | awk '{print $3}' | cut -d '.' -f 1-2)
  CHROMEDRIVER_URL="https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/121.0.6167.85/win64/chromedriver-win64.zip"
  wget -O chromedriver.zip $CHROMEDRIVER_URL
  unzip chromedriver.zip -d $STORAGE_DIR/chrome
  rm chromedriver.zip

else
  echo "...Using Chrome from cache"
fi

# be sure to add Chromes location to the PATH as part of your Start Command
# export PATH="${PATH}:/opt/render/project/.render/chrome/opt/google/chrome"

# add your own build commands...

pip install -r requirements.txt