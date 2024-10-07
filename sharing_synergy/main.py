import sys
from sharing_synergy.cli.parser import create_parser

def kadd(url):
    print(f"This will add something by url: {url}")

def klist():
    print("This will list something")

def kremove(feed_name):
    print(f"This will remove something by name: {feed_name}")

def ksummarize(feed_name, output_name):
    print(f"This will summarize something by name: {feed_name} into: {output_name}")

def ktranslate(feed_name, desired_language, output_name):
    print(f"This will translate something by name: {feed_name} into desired language: {desired_language} into feed: {output_name}")

def kkeywords(feed_name, output_feed):
    print(f"This will find the keywords in feed: {feed_name} and put it in feed {output_feed}")

def kpublish(feed_name):
    print(f"This will publish {feed_name}")

def khelp():
    print("""
    Available commands:
    help  - Show this help message
    add [url]  - adds an article to the system using a URL
    list   - Displays available feeds or articles in the current context
    remove [feed name]  - Removes a feed
    summarize [feed name] [output name]  - Summarizes all the articles in the selected feed. This creates a new feed.
    translate [feed name] [desired language] [output name]  - Translates all the articles in a feed to a desired language, This creates new feed.
    keywords [feed name] [output name]   - Searches the feed for related keywords
    publish [feed name]   - Publishes a newly transformed feed. A confirmation message that includes a UUID and HTML link is provided
    """)

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command == "add":
        kadd(args.url)
    elif args.command == "list":
        klist()
    elif args.command == "remove":
        kremove(args.feed_name)
    elif args.command == "summarize":
        ksummarize(args.feed_name, args.output_name)
    elif args.command == "translate":
        ktranslate(args.feed_name, args.desired_language, args.output_name)
    elif args.command == "keywords":
        kkeywords(args.feed_name, args.output_name)
    elif args.command == "publish":
        kpublish(args.output_name)
    else:
        parser.print_help()