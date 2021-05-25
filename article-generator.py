#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import random
import string
from sys import argv

def generate_word():
    length = random.randint(1, 10)
    word = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    return word


def generate_sentence(words):
    return ' '.join([generate_word() for i in range(words)])


def generate_categories(num_categories):
    return [generate_word() for i in range(num_categories)]

def get_random_date():
    year = random.choice(range(1950, 2021))
    month = random.choice(range(1, 13))
    day = random.choice(range(1, 29))
    hours = random.choice(range(0, 24))
    minutes = random.choice(range(0, 60))
    seconds = random.choice(range(0, 60))
    
    return datetime(year, month, day, hours, minutes, seconds).strftime('%Y-%m-%d_%H:%M:%S')


def create_post(output_dir):
    title = generate_sentence(8)
    desc = generate_sentence(20)
    cat = random.choice(categories)

    slug = title.replace(' ', '-').lower()
    slug = ''.join(c for c in slug if c.isalnum() or c == '-')

    with open('%s/%s.md' % (output_dir, get_random_date()), 'w') as f:
        f.write('+++\n')
        f.write('title = "%s"\n' % title)
        f.write('description = "%s"\n' % desc)
        f.write('categories = [\n  "%s"\n]\n' % cat)
        f.write('date = "%s"\n' % datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S-00:03'))
        f.write('slug = "%s"\n' % slug)
        f.write('+++\n\n')

        num_paragraphs = random.randint(5, 10)

        for i in range(num_paragraphs):
            f.write(generate_sentence(random.randint(50, 100)))
            f.write('\n\n')


# Set defaults
output_dir = 'content/posts'
num_posts = 200
num_categories = 10

# Generate random categories
categories = generate_categories(num_categories)


if __name__ == '__main__':
    for i in range(num_posts):
        create_post(output_dir)


