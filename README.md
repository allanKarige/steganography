# steganography
Steganography is sending a message in a hidden way by hiding it in plain site.In this project I encoded a message in an image.I altered the last bits in the 
red pixels of the image to match the bits of my text message.I also hid information about the message i.e how long it was in the last blue pixel and how long 
each word was in the green pixels entirely.Ofcourse it could be simplified,however I wanted it to be almost impossible to know.

The main functions are encode and decode functions.
This project was inspired by the popular youtube channel computerphile where a video about this was done.
The limit of the message which can be sent depends on the number of pixels in the image.
