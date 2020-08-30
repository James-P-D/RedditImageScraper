# RedditImageScraper
Console application for downloading images from Reddit in Python

![Screenshot](https://github.com/James-P-D/RedditImageScraper/blob/master/screenshot.gif)

## Introduction

This short Python script was created for the mass-downloading of images from [Reddit](https://reddit.com/). It will be used later for creating data-sets for several Machine Learning projects.

In order to use the script, you will have to have a Reddit account sign-up to create a [developer account](https://www.reddit.com/prefs/apps/). You will be assigned a `client_id` and `client_secret` which you have to enter in [https://github.com/James-P-D/RedditImageScraper/blob/master/src/RedditImageScraper/RedditImageScraper/config.ini](config.ini) before you run the script.

## Usage

The `-r` parameter provides a list of sub-reddits to search.
The `-st` parameter can specify the maximum number of images to download from each sub-reddit. Defaults to 1000.
The `-t` parameter can specify the total number of images to download across all sub-reddits before we abort. Defaults to 10000.
The `-f` parameter can specify the folder into which we download the images. Defaults to `download`.

For example, to download at-most 20 pictures from the [dogpictures](https://www.reddit.com/r/dogpictures/), [dogswithjobs](https://www.reddit.com/r/dogswithjobs/), [GuiltyDogs](https://www.reddit.com/r/GuiltyDogs/), and [dogs](https://www.reddit.com/r/dogs/) sub-reddits, aborting when we have 50 files in total, and saving the files to a folder titled `dog`, we would use the following:

```
python RedditImageScraper.py -r dogpictures dogswithjobs GuiltyDogs dog -st 20 -t 50 -f dogs
```

This should produce something like the following:

```
Downloading from dogpictures
3tdfpayjp1k51.jpg
cuz4a5np90k51.jpg
1e1g882z40k51.jpg
xX3OQgP.jpg
fuatv49mizj51.jpg
tk9khtspb1k51.jpg
pgbxxakm63k51.jpg
oeUI8Iy.jpg
vqklutghc1k51.jpg
1ctn7f0390k51.jpg
r7995a1dd3k51.jpg
qbjj06vaa0k51.jpg
q6nl05omyzj51.jpg
bl8bi5tsu2k51.jpg
gxc78spvxxj51.jpg
w0pdsr1hsyj51.jpg
9h19nq1k5vj51.jpg
y67tpittfyj51.jpg
Downloaded 18 from dogpictures

Downloading from dogswithjobs
5xxpn6xs7xj51.png
3mrgwnlum1k51.jpg
rs2uecgnb1k51.jpg
y077mg1974k51.jpg
kci6u8pc02k51.jpg
iho9wex0qrj51.jpg
109eyp6kjyj51.jpg
i86x3o6dutj51.jpg
Downloaded 8 from dogswithjobs

Downloading from GuiltyDogs
8z89s7a89dj51.jpg
c9rf2r516li51.jpg
pbdqr853rsh51.jpg
e9xihfbqdeh51.jpg
53gamygu9ch51.jpg
d3tq02dbbyg51.jpg
ifsmwutou2h51.jpg
Downloaded 7 from GuiltyDogs

Downloading from dog
1kloilrhc1k51.jpg
bwe1go65h1k51.jpg
8118vyqeg1k51.jpg
bajprhddg0k51.jpg
rlc7n4m6q0k51.jpg
z9p8llkuyyj51.jpg
dhdi10myx2k51.jpg
6zflnt9hozj51.jpg
niptrbxzf2k51.jpg
jxi3vrd901k51.jpg
u8eykob35yj51.jpg
5hwj8cce6zj51.png
9nr2t4f0vzj51.jpg
ozs8tuu7mzj51.jpg
0h1fwfqhh3k51.jpg
Downloaded 15 from dog

Downloaded 48 in total
```