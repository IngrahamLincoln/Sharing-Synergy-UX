import argparse

#all these commands do not have functionality yet other than being callable
def kadd():
    print("This will add something")

def klist():
    print("This will list something")

def kremove():
    print("This will remove something")

def ksummarize():
    print("This will summarize something")

def ktranslate():
    print("This will translate something")

def kkeywords():
    print("This do something with keywords")

def kpublish():
    print("This will publish")

#first command to do anything
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
    parser = argparse.ArgumentParser(description="Command-line tool")
    
    #here is where the commands are defined, if the name of a command needs to be changed it needs to change here, currently uses "syn_" instead of "syn " because the space caused issues if you want to change that go for it
    parser.add_argument('command', choices=['syn_help', 'syn_add', 'syn_list', 'syn_remove', 'syn_summarize', 'syn_translate', 'syn_keywords', 'syn_publish'], 
                        help="Use ' syn_help' for a syn_list of commands.")
    
    args = parser.parse_args()

    #all the user commands are heralded by  and all kernal commands start with k, probably a good idea to provent users from accessing the kernel versions
    if args.command == "syn_help":
        khelp()
    elif args.command == "syn_add":
        kadd()
    elif args.command == "syn_list":
        klist()
    elif args.command == "syn_remove":
        kremove()
    elif args.command == "syn_summarize":
        ksummarize()
    elif args.command == "syn_translate":
        ktranslate()
    elif args.command == "syn_keywords":
        kkeywords()
    elif args.command == "syn_publish":
        kpublish()

if __name__ == "__main__":
    main()
