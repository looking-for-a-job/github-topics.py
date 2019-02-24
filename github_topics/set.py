#!/usr/bin/env python
"""set repo topics"""
import click
import github_topics

MODULE_NAME = "github_topics.replace"
USAGE = 'python -m %s fullname topics ...' % MODULE_NAME
PROG_NAME = 'python -m %s' % USAGE


@click.command()
@click.argument('fullname')
@click.argument('topics', nargs=-1, required=True)
def _cli(fullname, topics):
    github_topics.replace(fullname, topics)


if __name__ == "__main__":
    _cli()
