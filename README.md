# facial-recognition
IOT in University Restaurant to reduce food waste

This project was developed as the final work of the Operating Systems discipline, and intends to use facial
recognition and IOT's to reduce food waste in university restaurants. The idea was conceived in the
following way: In the restaurant, in front of the garbage can, we would have some kind of camera,
connected to a machine running this facial recognition script. The bin would have a scale that would
weigh the amount of food being thrown away at that moment, this value would be captured, either
directly from the main machine or through Arduino. The script will associate that identified face with the
received weight value, and, if this amount is greater than a maximum amount of waste tolerance, the
script will access the database through the key without facial recognition, which is the number of
enrollment, and send an awareness and alert email to the user. Remembering that no project has two
phases, the primary one, which would be the registration of all faces and information, such as registration
number and e-mail, and in the second, the main script itself. In the project I used Python, SQLite, the
face_recognition library, numpy to compare the values received in recognition, and cv2 to capture the
image.
