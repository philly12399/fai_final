from game.players import BasePokerPlayer
import random as rand
import game.visualize_utils as U
import cardStrat  as cs

class myPlayer(BasePokerPlayer):
    def __init__(self):
       pass
        
    def declare_action(self, valid_actions, hole_card, round_state):
        #TODO
        #round_state small_blind_pos big_blind_pos
        street = round_state['street']
        if(street == 'preflop'):
            return cs.preFlop(valid_actions, hole_card, round_state)
        elif(street == 'flop'):
            return cs.theFlop(valid_actions, hole_card, round_state)
        elif(street == 'turn'):
            return cs.theTurn(valid_actions, hole_card, round_state)
        elif(street == 'river'):
            return cs.theRiver(valid_actions, hole_card, round_state)

    def receive_game_start_message(self, game_info):
        #print(U.visualize_game_start(game_info, self.uuid))
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
        #print(U.visualize_round_start(round_count, hole_card, seats, self.uuid))
        pass

    def receive_street_start_message(self, street, round_state):
        #print(U.visualize_street_start(street, round_state, self.uuid))
        pass

    def receive_game_update_message(self, new_action, round_state):
        #print(U.visualize_game_update(new_action, round_state, self.uuid))
        pass

    def receive_round_result_message(self, winners, hand_info, round_state):
        #print(U.visualize_round_result(winners, hand_info, round_state, self.uuid))
        pass

def setup_ai():
    return myPlayer()
