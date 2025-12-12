## rai's scripts
python things to help me use the computer

how to use:
1. make sure the top-level comment on each script matches the output of `which python`
2. create a symlink to each script you want to use in `~/.local/bin`
    - whatever you name the symlink will be what you type in the console to run the script!
3. have fun!

### `yt_dl`
downloads a youtube link using [yt-dlp](https://github.com/yt-dlp/yt-dlp) (by default into `/media/music/<artist>/<album>`) and then converts it to a standard format using [ffmpeg](https://www.ffmpeg.org/) (by default `m4a`).

arguments:
1. `artist`: used in the download path (`/media/music/<artist>/<album>`)
2. `album`: used in the download path (`/media/music/<artist>/<album>`)
3. `link`: any youtube URL (playlist, youtube music link, video, etc) to be downloaded

i recommend using [picard](https://picard.musicbrainz.org/) to apply proper metadata after downloading.