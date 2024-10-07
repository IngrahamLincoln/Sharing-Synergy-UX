import argparse

def create_parser():
    # Create the top-level parser
    parser = argparse.ArgumentParser(
        description="Sharing Synergy CLI tool"
    )

    # Add the verbose flag for debugging purposes
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')

    # Set up subcommands (like `add`, `remove`, etc.)
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # `help` is implicit since argparse handles it automatically
    # Add the commands below

    # `add` command: expects a URL
    parser_add = subparsers.add_parser('add', help='Add an article using a URL')
    parser_add.add_argument('url', type=str, help='URL of the article to add')

    # `list` command: no arguments needed
    parser_list = subparsers.add_parser('list', help='List available feeds or articles')

    # `remove` command: expects a feed name
    parser_remove = subparsers.add_parser('remove', help='Remove a feed')
    parser_remove.add_argument('feed_name', type=str, help='Name of the feed to remove')

    # `summarize` command: expects a feed name and output name
    parser_summarize = subparsers.add_parser('summarize', help='Summarize a feed')
    parser_summarize.add_argument('feed_name', type=str, help='Name of the feed to summarize')
    parser_summarize.add_argument('output_name', type=str, help='Name for the output feed')

    # `translate` command: expects a feed name, desired language, and output name
    parser_translate = subparsers.add_parser('translate', help='Translate a feed to a desired language')
    parser_translate.add_argument('feed_name', type=str, help='Name of the feed to translate')
    parser_translate.add_argument('desired_language', type=str, help='Language to translate into (e.g., "fr" for French)')
    parser_translate.add_argument('output_name', type=str, help='Name for the translated output feed')

    # `keywords` command: expects a feed name and output name
    parser_keywords = subparsers.add_parser('keywords', help='Search for related keywords in a feed')
    parser_keywords.add_argument('feed_name', type=str, help='Name of the feed to search')
    parser_keywords.add_argument('output_name', type=str, help='Name for the output file')

    # `publish` command: expects a feed name
    parser_publish = subparsers.add_parser('publish', help='Publish a transformed feed')
    parser_publish.add_argument('feed_name', type=str, help='Name of the feed to publish')

    # Parse the arguments
    return parser