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


def generate_random_combo(combo_length=3, stupid=False):
    combo = []
    if stupid:
        techniques = KICKS + ('headbutt',)
    else:
        techniques = KICKS
    while len(combo) < combo_length:
        combo.append(random.choice(techniques))
    return ', '.join(combo)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--length',
        type=int,
        default=3,
        help='Length of the combination to generate.'
    )
    parser.add_argument(
        '--stupid',
        action='store_true'
    )
    args = parser.parse_args()
    combo_length = args.length
    if args.stupid:
        stupid = True
    else:
        stupid = False

    result = generate_random_combo(combo_length, stupid)
    print(result)
