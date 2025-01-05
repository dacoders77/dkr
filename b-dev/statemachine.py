from transitions import Machine # https://github.com/pytransitions/transitions?tab=readme-ov-file
import random


class Hero():
    def __init__(self, name):
        # Transitions are made throughout these states
        self.states = ["asleep", "hungry", "hanging out", "sweaty", "saving the world"]
        self.name = name
        self.kittens_rescued = 0
        self.machine = Machine(model=self, states=self.states, initial="asleep")

        # Transition. Can be many. This transition called by invoking "wake_up" method
        # do i need to say trigger= explicitly
        # States: asleep, hungry, hanging out
        # trigger | source | destination

        # Trigger: The method name (e.g., wake_up) that initiates the transition.
        # Source: The current state from which the transition can occur.
        # Destination (dest): The state to move to after the transition.
        # Transitions can also specify actions (before and after) and conditions for more control.
        # Can go to "hanging out state" on from "asleep" state. The only way
        self.machine.add_transition(trigger="wake_up", source="asleep", dest="hanging out")

        # When the work_out method is called, the Hero transitions from 'hanging out' to 'hungry'.
        self.machine.add_transition("work_out", "hanging out", "hungry")

        # Regular transition pair
        self.machine.add_transition("eat", "hungry", "hanging out")

        # Before action is added. Invoked as a separate function
        # Can place there: menu render, other game logic
        # If * is set as source, it means that you can go from any state to "saving the world"
        self.machine.add_transition("distress_call", "*", "saving the world", before="change_into_super_secret_costume")

        # After action
        self.machine.add_transition("complete_mission", "saving the world", "sweaty", after="update_journal")

        # Condition. "is_exhaused" function call. This transition happens only if the is_exhausted condition returns True and it comes from Sweaty
        self.machine.add_transition("clean_up", "sweaty", "asleep", conditions=["is_exhausted"])

        self.machine.add_transition("clean_up", "sweaty", "hanging out")

        # Can go from any state to asleep
        self.machine.add_transition("nap", "*", "asleep")




@property
def is_exhausted(self):
    # Coin toss. Not working?
    #return random.random() < 0.5
    return True

def change_into_super_secret_costume(self):
    print("Beauty, eh?")



batman = Hero("Batman")
print(batman.state) # Show current state of Hero (object)
batman.wake_up() # To hanging out state
print(batman.state)
#batman.clean_up() # To
#print(batman.state)













