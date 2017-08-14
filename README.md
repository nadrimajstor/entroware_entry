![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)
Sound and images of entroware_entry by Ivan Pejić aka nadrimajstor is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/)

***

## Ubuntu Podcast Entroware Apollo laptop contest entry

First we have [image.ppm](https://github.com/nadrimajstor/entroware_entry/blob/master/image.ppm) - a 20 color image.

![image preview](docs/image_preview.png)

> Well... Technically black and white are not colors...
> Nevertheless, image.ppm does consists of only 20 uniqe pixel values :smile:

Now if you clone the repo,
```bash
git clone https://github.com/nadrimajstor/entroware_entry.git
```
and run the 20 lines python script:
```bash
cd entroware_entry
./dec.py
```
you will get `sound.opus` a 20 seconds sound rendering of a scan of a 1927 [Piano Roll](https://en.wikipedia.org/wiki/Piano_roll) :stuck_out_tongue_winking_eye:

Use your favourite player or:
```bash
sudo apt install opus-tools
padsp opusdec sound.opus
```

:sparkles:
