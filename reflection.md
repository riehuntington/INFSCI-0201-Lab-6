This is the file I will be answering questions in for Lab 6. I have the Lab 6 Report saved (the assignment said to
just submit the Github folder so that is what I did!)

a. Inheritance, in short, is when a more simplified, downstream class receives attributes, methods, and other class
characteristics from another class so that those same class characteristics do not need to be repetitively programmed
in multiple classes. In this example, the Hero and Enemy classes inherit attributes such as name, health, and weapon
from the Character class, as these attributes are the same in both Hero and Enemy. They also inherit the equip and
attack methods, as they are made use of in both classes.

b. Association is when two classes are related to one another. In this case, weapons are associated with the heroes
or enemies who hold them through the equip method. Once this is done, a character can use their weapon to attack other
characters. With the way that this program is set up, characters and weapons have a one-to-one relationship, as each
character can only hold one weapon. This is an example of aggregation, as characters and weapons can exist independently
of one another (as a character does not have to exist for their weapon to exist.)

c. Encapsulation is when variables (attributes) and functions (methods) belong to a specific class and are contained.
This helps us organize variables and functions that, without the class or object, would be unorganized. In this case,
looking at the Character class for example, name, health, and weapon are all attributes that belong to, or are
encapsulated in, the Character class. To access these variables, we would need to access them through the specific
object that they belong to.