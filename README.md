# Labeler
Labeler is used for going from a video (mp4) to a series of images (jpg) and generates a file mapping the JPEG image with the label assigned to it

# Usage
```
usage: label.py [-h] [-p PREFIX] [-o OUTPUT] [-i INPUT]

Labeling videos

optional arguments:
	-h, --help show this help message and exit
	-p PREFIX Prefix matching of videos
	-o OUTPUT Output directory to store result
	-i INPUT Input directory to search
```

So given a directory like the following

```
.
├── label.py
├── test_ir.mp4
└── test_rgb.mp4
```

The command `python label.py -p test_ -i . -o foo`
Looks in the directory `.`
Will find files `test_ir.mp4` and `test_rgb.mp4`
Creates a directory `foo`
Open up a window for each of the files
Wait for a key press and write the frames and key press to a file `foo/label`
Keeps going until either video finishes

Result of `foo/label`
```
test_ir.mp4_frame_000000.jpg,<label>
test_rgb.mp4_frame_000000.jpg,<label>
test_ir.mp4_frame_000001.jpg,<label>
test_rgb.mp4_frame_000001.jpg,<label>
test_ir.mp4_frame_000002.jpg,<label>
test_rgb.mp4_frame_000002.jpg,<label>
test_ir.mp4_frame_000003.jpg,<label>
test_rgb.mp4_frame_000003.jpg,<label>
test_ir.mp4_frame_000004.jpg,<label>
test_rgb.mp4_frame_000004.jpg,<label>
```

Result inside `foo`
```
foo
├── labels
├── test_ir.mp4_frame_000000.jpg
├── test_ir.mp4_frame_000001.jpg
├── test_ir.mp4_frame_000002.jpg
├── test_ir.mp4_frame_000003.jpg
├── test_ir.mp4_frame_000004.jpg
├── test_ir.mp4_frame_000005.jpg
├── test_ir.mp4_frame_000006.jpg
├── test_ir.mp4_frame_000007.jpg
```
