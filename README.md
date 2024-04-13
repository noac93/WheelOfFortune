# WheelOfFortune

## Description
Wheel Of Fortune is a word guessing game.

## Parameters
- `<words_file>`: Path to a JSON file containing a list of words and categories.
- `<num_of_words>`: Number of words to be used in the game. (optional, defaults to 10)
- `<player_names>`: Player names separated by spaces. (optional, defaults to 2 players - player1 and player2)

## How to run
1. git clone git@github.com:noac93/WheelOfFortune.git 
2. cd <project_directory>
3. <main.py_path> <words_file> <num_of_words>
4. Optional, if you need to run tests: <code>pip install -r requirements.txt</code>

### Example
```python main.py words.json 5 Player1 Player2 Player3```

## Example JSON File
```json
{
  "words": [
    {"word": "apple", "category": "fruit"},
    {"word": "teacher", "category": "profession"},
    {"word": "uncle", "category": "family members"},
    {"word": "stomach", "category": "body parts"},
    {"word": "A blessing in disguise", "category": "phrase"},
    {"word": "computer", "category": "electronics"},
    {"word": "dog", "category": "animal"},
    {"word": "engineer", "category": "profession"},
    {"word": "brother", "category": "family members"},
    {"word": "eye", "category": "body parts"},
    {"word": "the whole nine yards", "category": "phrase"},
    {"word": "banana", "category": "fruit"},
    {"word": "doctor", "category": "profession"},
    {"word": "aunt", "category": "family members"},
    {"word": "heart", "category": "body parts"},
    {"word": "bite the bullet", "category": "phrase"},
    {"word": "car", "category": "vehicle"},
    {"word": "elephant", "category": "animal"},
    {"word": "lawyer", "category": "profession"},
    {"word": "sister", "category": "family members"}
  ]
}
```

## Unit Tests
UTs should be run with pytest