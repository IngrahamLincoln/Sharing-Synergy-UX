import argparse
import json

#write user provided url to JSON file.
def kadd(url):
    #slice URL to contain only feed name for easier reading on user end
    domain_name = url.split('//')[-1].split('/')[0].split('.')[-2]

    feed_data = {
        "url": url,
        "name": domain_name
    }

    try:
        #read existing data from the JSON file
        try:
            with open("feed_data.json", "r") as json_file:
                #load existing JSON data
                existing_data = json.load(json_file)
        except FileNotFoundError:
            
            existing_data = []

        #append the new feed data
        existing_data.append(feed_data)

        #write the updated list back to the JSON file
        with open("feed_data.json", "w") as json_file:
            json.dump(existing_data, json_file, indent=4)

        print(f"'{url}' added to feed list")

    except Exception as e:
        print(f"An error occurred while writing to the JSON file: {e}")

#list names of feeds that the user has added
def klist():
    try:
        with open("feed_data.json", "r") as json_file:
            feed_data = json.load(json_file)
            
            for item in feed_data:
                print(item["name"])

    except FileNotFoundError:
        print("No feed data found. Please add some feeds first.")
    except json.JSONDecodeError:
        print("Error decoding JSON. The file may be corrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")

def kremove(name):
    try:
        #read existing data from the JSON file
        with open("feed_data.json", "r") as json_file:
            existing_data = json.load(json_file)

        #filter out the item with the matching name
        new_data = [item for item in existing_data if item["name"] != name]

        #check if any items were removed
        if len(existing_data) == len(new_data):
            print(f"No item found with name '{name}'.")
        else:
            #write the updated list back to the JSON file
            with open("feed_data.json", "w") as json_file:
                json.dump(new_data, json_file, indent=4)
            print(f"Item with name '{name}' removed from feed list.")

    except FileNotFoundError:
        print("No feed data found. Please add some feeds first.")
    except json.JSONDecodeError:
        print("Error decoding JSON. The file may be corrupted.")
    except Exception as e:
        print(f"An error occurred while removing the item: {e}")

def ksummarize():
    print("This will summarize something")

def ktranslate():
    print("This will translate something")

def kkeywords():
    print("This do something with keywords")

def kpublish():
    print("This will publish")

#print information relating to user commands
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
                        help="Use 'syn_help' for a list of commands.")
    
    #argument for the URL for syn_add or name for kremove.
    parser.add_argument('argument', nargs='?', help="The URL to add or the name to remove.")

    args = parser.parse_args()

    #all the user commands are heralded by  and all kernal commands start with k, probably a good idea to provent users from accessing the kernel versions
    if args.command == "syn_help":
        khelp()

    elif args.command == "syn_add":
        if args.argument: 
            kadd(args.argument)
        else:
            print("Error: URL must be provided for the 'syn_add' command.")

    elif args.command == "syn_list":
        klist()

    elif args.command == "syn_remove":
        if args.argument: 
            kremove(args.argument)  
        else:
            print("Error: Name must be provided for the 'syn_remove' command.")

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

