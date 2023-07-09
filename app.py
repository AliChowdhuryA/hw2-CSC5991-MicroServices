from flask import Flask, jsonify, request
import random

app = Flask(__name__)

jokes = [
    "What do you call a cow with no legs? Ground beef!",
    "What do you get when you cross a snowman and a vampire? Frostbite!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "Why did the chicken cross the road? To get to the other side",
    "What gets wet as dries and dries as it gets wet? A towel",
    "What did the bear say when he saw something? I bear witness",
    "how do pilots hide? in plain sight?",
    "programmers with glasses cant c#",
    "underachieving programmers get a c++",
    "a programmer walks into a bar and compiled at run time",
    "tenth joke placeholder text",
]


@app.route('/jokes', methods=['GET'])
def get_jokes():
    num = int(request.args.get('num', default=1))
    random_jokes = random.sample(jokes, num)
    return jsonify(random_jokes)


if __name__ == '__main__':
    app.run(debug=True)
