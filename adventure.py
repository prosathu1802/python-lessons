class Person:
        
        def __init__(self):
                    self.location = {}
                            self.flame = Flame() 
                                    self.ice = Ice()  
                                            self.light = Light()
                                                    self.dark = Dark()

                                                        def start(self):
                                                                    print("Let's begin your adventure")
                                                                            self.location[self.flame.location] = self.flame.desc
                                                                                    self.location[self.ice.location] = self.ice.desc
                                                                                            self.location[self.dark.location] = self.dark.desc
                                                                                                    self.location[self.light.location]= self.light.desc
                                                                                                            
                                                                                                                    response = None
                                                                                                                            while response != "Q":
                                                                                                                                            a =  "Would you go North, South, East, or West? or 'q' to finish your journey?  \n"
                                                                                                                                                        response = input(a).capitalize()
                                                                                                                                                                    if response not in self.location:
                                                                                                                                                                                        print("Please select available direction")
                                                                                                                                                                                                        continue
                                                                                                                                                                                                                print(self.location[response])
                                                                                                                                                                                                                          
                                                                                                                                                                                                                          class Ice:
                                                                                                                                                                                                                                  def __init__(self):
                                                                                                                                                                                                                                              self.desc = "\n The huge white door, upon opening, leading up to a white room with an extremely low temperature. \n"
                                                                                                                                                                                                                                                      self.location = "North"

                                                                                                                                                                                                                                                      class Flame:
                                                                                                                                                                                                                                                              def __init__(self):
                                                                                                                                                                                                                                                                          self.desc = "\n The red hellish looking gate with its heat spreading to the surrounding. Covering with condensed red liquid. \n"
                                                                                                                                                                                                                                                                                  self.location = "South"
                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                          class Dark:
                                                                                                                                                                                                                                                                                                  def __init__(self):
                                                                                                                                                                                                                                                                                                              self.desc = "\n The darkness is warping the room with no light visible along with an absolute silence. \n"
                                                                                                                                                                                                                                                                                                                      self.location = "West"

                                                                                                                                                                                                                                                                                                                      class Light:
                                                                                                                                                                                                                                                                                                                              def __init__(self):
                                                                                                                                                                                                                                                                                                                                          self.desc = "\n The brightness emits from the room is extremely tense causing vision to be disable. \n"
                                                                                                                                                                                                                                                                                                                                                  self.location = "East"


                                                                                                                                                                                                                                                                                                                                                  person = Person()
                                                                                                                                                                                                                                                                                                                                                  person.start()


