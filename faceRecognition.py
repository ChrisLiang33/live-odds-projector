import faceRecognition

know_fighter_image = faceRecognition.load_image_file('fighter.jpg')
known_fighter_encoding = faceRecognition.face_encodings(know_fighter_image)[0]

ret, frame = cap.read()

if ret:
  rgb_frame = frame[:, :, ::-1]
  # Find all face locations and face encodings in the current frame
  face_locations = face_recognition.face_locations(rgb_frame)
  face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
  for face_encoding in face_encodings:
    match = face_recognition.compare_faces([known_fighter_encoding], face_encoding)
    if match[0]:
      print("Fighter identified!")
    else:
      print("Fighter not recognized.")