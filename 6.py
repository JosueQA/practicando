from typing import List, Dict

def match_gloves(gloves: List[Dict[str, str]]) -> List[str]:
    # Code here
    for pos, val in enumerate(gloves):
        
        position = pos
        glove_hand = val

        while position <= (len(gloves) - 1):
            
            if (position == (len(gloves) -1)):
                break
            else:
                print(gloves[position + 1])
                position = position + 1

    return []
      


GLOVES = [
          { "hand": 'L', "color": 'red' },
          { "hand": 'R', "color": 'red' },
          { "hand": 'R', "color": 'green' },
          { "hand": 'L', "color": 'blue' },
          { "hand": 'L', "color": 'green' }
          ]

match_gloves(GLOVES)
["red", "green"]

