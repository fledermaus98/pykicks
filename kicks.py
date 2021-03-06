import argparse
import random


KICKS = (
    'front',
    'jump front',
    'skip front',
    'flying front',
    'roundhouse',
    'jump roundhouse',
    'skip roundhouse',
    'flying roundhouse',
    'axe',
    'jump axe',
    'flying axe',
    'flying spin axe',
    'spin flying roundhouse',
    'side',
    'step side',
    'flying side',
    'hook',
    'spin hook',
    'jump spin hook',
    'flying spin hook',
    'back',
    'jump back',
    'flying back',
    'inside-out crescent',
    'outside-in crescent',
    'flying crescent',
    'spin crescent'
)


def generate_random_combo(combo_length=3):
    combo = []
    while len(combo) < combo_length:
        combo.append(random.choice(KICKS))
    return ', '.join(combo)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--length',
        type=int,
        default=3,
        help='Length of the combination to generate.'
    )
    args = parser.parse_args()
    combo_length = args.length

    result = generate_random_combo(combo_length)
    print(result)
