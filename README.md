## rai's scripts
python things to help me use the computer

how to use:
1. make sure the top-level comment on each script matches the output of `which python`
2. make sure that your `~/.bashrc` file contains `~/.local/bin` in the PATH
3. create a symlink to each script you want to use in `~/.local/bin`
    - whatever you name the symlink will be what you type in the console to run the script!
    - if you get a `permission denied` error, make the symlink executable with `chmod +x <name>`
3. have fun!

### `yt_dl`
downloads a youtube link using [yt-dlp](https://github.com/yt-dlp/yt-dlp) (by default into `/media/music/<artist>/<album>`) and then converts it to a standard format using [ffmpeg](https://www.ffmpeg.org/) (by default `m4a`).
</br>
always runs in `/media/music`.

arguments:
1. `artist`: used in the download path (`/media/music/<artist>/<album>`)
2. `album`: used in the download path (`/media/music/<artist>/<album>`)
3. `link`: any youtube URL (playlist, youtube music link, video, etc) to be downloaded

i recommend using [picard](https://picard.musicbrainz.org/) to apply proper metadata after downloading.

### `convert_walkman`
converts a music library into a version compatible with the walkman `NWZ-E463`, using `ffmpeg` and `exiftool`.
converts to mp3, downgrades metadata to id3v2, and edits album art to a walkman-compatible format.
</br>
runs in the current directory and takes no arguments.

### `convert_dir`
converts all files in the current directory to the specified format using `ffmpeg`. 

arguments:
1. `extension`: the file extension to conver to

### `music_stats`
prints out stats for `/media/music/` such as number of albums, number of artists, average albums per artist, etc.
</br>
runs in the current directory and takes no arguments.