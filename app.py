"""
Endpoints:
- GET /word?count=X  -> returns a JSON array of X words (X <= 10)

To run:
    pip install flask
    python3 app.py

"""
from flask import Flask, request, jsonify
import random
from time import sleep

app = Flask("RandWordAPI")

VALID_KEYS = ["REPLACE_ME"]

# A list of 100 random-ish English words
WORDS = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "iris", "jasmine",
    "kettle", "lemon", "mango", "nectarine", "olive", "papaya", "quince", "raspberry", "strawberry", "tangerine",
    "umbrella", "violet", "willow", "xenon", "yam", "zucchini", "acorn", "beacon", "cactus", "dolphin",
    "ember", "falcon", "gadget", "harbor", "igloo", "jungle", "kitten", "lantern", "meteor", "nebula",
    "oracle", "pioneer", "quartz", "ripple", "summit", "tundra", "utopia", "vortex", "wander", "xylophone",
    "yonder", "zephyr", "anchor", "breeze", "crimson", "dewdrop", "echo", "fern", "glimmer", "harvest",
    "indigo", "journey", "kismet", "lagoon", "meadow", "noodle", "opal", "prairie", "quail", "raven",
    "saffron", "thimble", "unicorn", "vista", "whisper", "xenial", "yarrow", "zest", "aurora", "blossom",
    "cinder", "drift", "emberly", "fable", "glisten", "horizon", "ivory", "jovial", "kinetic", "lunar",
    "mosaic", "nimbus", "opaline", "paladin", "quiver", "reverie", "solace", "travail", "umbra", "valiant"
]

MAX_COUNT = 10


@app.route('/word', methods=['GET'])
def get_words():
    """Return a JSON array of random words.

    Query param: count (int) - number of words to return (default 1, max 10)
    """
    count_param = request.args.get('count', '1')
    key = request.args.get('key', 'unauth')

    if key not in VALID_KEYS:
        sleep(random.random() * 5)
        return jsonify({"error": "unauthorized"}), 401
    try:
        count = int(count_param)
    except ValueError:
        return jsonify({"error": "count must be an integer"}), 400

    if count < 1 or count > MAX_COUNT:
        return jsonify({"error": f"count must be between 1 and {MAX_COUNT}"}), 400

    # If the caller requests more words than available, allow repeats by sampling with replacement
    if count <= len(WORDS):
        result = random.sample(WORDS, count)
    else:
        result = [random.choice(WORDS) for _ in range(count)]

    return jsonify(result)


@app.route('/', methods=['GET'])
def index():
    return "Simple Random Word API. Use /word?count=X to get words."


if __name__ == '__main__':
    # Run on 0.0.0.0 so it is reachable from other containers/hosts if needed
    app.run(host='0.0.0.0', port=5000)
