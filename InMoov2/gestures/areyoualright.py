def areyoualright():
  inMoov.startedGesture()
  inMoov.setHeadVelocity(43.0,-1,43.0,43.0,-1)
  inMoov.moveHead(90,60,90,180,65)
  sleep(0.5)
  inMoov.moveHead(90,120,90,180,65)
  sleep(0.7)
  inMoov.moveHead(90,60,90,180,65)
  sleep(0.7)
  inMoov.moveHead(90,120,90,180,65)
  sleep(0.7)
  inMoov.moveHead(90,90,90,180,65)
  sleep(0.7)
  x = (random.randint(1, 2))
  if x == 1:
    inMoov.mouth.speak("i am very, super, mega bored")
    inMoov.moveArm("left",85,93,42,16)
    inMoov.moveArm("right",87,93,37,18)
    inMoov.moveHand("left",124,82,65,81,41,143)
    inMoov.moveHand("right",59,53,89,61,36,21)
    inMoov.moveTorso(90,90,90)
    sleep(0.2)
    inMoov.setHeadVelocity(-1,-1,-1,-1,-1)
    inMoov.moveHead(90,90,90,90,65)
    sleep(1)
    relax()
  if x == 2:
    inMoov.mouth.speak("I feel like a machine, doing the same thing over and over")
    inMoov.moveArm("left",85,93,42,16)
    inMoov.moveArm("right",87,93,37,18)
    inMoov.moveHand("left",124,82,65,81,41,143)
    inMoov.moveHand("right",59,53,89,61,36,21)
    inMoov.moveTorso(90,90,90)
    sleep(0.2)
    inMoov.setHeadVelocity(-1,-1,-1,-1,-1)
    inMoov.moveHead(90,90,90,90,65)
    sleep(1)
  inMoov.finishedGesture()
  relax()